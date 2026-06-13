#!/usr/bin/env python3
"""Assess quality of all article HTML files and rank them.

構造スコア ( 0-100 ):
- Body length ( target 2,500+ chars ): up to 20
- Number of tables: up to 15
- Specific data ( numbers + Japanese counters ): up to 20
- External case detail ( proper nouns + years ): up to 15
- Sources ( URLs ): up to 10
- わたしたちにできること section: 10
- 中心問い callout: 5
- 残る資産 mention: 5

鮮度スコア ( 0-15 ): articles updatedAt からの経過日数
- 30 日内: 15
- 90 日内: 10
- 180 日内: 6
- 365 日内: 3
- それ以外: 0

将来追加: GA4 エンゲージメントスコア ( 0-25 )

Lower score = more improvement needed.
"""
import re
import json
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ART_DIR = ROOT / "articles"

# Common towns/orgs/years that indicate specific external cases
SPECIFIC_PATTERNS = [
    r"海士町", r"神山町", r"尾道", r"流山市", r"上士幌", r"ニセコ",
    r"札幌", r"旭川", r"函館", r"釧路", r"帯広", r"苫小牧", r"千歳",
    r"沖縄県", r"福岡", r"福井", r"京都", r"鳥取", r"鯖江市", r"智頭",
    r"19\d\d 年", r"20\d\d 年", r"2024", r"2025", r"2026",
    r"17 年", r"15 年", r"20 年", r"25 年", r"30 年",
]

JAPANESE_COUNTERS_RE = re.compile(
    r"\d+(?:\.\d+)?(?:兆|億|万|千|円|人|戸|本|社|件|個|種|位|頭|名|歳|台|軒|分|秒|時間|日|月|年|週|ha|km|m|kg|t|GW|MW|kW|%|％|ヶ所|箇所)"
)


def assess(html: str) -> dict:
    """Return dict with score and breakdown."""
    # Extract body content
    body_match = re.search(r'<article class="body">(.+?)</article>', html, re.DOTALL)
    body = body_match.group(1) if body_match else ""

    # Strip HTML tags for text
    text = re.sub(r"<[^>]+>", "", body)
    text_no_space = re.sub(r"\s+", "", text)

    # Scores
    scores = {}

    # 1. Body length
    char_count = len(text_no_space)
    scores["length"] = min(20, int(char_count / 125))  # 2500 chars = 20 pts

    # 2. Tables
    table_count = body.count("<table>")
    scores["tables"] = min(15, table_count * 5)  # 3 tables = 15

    # 3. Specific data ( number+counter )
    counter_matches = JAPANESE_COUNTERS_RE.findall(text)
    scores["specific_data"] = min(20, len(counter_matches))

    # 4. External case detail
    specific_hits = 0
    for pat in SPECIFIC_PATTERNS:
        if re.search(pat, text):
            specific_hits += 1
    scores["case_detail"] = min(15, specific_hits * 2)

    # 5. Sources
    source_urls = re.findall(r'article-sources-block.+?</div>\s*</div>', html, re.DOTALL)
    if source_urls:
        url_count = len(re.findall(r"https?://", source_urls[0]))
    else:
        url_count = 0
    scores["sources"] = min(10, url_count * 2)

    # 6. わたしたちにできること
    has_habits = "わたしたちにできること" in body
    scores["habits"] = 10 if has_habits else 0

    # 7. 中心問い
    has_central = "中心問い" in body or "中心問い" in text
    scores["central"] = 5 if has_central else 0

    # 8. 残る資産
    has_assets = "残る資産" in text
    scores["assets"] = 5 if has_assets else 0

    total = sum(scores.values())
    return {
        "char_count": char_count,
        "table_count": table_count,
        "scores": scores,
        "total": total,
    }


