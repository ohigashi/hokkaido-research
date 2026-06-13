#!/usr/bin/env python3
"""OG IMAGE を SVG で生成する。

生成物:
1. カテゴリ別 OG IMAGE 8 種 ( /og/category-{cat_id}.svg )
2. 記事個別 OG IMAGE 104 件 ( /og/article-{slug}.svg )
3. 静的ページ用 OG IMAGE ( /og/site.svg / og/articles.svg / og/glossary.svg )

サイズ: 1200x630 ( OG 標準 )
"""
import re
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OG_DIR = ROOT / "og"
OG_DIR.mkdir(exist_ok=True)

# CATEGORIES from data.js
CATEGORIES = [
    {"id": "population",  "name": "人口・世代・暮らし",     "color": "#2C6E63", "label_jp": "人口"},
    {"id": "primary",     "name": "一次産業・食・森林",     "color": "#7A8450", "label_jp": "一次産業"},
    {"id": "regional",    "name": "地域・インフラ・交通",   "color": "#3D6B9E", "label_jp": "地域インフラ"},
    {"id": "medical",     "name": "医療・福祉・ケア",       "color": "#9E5A6B", "label_jp": "医療福祉"},
    {"id": "industry",    "name": "産業・仕事・移住",       "color": "#B5733A", "label_jp": "産業・仕事"},
    {"id": "environment", "name": "環境・エネルギー・防災", "color": "#4F8A6B", "label_jp": "環境"},
    {"id": "tourism",     "name": "観光・交流・共生",       "color": "#6B5B95", "label_jp": "観光・共生"},
    {"id": "digital",     "name": "デジタル・行政",         "color": "#5A7D8C", "label_jp": "デジタル・行政"},
]
CAT_BY_ID = {c["id"]: c for c in CATEGORIES}

# ARTICLE_CATEGORIES ( 編集カテゴリ ・ Article の category 値 → 色 )
ARTICLE_CAT_COLOR = {
    "課題発見": "#B5733A",
    "アイデア": "#2E7CA8",
    "事例": "#6B5B95",
}


def escape_xml(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
              .replace('"', "&quot;").replace("'", "&apos;"))


def wrap_title(title, max_per_line=18, max_lines=3):
    """タイトルを max_per_line 文字で改行。 max_lines を超えたら省略。"""
    # 句読点 / 記号での自然改行を優先
    lines = []
    current = ""
    for ch in title:
        if len(current) >= max_per_line and ch in "・ -ー":
            lines.append(current)
            current = ch
            if len(lines) >= max_lines:
                break
            continue
        current += ch
        if len(current) >= max_per_line + 4:
            # 強制改行
            lines.append(current)
            current = ""
            if len(lines) >= max_lines:
                break
    if current and len(lines) < max_lines:
        lines.append(current)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1][:max_per_line] + "…"
    return lines


SVG_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_color}" stop-opacity="1"/>
      <stop offset="100%" stop-color="{bg_color2}" stop-opacity="1"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="630" fill="url(#bg)"/>
  <rect x="0" y="0" width="1200" height="14" fill="{accent}"/>
  <text x="64" y="120" font-family="Hiragino Kaku Gothic ProN, Hiragino Sans, sans-serif" font-size="28" font-weight="700" fill="#FFFFFF" opacity="0.85">{breadcrumb}</text>
  {category_label}
  <g font-family="Hiragino Kaku Gothic ProN, Hiragino Sans, sans-serif" font-weight="900" fill="#FFFFFF">
    {title_lines}
  </g>
  <text x="64" y="540" font-family="Hiragino Kaku Gothic ProN, Hiragino Sans, sans-serif" font-size="22" font-weight="600" fill="#FFFFFF" opacity="0.7">hokkaido-research.lrg.jp</text>
  <text x="64" y="580" font-family="Hiragino Kaku Gothic ProN, Hiragino Sans, sans-serif" font-size="20" font-weight="500" fill="#FFFFFF" opacity="0.55">北海道・地域課題リサーチ</text>
