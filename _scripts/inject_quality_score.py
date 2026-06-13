#!/usr/bin/env python3
"""Inject quality / ga4Score / priorityType into each ARTICLES entry in data.js.

Fields written:
- quality: 構造スコア ( 0-100 )
- freshness: 鮮度スコア ( 0-15 、参考情報のみ。 composite には加算しない )
- ga4Score: GA4 エンゲージメントスコア ( 0-25 、内部回遊 PV × エンゲ時間ベース )
- compositeScore: quality + ga4Score ( 鮮度は含めない 、 TOP / 関連記事の並び順に使用 )
- priorityType: A / B / C / D / E / F / NODATA ( 強化施策の判定に使う )
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data.js"
QUALITY = ROOT / "_articles_quality.json"

quality_data = json.loads(QUALITY.read_text(encoding="utf-8"))
info_by_slug = {q["slug"]: q for q in quality_data}

content = DATA.read_text(encoding="utf-8")

art_start = content.find("const ARTICLES = [")
art_end = content.find("];", art_start)
art_section = content[art_start:art_end]


def repl(m):
    full = m.group(0)
    aid = m.group("id")
    info = info_by_slug.get(aid, {})
    structure = info.get("total", 0)
    freshness = info.get("freshness", 0)
    ga4 = info.get("ga4Score", 0)
    ptype = info.get("priorityType", "NODATA")
    gsrc = info.get("ga4Source", "estimated")
    composite = structure + ga4  # 鮮度は含めない

    # Strip existing score fields
    cleaned = re.sub(r"\s*quality:\s*\d+,", "", full)
    cleaned = re.sub(r"\s*freshness:\s*\d+,", "", cleaned)
    cleaned = re.sub(r"\s*ga4Score:\s*\d+,", "", cleaned)
    cleaned = re.sub(r"\s*compositeScore:\s*\d+,", "", cleaned)
    cleaned = re.sub(r"\s*priorityType:\s*\"[A-Z_]+\",", "", cleaned)
    cleaned = re.sub(r"\s*ga4Source:\s*\"[a-z]+\",", "", cleaned)

    insertion = (
        f"    quality: {structure},\n"
        f"    freshness: {freshness},\n"
        f"    ga4Score: {ga4},\n"
        f"    compositeScore: {composite},\n"
        f"    priorityType: \"{ptype}\",\n"
        f"    ga4Source: \"{gsrc}\",\n"
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

print(f"スコア注入完了: {len(info_by_slug)} 件")
print("\nTOP / 関連記事の並び順に使う composite ( quality + ga4Score ) Top 10:")
ranked = sorted(quality_data, key=lambda x: -(x["total"] + x.get("ga4Score", 0)))
for q in ranked[:10]:
    print(
        f"  {q['total'] + q.get('ga4Score', 0):>3}  "
        f"( q={q['total']} g={q.get('ga4Score', 0)} )  "
        f"[{q.get('priorityType', '?')}]  {q['slug']}"
    )
