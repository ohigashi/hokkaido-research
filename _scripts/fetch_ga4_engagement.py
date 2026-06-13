#!/usr/bin/env python3
"""GA4 Data API から記事別エンゲージメントを取得し、スコア化して保存する。

前提:
- Google Cloud Console で service account を作成し、 GA4 プロパティに「閲覧者」権限で追加
- JSON キーを `_secrets/ga4-service-account.json` に保存 ( gitignore 済み )
- GA4 プロパティ ID を環境変数 GA4_PROPERTY_ID または `_secrets/ga4-config.json` に保存

取得指標 ( 過去 28 日間 ):
- pagePath ( フィルタ: /articles/{slug}.html )
- screenPageViews
- userEngagementDuration ( 平均算出 )
- engagementRate
- sessions

スコア化 ( 0-25 ):
- userEngagementDuration: 上位 25% +10 / 上中 +6 / 中央 +3 / 下位 0
- engagementRate × screenPageViews ( ボリューム重み ): 上位 25% +10 / 上中 +6 / 中央 +3 / 下位 0
- screenPageViews 単独で 100PV+ なら +5 ( 露出量ボーナス )

出力: _ga4_engagement.json
形式: [{slug, pv, engagement_seconds_avg, engagement_rate, ga4Score, raw}, ...]
"""
import json
import os
import sys
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

# Property ID
property_id = os.environ.get("GA4_PROPERTY_ID")
if not property_id:
    cfg = SECRETS / "ga4-config.json"
    if cfg.exists():
        property_id = json.loads(cfg.read_text())["property_id"]

if not property_id:
    print("ERROR: GA4_PROPERTY_ID が未設定。環境変数または _secrets/ga4-config.json に設定してください。", file=sys.stderr)
    sys.exit(1)

# Service account credential
cred = SECRETS / "ga4-service-account.json"
if not cred.exists():
    print(f"ERROR: {cred} が存在しません。 README の手順で配置してください。", file=sys.stderr)
    sys.exit(1)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(cred)

client = BetaAnalyticsDataClient()

# 記事ページのみ
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
    dimensions=[Dimension(name="pagePath")],
    metrics=[
        Metric(name="screenPageViews"),
        Metric(name="userEngagementDuration"),
        Metric(name="engagementRate"),
        Metric(name="sessions"),
    ],
    date_ranges=[DateRange(start_date="28daysAgo", end_date="yesterday")],
    dimension_filter=path_filter,
    limit=500,
)

response = client.run_report(req)

records = []
for row in response.rows:
    path = row.dimension_values[0].value
    if not path.startswith("/articles/") or not path.endswith(".html"):
        continue
    slug = path.replace("/articles/", "").replace(".html", "")
    if slug == "index":
        continue
    pv = int(row.metric_values[0].value or 0)
    user_eng_dur = float(row.metric_values[1].value or 0)
    eng_rate = float(row.metric_values[2].value or 0)
    sessions = int(row.metric_values[3].value or 0)
    avg_eng = user_eng_dur / sessions if sessions > 0 else 0
    records.append({
        "slug": slug,
        "pv": pv,
        "sessions": sessions,
        "engagement_seconds_avg": round(avg_eng, 1),
        "engagement_rate": round(eng_rate, 3),
        "engagement_volume": round(eng_rate * pv, 1),
    })

# パーセンタイル分布でスコア化
def quartile_score(values, target, points=(10, 6, 3, 0)):
    if not values:
        return points[3]
    sorted_v = sorted(values)
    n = len(sorted_v)
    rank = sum(1 for v in sorted_v if v <= target) / n
    if rank >= 0.75:
        return points[0]
    if rank >= 0.5:
        return points[1]
    if rank >= 0.25:
        return points[2]
    return points[3]


eng_vals = [r["engagement_seconds_avg"] for r in records]
vol_vals = [r["engagement_volume"] for r in records]

for r in records:
    s = 0
    s += quartile_score(eng_vals, r["engagement_seconds_avg"])
    s += quartile_score(vol_vals, r["engagement_volume"])
    if r["pv"] >= 100:
        s += 5
    r["ga4Score"] = s

OUT.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"GA4 取得 {len(records)} 記事 → {OUT.relative_to(ROOT)}")
print(f"\nTop 10 by ga4Score:")
for r in sorted(records, key=lambda x: -x["ga4Score"])[:10]:
    print(
        f"  {r['ga4Score']:>3}  pv={r['pv']:>4}  eng={r['engagement_seconds_avg']:>5.1f}s  "
        f"rate={r['engagement_rate']:.2%}  {r['slug']}"
    )
