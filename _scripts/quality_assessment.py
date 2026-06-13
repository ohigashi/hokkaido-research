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

    results = []
    for f in sorted(ART_DIR.glob("*-2026-06.html")):
        if f.name == "index.html":
            continue
        html = f.read_text(encoding="utf-8")
        a = assess(html)

        # 鮮度スコア
        upd = updated_by_slug.get(f.stem)
        fresh_score, days_since = freshness_score(upd)

        # Extract title and id
        title_m = re.search(r"<h1 class=\"article-title\">(.+?)</h1>", html)
        title = title_m.group(1) if title_m else f.stem
        results.append({
            "slug": f.stem,
            "title": title,
            "url": f"https://hokkaido-research.lrg.jp/articles/{f.name}",
            "total": a["total"],
            "freshness": fresh_score,
            "days_since_update": days_since,
            "updatedAt": upd or "",
            "composite": a["total"] + fresh_score,
            "char_count": a["char_count"],
            "table_count": a["table_count"],
            "breakdown": a["scores"],
        })

    # Sort by composite ( weakest first ) - 構造 + 鮮度 の合算で弱い順
    results.sort(key=lambda x: x["composite"])

    # Output
    print(f"Total articles assessed: {len(results)}\n")
    print(f"{'Comp':<5} {'Str':<4} {'Frs':<4} {'Days':<5} {'Chars':<6} {'Tbls':<5} Slug")
    print("-" * 80)
    for r in results:
        print(
            f"{r['composite']:>3}   {r['total']:>3}  {r['freshness']:>3}  "
            f"{r['days_since_update']:>4}  {r['char_count']:>5}  {r['table_count']:>2}    {r['slug']}"
        )

    # Save full JSON
    out = ROOT / "_articles_quality.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n→ Saved to {out.relative_to(ROOT)}")

    # Identify weak articles ( 構造 score < 60 )
    weak = [r for r in results if r["total"] < 60]
    print(f"\n構造弱: {len(weak)} 件 ( total < 60 )")
    stale = [r for r in results if r["freshness"] < 6]
    print(f"鮮度低下: {len(stale)} 件 ( freshness < 6 )")


if __name__ == "__main__":
    main()
