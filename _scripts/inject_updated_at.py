#!/usr/bin/env python3
"""Inject updatedAt field into each ARTICLES entry in data.js.

Strategy:
- If entry already has updatedAt: keep as-is
- Else: set updatedAt = publishedAt as initial value

Also writes a helper to be called when an article is enhanced:
  python3 _scripts/inject_updated_at.py --stamp <slug>
sets updatedAt = today for that slug.
"""
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data.js"


def bulk_initialize():
    content = DATA.read_text(encoding="utf-8")
    art_start = content.find("const ARTICLES = [")
    art_end = content.find("];", art_start)
    art_section = content[art_start:art_end]

    pattern = re.compile(
        r"(?P<head>\{\s*\n\s*id:\s*\"(?P<id>[a-z0-9-]+)\",[\s\S]+?publishedAt:\s*\"(?P<pub>[\d-]+)\",)"
    )

    updated_count = 0

    def repl(m):
        nonlocal updated_count
        # Search the full block for existing updatedAt
        full_block = m.group(0)
        # We only see up to publishedAt here - check the whole remaining article block
        # Insert updatedAt right after publishedAt if not present in entire ARTICLES section later
        return m.group(0) + f"\n    updatedAt: \"{m.group('pub')}\","

    # We need block-level processing. Use a wider regex matching the full entry.
    entry_re = re.compile(
        r"\{\s*\n\s*id:\s*\"(?P<id>[a-z0-9-]+)\",[\s\S]+?\n\s*\},"
    )

    def process_entry(m):
        nonlocal updated_count
        full = m.group(0)
        if "updatedAt:" in full:
            return full
        pub_m = re.search(r"publishedAt:\s*\"([\d-]+)\",", full)
        if not pub_m:
            return full
        pub = pub_m.group(1)
        # Insert updatedAt immediately after the publishedAt line
        new_full = full.replace(
            f"publishedAt: \"{pub}\",",
            f"publishedAt: \"{pub}\",\n    updatedAt: \"{pub}\",",
            1,
        )
        updated_count += 1
        return new_full

    new_section = entry_re.sub(process_entry, art_section)
    content = content[:art_start] + new_section + content[art_end:]
    DATA.write_text(content, encoding="utf-8")
    print(f"updatedAt フィールドを {updated_count} 件の ARTICLES に注入完了")


def stamp_slug(slug: str):
    """Update specific slug's updatedAt to today."""
    content = DATA.read_text(encoding="utf-8")
    today = date.today().isoformat()
    pattern = re.compile(
        r"(id:\s*\"" + re.escape(slug) + r"\",[\s\S]*?updatedAt:\s*\")[\d-]+(\",)"
    )
    new_content, n = pattern.subn(rf"\g<1>{today}\g<2>", content)
    if n == 0:
        print(f"slug '{slug}' not found or updatedAt missing", file=sys.stderr)
        sys.exit(1)
    DATA.write_text(new_content, encoding="utf-8")
    print(f"{slug} の updatedAt を {today} に更新")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--stamp":
        stamp_slug(sys.argv[2])
    else:
        bulk_initialize()