def freshness_score(updated_at_str):
    """Return ( score 0-15, days_since_update )."""
    if not updated_at_str:
        return 0, 9999
    try:
        d = datetime.strptime(updated_at_str, "%Y-%m-%d").date()
    except Exception:
        return 0, 9999
    days = (date.today() - d).days
    if days <= 30:
        return 15, days
    if days <= 90:
        return 10, days
    if days <= 180:
        return 6, days
    if days <= 365:
        return 3, days
    return 0, days


def classify_priority(pv, eng_sec, pv_thresholds, eng_thresholds):
    """PV × エンゲージメント の象限から打ち手タイプを判定。

    Returns:
      ( type, label, action )
      type: A / B / C / D / E / F / NODATA
    """
    if pv is None or eng_sec is None:
        return "NODATA", "GA4 データ未取得", "構造スコアベースで判定"
    pv_lo, pv_hi = pv_thresholds
    eng_lo, eng_hi = eng_thresholds
    pv_band = "high" if pv >= pv_hi else ("low" if pv <= pv_lo else "mid")
    eng_band = "high" if eng_sec >= eng_hi else ("low" if eng_sec <= eng_lo else "mid")
    table = {
        ("high", "high"): ("D", "高エンゲ × 高 PV", "維持 ( 触らない )"),
        ("high", "mid"):  ("A", "高エンゲ × 中 PV", "露出 + SEO 強化"),
        ("high", "low"):  ("A", "高エンゲ × 低 PV", "露出 + SEO 強化"),
        ("mid", "high"):  ("F", "中エンゲ × 高 PV", "コンテンツ強化"),
        ("mid", "mid"):   ("F", "中エンゲ × 中 PV", "ローテーション ( コンテンツ )"),
        ("mid", "low"):   ("C", "中エンゲ × 低 PV", "SEO 先 → 流入後にコンテンツ"),
        ("low", "high"):  ("B", "低エンゲ × 高 PV", "コンテンツ強化 ( 離脱対策 )"),
        ("low", "mid"):   ("B", "低エンゲ × 中 PV", "コンテンツ強化"),
        ("low", "low"):   ("E", "低エンゲ × 低 PV", "根本見直し ( 両方強化 )"),
    }
    key = (eng_band, pv_band)
    return table.get(key, ("NODATA", "未分類", "構造スコアベース"))


