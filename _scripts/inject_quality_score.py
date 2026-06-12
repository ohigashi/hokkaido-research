#!/usr/bin/env python3
"""Inject quality score into each ARTICLES entry in data.js."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data.js"
QUALITY = ROOT / "_articles_quality.json"

quality_data = json.loads(QUALITY.read_text(encoding="utf-8"))
score_by_slug = {q["slug"]: q["total"] for q in quality_data}

content = DATA.read_text(encoding="utf-8")

# Match each ARTICLES entry block in data.js (looking only inside ARTICLES section)
art_start = content.find("const ARTICLES = [")
art_end = content.find("];", art_start)
art_section = content[art_start:art_end]

# Pattern matches one article entry; capture id and find a stable insertion point
def repl(m):
    full = m.group(0)
    aid = m.group("id")
    if "quality:" in full:
        return full  # already has quality
    score = score_by_slug.get(aid, 0)
    # Insert quality field before the closing "}," of this object
    # Specifically, before the line ending with "  }," at end of block
    if full.rstrip().endswith("},"):
        # remove trailing "  },"
        insertion = f"    quality: {score},\n  }},"
        return re.sub(r"\s*\}\,\s*$", "\n" + insertion + "\n", full)
    return full

new_art_section = re.sub(
    r"\{\s*\n\s*id:\s*\"(?P<id>[a-z0-9-]+)\",[\s\S]+?\n\s*\},",
    repl,
    art_section,
)

content = content[:art_start] + new_art_section + content[art_end:]
DATA.write_text(content, encoding="utf-8")

# Stats
print(f"Quality scores available: {len(score_by_slug)}")
print(f"Top 10 by quality:")
for q in sorted(quality_data, key=lambda x: -x["total"])[:10]:
    print(f"  {q['total']:>3}  {q['slug']}")
