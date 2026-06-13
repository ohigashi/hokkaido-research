#!/usr/bin/env python3
"""GA4 Data API から記事別エンゲージメントを取得し、スコア化して保存する。

質の定義 ( 2026-06-13 大東 ):
- 質の高い記事 = 内部回遊でよく読まれて、エンゲージメントも強い記事
- 外部バズで PV が高くても質の指標にしない
- 評価軸: internal_pv ( pageReferrer がサイト内 ) × engagement_seconds_avg

前提:
- Google Cloud Console で service account を作成し、 GA4 プロパティに「閲覧者」権限で追加
- JSON キーを `_secrets/ga4-service-account.json` に保存
- GA4 プロパティ ID を `_secrets/ga4-config.json` または環境変数 GA4_PROPERTY_ID に設定

取得指標 ( 過去 28 日間 ):
- pagePath × pageReferrer
- screenPageViews
- userEngagementDuration
- engagementRate
- sessions

集計:
- internal_pv = pageReferrer が同ドメイン ( hokkaido-research を含む ) の PV
- external_pv = それ以外の PV
- internal_engagement_avg = internal 行の userEngagementDuration 合計 / sessions 合計

ga4Score ( 0-25 ):
- internal_pv の四分位: 上位 25% +10 / 上中 +6 / 中央 +3 / 下位 0
- internal × engagement_avg ( ボリューム × 質 ): 上位 25% +10 / 上中 +6 / 中央 +3 / 下位 0
- internal_pv >= 50 なら +5

出力: _ga4_engagement.json
形式: [{slug, internal_pv, external_pv, engagement_seconds_avg, engagement_rate, ga4Score, raw}, ...]
"""
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

try:
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import (
        DateRange,
        Dimension,
        Metric,
        RunReportRequest,
        FilterExpression,
        Filter,
    )
except ImportError:
    print("ERROR: google-analytics-data がインストールされていません。", file=sys.stderr)
    print("pip install google-analytics-data", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SECRETS = ROOT / "_secrets"
OUT = ROOT / "_ga4_engagement.json"
INTERNAL_REFERRER_KEYWORDS = ["hokkaido-research", "lrg.jp"]

# Property ID
property_id = os.environ.get("GA4_PROPERTY_ID")
if not property_id:
    cfg = SECRETS / "ga4-config.json"
    if cfg.exists():
        property_id = json.loads(cfg.read_text())["property_id"]

if not property_id:
    print("ERROR: GA4_PROPERTY_ID が未設定。", file=sys.stderr)
    sys.exit(1)

cred = SECRETS / "ga4-service-account.json"
if not cred.exists():
    print(f"ERROR: {cred} が存在しません。", file=sys.stderr)
    sys.exit(1)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(cred)

client = BetaAnalyticsDataClient()

path_filter = FilterExpression(
    filter=Filter(
        field_name="pagePath",
        string_filter=Filter.StringFilter(
            value="/articles/",
            match_type=Filter.StringFilter.MatchType.CONTAINS,
        ),
    )
)

req = RunReportRequest(
    property=f"properties/{property_id}",
    dimensions=[Dimension(name="pagePath"), Dimension(name="pageReferrer")],
    metrics=[
        Metric(name="screenPageViews"),
        Metric(name="userEngagementDuration"),
        Metric(name="engagementRate"),
        Metric(name="sessions"),
    ],
    date_ranges=[DateRange(start_date="28daysAgo", end_date="yesterday")],
    dimension_filter=path_filter,
    limit=2000,
)

response = client.run_report(req)


def is_internal(referrer: str) -> bool:
    if not referrer:
        return False
    return any(k in referrer for k in INTERNAL_REFERRER_KEYWORDS)


# slug 別に集計
per_slug = defaultdict(lambda: {
    "internal_pv": 0,
    "external_pv": 0,
    "internal_eng_dur": 0.0,
    "external_eng_dur": 0.0,
    "internal_sessions": 0,
    "external_sessions": 0,
    "engagement_rate_weighted_num": 0.0,
    "engagement_rate_weighted_den": 0,
})

for row in response.rows:
    path = row.dimension_values[0].value
    referrer = row.dimension_values[1].value or ""
    if not path.startswith("/articles/") or not path.endswith(".html"):
        continue
    slug = path.replace("/articles/", "").replace(".html", "")
    if slug == "index":
        continue
    pv = int(row.metric_values[0].value or 0)
    eng_dur = float(row.metric_values[1].value or 0)
    eng_rate = float(row.metric_values[2].value or 0)
    sessions = int(row.metric_values[3].value or 0)

    bucket = per_slug[slug]
    if is_internal(referrer):
        bucket["internal_pv"] += pv
        bucket["internal_eng_dur"] += eng_dur
        bucket["internal_sessions"] += sessions
    else:
        bucket["external_pv"] += pv
        bucket["external_eng_dur"] += eng_dur
        bucket["external_sessions"] += sessions
    bucket["engagement_rate_weighted_num"] += eng_rate * pv
    bucket["engagement_rate_weighted_den"] += pv


records = []
for slug, b in per_slug.items():
    total_pv = b["internal_pv"] + b["external_pv"]
    internal_avg = (b["internal_eng_dur"] / b["internal_sessions"]
                    if b["internal_sessions"] > 0 else 0)
    overall_avg = ((b["internal_eng_dur"] + b["external_eng_dur"]) /
                   (b["internal_sessions"] + b["external_sessions"])
                   if (b["internal_sessions"] + b["external_sessions"]) > 0 else 0)
    eng_rate = (b["engagement_rate_weighted_num"] / b["engagement_rate_weighted_den"]
                if b["engagement_rate_weighted_den"] > 0 else 0)
    records.append({
        "slug": slug,
        "pv": total_pv,
        "internal_pv": b["internal_pv"],
        "external_pv": b["external_pv"],
        "internal_sessions": b["internal_sessions"],
        "engagement_seconds_avg": round(internal_avg, 1),  # 内部回遊ベース
        "engagement_seconds_avg_overall": round(overall_avg, 1),
        "engagement_rate": round(eng_rate, 3),
        "engagement_volume": round(b["internal_pv"] * internal_avg, 1),
    })


def quartile_score(values, target, points=(10, 6, 3, 0)):
    if not values:
        return points[3]
    sv = sorted(values)
    n = len(sv)
    rank = sum(1 for v in sv if v <= target) / n
    if rank >= 0.75:
        return points[0]
    if rank >= 0.5:
        return points[1]
    if rank >= 0.25:
        return points[2]
    return points[3]


internal_pv_vals = [r["internal_pv"] for r in records if r["internal_pv"] > 0]
vol_vals = [r["engagement_volume"] for r in records if r["engagement_volume"] > 0]

for r in records:
    s = 0
    s += quartile_score(internal_pv_vals, r["internal_pv"]) if internal_pv_vals else 0
    s += quartile_score(vol_vals, r["engagement_volume"]) if vol_vals else 0
    if r["internal_pv"] >= 50:
        s += 5
    r["ga4Score"] = s


OUT.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"GA4 取得 {len(records)} 記事 → {OUT.relative_to(ROOT)}")
print(f"\n質指標 ( 内部回遊 PV × 内部エンゲ秒 ) Top 10:")
for r in sorted(records, key=lambda x: -x["ga4Score"])[:10]:
    print(
        f"  {r['ga4Score']:>3}  intPV={r['internal_pv']:>3}  extPV={r['external_pv']:>3}  "
        f"intEng={r['engagement_seconds_avg']:>5.1f}s  {r['slug']}"
    )
