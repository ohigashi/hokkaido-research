#!/usr/bin/env python3
"""Inject quality / freshness scores into each ARTICLES entry in data.js.

Fields written:
- quality: 構造スコア ( 0-100 )
- freshness: 鮮度スコア ( 0-15 )
- ga4Score: GA4 エンゲージメントスコア ( 0-25、未連携時は 0 )
- compositeScore: quality + freshness + ga4Score

Use composite for ranking. Keep individual fields for transparency.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data.js"
QUALITY = ROOT / "_articles_quality.json"
GA4 = ROOT / "_ga4_engagement.json"  # Optional

quality_data = json.loads(QUALITY.read_text(encoding="utf-8"))
score_by_slug = {q["slug"]: q for q in quality_data}

ga4_by_slug = {}
if GA4.exists():
    try:
        ga4_by_slug = {x["slug"]: x.get("ga4Score", 0) for x in json.loads(GA4.read_text(encoding="utf-8"))}
        print(f"GA4 scores loaded: {len(ga4_by_slug)}")
    except Exception as e:
        print(f"GA4 load failed: {e}")

content = DATA.read_text(encoding="utf-8")

art_start = content.find("const ARTICLES = [")
art_end = content.find("];", art_start)
art_section = content[art_start:art_end]


def repl(m):
    full = m.group(0)
    aid = m.group("id")
    info = score_by_slug.get(aid, {})
    structure = info.get("total", 0)
    freshness = info.get("freshness", 0)
    ga4 = ga4_by_slug.get(aid, 0)
    composite = structure + freshness + ga4

    # Strip existing score fields
    cleaned = re.sub(r"\s*quality:\s*\d+,", "", full)
    cleaned = re.sub(r"\s*freshness:\s*\d+,", "", cleaned)
    cleaned = re.sub(r"\s*ga4Score:\s*\d+,", "", cleaned)
    cleaned = re.sub(r"\s*compositeScore:\s*\d+,", "", cleaned)

    # Insert score block before the closing "},"
    insertion = (
        f"    quality: {structure},\n"
        f"    freshness: {freshness},\n"
        f"    ga4Score: {ga4},\n"
        f"    compositeScore: {composite},\n"
        f"  }},"
    )
    return re.sub(r"\s*\}\,\s*$", "\n" + insertion + "\n", cleaned)


new_art_section = re.sub(
    r"\{\s*\n\s*id:\s*\"(?P<id>[a-z0-9-]+)\",[\s\S]+?\n\s*\},",
    repl,
    art_section,
)

content = content[:art_start] + new_art_section + content[art_end:]
DATA.write_text(content, encoding="utf-8")

print(f"Quality scores injected: {len(score_by_slug)}")
print("Top 10 by composite:")
ranked = sorted(quality_data, key=lambda x: -(x["total"] + x.get("freshness", 0)))
for q in ranked[:10]:
    print(
        f"  {q['total'] + q.get('freshness', 0):>3}  "
        f"( {q['total']} + {q.get('freshness', 0)} )  {q['slug']}"
    )