def percentile_thresholds(values, lo_pct=33, hi_pct=67):
    """Return ( lo_threshold, hi_threshold ) at given percentiles."""
    if not values:
        return 0, 0
    sv = sorted(values)
    n = len(sv)
    lo = sv[max(0, n * lo_pct // 100 - 1)]
    hi = sv[min(n - 1, n * hi_pct // 100)]
    return lo, hi


def main():
    # data.js の ARTICLES セクションから updatedAt を読み込み
    data_js = (ROOT / "data.js").read_text(encoding="utf-8")
    art_start = data_js.find("const ARTICLES = [")
    art_end = data_js.find("];", art_start)
    art_section = data_js[art_start:art_end] if art_start >= 0 else ""
    updated_by_slug = {}
    for m in re.finditer(
        r'id:\s*"(?P<id>[a-z0-9-]+-2026-\d{2})"[\s\S]*?updatedAt:\s*"(?P<u>[\d-]+)"',
        art_section,
    ):
        updated_by_slug[m.group("id")] = m.group("u")

    # GA4 データを読み込み ( なければ None )
    ga4_path = ROOT / "_ga4_engagement.json"
    ga4_by_slug = {}
    if ga4_path.exists():
        try:
            data = json.loads(ga4_path.read_text(encoding="utf-8"))
            ga4_by_slug = {x["slug"]: x for x in data}
        except Exception:
            pass

    # 閾値 ( 全記事の中央値ベース ) - GA4 がある記事のみで計算
    ga4_records = list(ga4_by_slug.values())
    pv_thr = percentile_thresholds([r["pv"] for r in ga4_records if r.get("pv", 0) > 0])
    eng_thr = percentile_thresholds(
        [r["engagement_seconds_avg"] for r in ga4_records if r.get("engagement_seconds_avg", 0) > 0]
    )

    results = []
    for f in sorted(ART_DIR.glob("*-2026-06.html")):
        if f.name == "index.html":
            continue
        html = f.read_text(encoding="utf-8")
        a = assess(html)

        # 鮮度スコア
        upd = updated_by_slug.get(f.stem)
        fresh_score, days_since = freshness_score(upd)

        # GA4 情報と打ち手分類
        ga4 = ga4_by_slug.get(f.stem, {})
        pv = ga4.get("pv")
        eng_sec = ga4.get("engagement_seconds_avg")
        ptype, plabel, paction = classify_priority(pv, eng_sec, pv_thr, eng_thr)

        # Extract title and id
        title_m = re.search(r"<h1 class=\"article-title\">(.+?)</h1>", html)
        title = title_m.group(1) if title_m else f.stem
        # composite = 構造 + GA4 ( 内部回遊エンゲージメント ) 。鮮度は別管理
        ga4_score = ga4.get("ga4Score", 0)
        results.append({
            "slug": f.stem,
            "title": title,
            "url": f"https://hokkaido-research.lrg.jp/articles/{f.name}",
            "total": a["total"],
            "freshness": fresh_score,
            "days_since_update": days_since,
            "updatedAt": upd or "",
            "composite": a["total"] + ga4_score,  # 鮮度を含めない
            "char_count": a["char_count"],
            "table_count": a["table_count"],
            "breakdown": a["scores"],
            "internal_pv": ga4.get("internal_pv", 0),
            "external_pv": ga4.get("external_pv", 0),
            "engagement_seconds_avg": eng_sec if eng_sec is not None else 0,
            "ga4Score": ga4_score,
            "priorityType": ptype,
            "priorityLabel": plabel,
            "priorityAction": paction,
        })

    # Sort by composite ( weakest first ) - 構造 + 鮮度 の合算で弱い順
    results.sort(key=lambda x: x["composite"])

    # Output
    print(f"Total articles assessed: {len(results)}\n")
    print(f"{'Comp':<5} {'Str':<4} {'GA4':<4} {'Frs':<4} {'Days':<5} {'iPV':<4} {'Type':<6} Slug")
    print("-" * 95)
    for r in results:
        print(
            f"{r['composite']:>3}   {r['total']:>3}  {r['ga4Score']:>3}  "
            f"{r['freshness']:>3}  {r['days_since_update']:>4}  "
            f"{r['internal_pv']:>3}  {r['priorityType']:<5}  {r['slug']}"
        )

    # Save full JSON
    out = ROOT / "_articles_quality.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n→ Saved to {out.relative_to(ROOT)}")

    # Identify weak articles ( 構造 score < 60 )
    weak = [r for r in results if r["total"] < 60]
    print(f"\n構造弱: {len(weak)} 件 ( total < 60 )")
    stale = [r for r in results if r["freshness"] < 6]
    print(f"鮮度低下: {len(stale)} 件 ( freshness < 6 ・ 古さ自体は欠点ではない )")
    # 優先タイプ別の件数
    from collections import Counter
    type_counts = Counter(r["priorityType"] for r in results)
    print("\n優先タイプ別件数:")
    type_order = ["A", "B", "C", "D", "E", "F", "NODATA"]
    for t in type_order:
        if type_counts.get(t):
            label_map = {
                "A": "高エンゲ × 低PV ( 露出+SEO )",
                "B": "低エンゲ × 高PV ( コンテンツ )",
                "C": "中エンゲ × 低PV ( SEO先→コンテンツ )",
                "D": "高エンゲ × 高PV ( 維持 )",
                "E": "低エンゲ × 低PV ( 根本見直し )",
                "F": "中エンゲ × 中/高PV ( コンテンツ )",
                "NODATA": "GA4 データなし ( 構造ベース判定 )",
            }
            print(f"  {t}  {type_counts[t]:>3} 件  {label_map[t]}")


if __name__ == "__main__":
    main()
