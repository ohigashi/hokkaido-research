#!/usr/bin/env python3
"""新スペースルール ( 過剰半角スペース禁止 ) で全文書を一括修正。

ルール:
- 数字 + 日本語単位の間のスペース除去 ( "498 万人" → "498万人" )
- 中黒「 ・ 」のスペース除去 ( "事業 ・ 関係 ・ 仕組み" → "事業・関係・仕組み" )
- 半角括弧の内側スペース除去 ( "( hello )" → "(hello)" )
- 英単語と日本語の境界スペースは維持 ( "JR 北海道", "Chartbeat の" は崩さない )
- 算術記号 ( → = + - ) と数字の間のスペースは維持
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 単位リスト ( 数字直後に続く可能性のあるもの )
UNITS = [
    "年", "ヶ月", "ヵ月", "ヵ年", "年度", "月", "日", "時", "分", "秒", "週",
    "時間", "世紀", "年代", "年間", "ヶ所", "ヵ所", "箇所", "ケ所",
    "人", "名", "戸", "世帯", "家族", "本", "冊", "社", "件", "個", "種",
    "位", "頭", "羽", "匹", "歳", "台", "軒", "店", "棟", "両", "回",
    "円", "万", "億", "兆", "千", "百", "度", "周年", "段階",
    "割", "%", "％", "ポイント", "倍", "枚",
    "kg", "km", "cm", "mm", "m", "t", "GW", "MW", "kW", "kWh", "MWh",
    "ha", "L", "ml", "ｍ", "ｋｍ", "ｋｇ",
    "つ", "つ目", "箇所目", "段", "層", "重", "次",
]
# 正規表現用に escape して |
UNITS_RE = "|".join(re.escape(u) for u in sorted(UNITS, key=len, reverse=True))

# 置換ルール ( 順序が重要、 上から順に適用 )
RULES = [
    # 1. 中黒のスペース除去 ( 「 ・ 」 → 「・」 )
    (re.compile(r"\s*・\s*"), "・"),
    # 2. 数字 + 半角スペース + 日本語単位 → 数字 + 日本語単位
    #    ( 例: "498 万人" → "498万人", "5 分" → "5分", "3 つ" → "3つ" )
    (re.compile(r"(\d(?:[\d,\.]*\d)?) +(" + UNITS_RE + r")"), r"\1\2"),
    # 3. 半角括弧の内側余分スペース ( 「( hello )」→「(hello)」 ・ ただし英単語の境界は維持 )
    #    ここは保留: 「( 数値 )」のような表記が多く、 そのままにする
    # 4. 全角括弧内の余分スペース ( 「（ hello ）」→「（hello）」 )
    (re.compile(r"（\s+"), "（"),
    (re.compile(r"\s+）"), "）"),
    # 5. 句点・読点後の余分スペース ( 「。 」「、 」 内側スペースのみ )
    (re.compile(r"。 +"), "。"),
    (re.compile(r"、 +"), "、"),
]


def normalize(text: str) -> str:
    """新ルールで text を整形して返す。"""
    out = text
    for pat, rep in RULES:
        out = pat.sub(rep, out)
    return out


def process_text_file(path: Path) -> int:
    """テキストファイルを変換 ・ 変更行数を返す。"""
    if not path.exists():
        return 0
    src = path.read_text(encoding="utf-8")
    dst = normalize(src)
    if src == dst:
        return 0
    path.write_text(dst, encoding="utf-8")
    # 簡易: 行数差ではなく 行単位で diff
    src_lines = src.splitlines()
    dst_lines = dst.splitlines()
    changed = sum(1 for a, b in zip(src_lines, dst_lines) if a != b)
    return changed


TARGETS = [
    ROOT / "data.js",
    ROOT / "_scripts/generate_articles.py",
    ROOT / "index.html",
    ROOT / "articles/index.html",
    ROOT / "articles/_article_styles.css",
    ROOT / "glossary.html",
    ROOT / "robots.txt",
    ROOT / "404.html",
]
# _docs/*.md
for f in (ROOT / "_docs").glob("*.md"):
    TARGETS.append(f)


total = 0
for path in TARGETS:
    if not path.exists():
        continue
    changed = process_text_file(path)
    if changed:
        print(f"  {changed:>4} 行  {path.relative_to(ROOT)}")
        total += changed

print(f"\n計 {total} 行を新スペースルールに修正")
print("→ 次に generate_articles.py を実行して articles/ を再生成")
