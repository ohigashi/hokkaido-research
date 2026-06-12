#!/usr/bin/env python3
"""Bulk text spacing cleanup across content files.

Rules:
1. Remove space around 中黒 ( ・ ): " ・ " → "・"
2. Remove space between number and Japanese counter
   ( "1 兆円" → "1兆円"、"4 分" → "4分" 等 )

Keeps space around English alphabet ( "JR 北海道", "GCF を活用" ).
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

# Files to process
TARGETS = [
    ROOT / "data.js",
    ROOT / "index.html",
    ROOT / "glossary.html",
    ROOT / "terms.html",
    ROOT / "privacy.html",
    ROOT / "_scripts" / "generate_articles.py",
    ROOT / "articles" / "index.html",
]

# Japanese counters that immediately follow a number
COUNTERS = "|".join([
    # Basic units
    "兆", "億", "万", "千", "百",
    # Quantities
    "円", "人", "戸", "本", "社", "件", "個", "種", "章", "位", "頭", "名", "歳", "台", "軒", "枚", "回", "倍", "層",
    # Time
    "分", "秒", "時", "日", "月", "年", "週", "世紀", "時間",
    # Distance/area
    "ヶ所", "ヵ所", "箇所",
    # Common percentages and ranges
    "%",
])

NUM_COUNTER_RE = re.compile(r"(\d) (" + COUNTERS + ")")
COUNTER_NUM_RE = re.compile(r"(" + COUNTERS + ") (\d)")  # "年 6月" → "年6月"


def fix_text(content: str) -> tuple[str, int, int]:
    n_nakaguro = 0
    n_counter = 0

    # 1. " ・ " → "・"
    new_content, n_nakaguro = re.subn(r" ・ ", "・", content)

    # 2. number + space + Japanese counter ( "1 兆円" → "1兆円" )
    def repl(m):
        return m.group(1) + m.group(2)
    new_content, n_counter = NUM_COUNTER_RE.subn(repl, new_content)

    # 3. counter + space + number ( "年 6月" → "年6月" ) - second pass
    new_content, n_more = COUNTER_NUM_RE.subn(repl, new_content)
    n_counter += n_more

    return new_content, n_nakaguro, n_counter


def main():
    total_n = 0
    total_c = 0
    for f in TARGETS:
        if not f.exists():
            print(f"SKIP (not exists): {f.relative_to(ROOT)}")
            continue
        content = f.read_text(encoding="utf-8")
        new_content, n_n, n_c = fix_text(content)
        if new_content != content:
            f.write_text(new_content, encoding="utf-8")
            print(f"  {f.relative_to(ROOT)}: 中黒 {n_n}, 数字 {n_c}")
            total_n += n_n
            total_c += n_c
        else:
            print(f"  {f.relative_to(ROOT)}: no change")

    print(f"\nTotal: 中黒 {total_n} 件 ・ 数字カウンタ {total_c} 件")


if __name__ == "__main__":
    main()