</svg>
"""


def darken(hex_color, factor=0.7):
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"#{int(r*factor):02X}{int(g*factor):02X}{int(b*factor):02X}"


def render_svg(title, breadcrumb, bg_color, accent="#FFFFFF", category_label_text=None):
    """SVG を生成して返す。"""
    bg_color2 = darken(bg_color, 0.55)
    lines = wrap_title(title, max_per_line=18, max_lines=3)
    n = len(lines)
    # フォントサイズを行数で調整
    if n == 1:
        fs = 92
        start_y = 320
    elif n == 2:
        fs = 80
        start_y = 280
    else:
        fs = 64
        start_y = 250
    title_svg = ""
    line_h = int(fs * 1.25)
    for i, line in enumerate(lines):
        title_svg += f'    <text x="64" y="{start_y + i * line_h}" font-size="{fs}" letter-spacing="-1">{escape_xml(line)}</text>\n'

    category_label = ""
    if category_label_text:
        category_label = (
            f'<rect x="64" y="160" width="{len(category_label_text)*22+40}" height="48" '
            f'fill="#FFFFFF" fill-opacity="0.18" rx="6"/>'
            f'<text x="84" y="194" font-family="Hiragino Kaku Gothic ProN, Hiragino Sans, sans-serif" '
            f'font-size="22" font-weight="700" fill="#FFFFFF">{escape_xml(category_label_text)}</text>'
        )

    return SVG_TEMPLATE.format(
        bg_color=bg_color, bg_color2=bg_color2, accent=accent,
        breadcrumb=escape_xml(breadcrumb),
        category_label=category_label,
        title_lines=title_svg.rstrip(),
    )


def parse_articles_from_generator():
    """generate_articles.py から ARTICLES の id / title / category / relatedIssueIds を取得。"""
    gen_path = ROOT / "_scripts" / "generate_articles.py"
    text = gen_path.read_text(encoding="utf-8")
    # 簡易: "id": "..." と "title": "..." と "category": "..." と "relatedIssueIds": [...] を順に抽出
    art_section_start = text.find("ARTICLES = [")
    if art_section_start < 0:
        return []
    # 最初のエントリブロックは "{ ... }," が複数並ぶ
    # 簡易パターンマッチ
    entries = []
    pat = re.compile(
        r'"id":\s*"(?P<id>[a-z0-9-]+-2026-\d{2})",[\s\S]*?'
        r'"title":\s*"(?P<title>[^"]+)",[\s\S]*?'
        r'"category":\s*"(?P<category>[^"]+)",[\s\S]*?'
        r'"relatedIssueIds":\s*\[(?P<rel>[^\]]*)\]'
    )
    for m in pat.finditer(text[art_section_start:]):
        rel = re.findall(r'"([^"]+)"', m.group("rel"))
        entries.append({
            "id": m.group("id"),
            "title": m.group("title"),
            "category": m.group("category"),
            "relatedIssueIds": rel,
        })
    return entries


def parse_issues_from_data():
    """data.js から ISSUES の id / cat を取得。"""
    data_path = ROOT / "data.js"
    text = data_path.read_text(encoding="utf-8")
    # const ISSUES = [...]
    start = text.find("const ISSUES = [")
    end = text.find("];", start)
    section = text[start:end] if start >= 0 else ""
    issues = {}
    pat = re.compile(
        r'id:\s*"(?P<id>[a-z0-9-]+)",[\s\S]+?cat:\s*"(?P<cat>[^"]+)"'
    )
    for m in pat.finditer(section):
        issues[m.group("id")] = m.group("cat")
    return issues


def main():
    # 1. カテゴリ別 OG ( 8 種 )
    for c in CATEGORIES:
        svg = render_svg(
            title=c["name"],
            breadcrumb="課題分類",
            bg_color=c["color"],
            category_label_text=None,
        )
        out = OG_DIR / f"category-{c['id']}.svg"
        out.write_text(svg, encoding="utf-8")
    print(f"✓ カテゴリ別 OG ・ {len(CATEGORIES)} 件")

    # 2. 静的ページ用 OG
    site_svg = render_svg(
        title="北海道の地域課題を構造から読み解く",
        breadcrumb="hokkaido-research",
        bg_color="#2C6E63",
        accent="#FFFFFF",
    )
    (OG_DIR / "site.svg").write_text(site_svg, encoding="utf-8")
    articles_svg = render_svg(
        title="読み物一覧 ・ 構造分析と長期事例",
        breadcrumb="読み物",
        bg_color="#3A4A52",
    )
    (OG_DIR / "articles.svg").write_text(articles_svg, encoding="utf-8")
    glossary_svg = render_svg(
        title="用語集 ・ 65 専門用語を 16 カテゴリで整理",
        breadcrumb="用語集",
        bg_color="#5A7D8C",
    )
    (OG_DIR / "glossary.svg").write_text(glossary_svg, encoding="utf-8")
    print("✓ 静的ページ用 OG ・ 3 件")

    # 3. 記事個別 OG
    issues_cat = parse_issues_from_data()
    arts = parse_articles_from_generator()
    for a in arts:
        # 関連 ISSUE の cat → CATEGORIES の色を選ぶ
        related = a["relatedIssueIds"]
        cat_id = None
        for iid in related:
            if iid in issues_cat:
                cat_id = issues_cat[iid]
                break
        cat_info = CAT_BY_ID.get(cat_id) if cat_id else None
        if cat_info:
            bg = cat_info["color"]
            label = cat_info["label_jp"]
        else:
            bg = ARTICLE_CAT_COLOR.get(a["category"], "#2C6E63")
            label = a["category"]

        svg = render_svg(
            title=a["title"],
            breadcrumb=a["category"],
            bg_color=bg,
            category_label_text=label,
        )
        out = OG_DIR / f"article-{a['id']}.svg"
        out.write_text(svg, encoding="utf-8")
    print(f"✓ 記事個別 OG ・ {len(arts)} 件")
    print(f"\n→ {OG_DIR.relative_to(ROOT)}/ に合計 {len(CATEGORIES) + 3 + len(arts)} ファイル")


if __name__ == "__main__":
    main()
