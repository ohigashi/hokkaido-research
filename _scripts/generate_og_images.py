#!/usr/bin/env python3
"""OG IMAGE を PNG で生成する ( 文字化け対策で SVG ではなく PNG ) 。

生成物:
1. カテゴリ別 OG IMAGE 8 種 ( /og/category-{cat_id}.png )
2. 記事個別 OG IMAGE 104 件 ( /og/article-{slug}.png )
3. 静的ページ用 OG IMAGE ( /og/site.png / og/articles.png / og/glossary.png )

サイズ: 1200x630 ( OG 標準 )
フォント: ヒラギノ角ゴシック ( システム ・ macOS )
"""
import re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OG_DIR = ROOT / "og"
OG_DIR.mkdir(exist_ok=True)

# フォント
FONT_HEAVY = "/System/Library/Fonts/ヒラギノ角ゴシック W8.ttc"
FONT_BOLD = "/System/Library/Fonts/ヒラギノ角ゴシック W7.ttc"
FONT_MEDIUM = "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc"

# CATEGORIES
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

ARTICLE_CAT_COLOR = {
    "課題発見": "#B5733A",
    "アイデア": "#2E7CA8",
    "事例": "#6B5B95",
}


def hex_to_rgb(h):
    h = h.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def darken(rgb, factor=0.55):
    return tuple(int(c * factor) for c in rgb)


def make_gradient(size, top_rgb, bottom_rgb):
    """斜めグラデーション ( 左上 → 右下 ) を作る。RGBA で返す。"""
    w, h = size
    base = Image.new("RGB", size, top_rgb)
    overlay = Image.new("L", size, 0)
    px = overlay.load()
    diag = w + h
    for y in range(h):
        for x in range(w):
            t = (x + y) / diag
            px[x, y] = int(t * 255)
    bottom_img = Image.new("RGB", size, bottom_rgb)
    base = Image.composite(bottom_img, base, overlay)
    return base.convert("RGBA")


def wrap_text(text, font, max_width, draw):
    """draw.textbbox で 1 行ずつ計測しながら折り返し。"""
    lines = []
    line = ""
    for ch in text:
        candidate = line + ch
        bbox = draw.textbbox((0, 0), candidate, font=font)
        if bbox[2] - bbox[0] > max_width and line:
            lines.append(line)
            line = ch
        else:
            line = candidate
    if line:
        lines.append(line)
    return lines


def render_og(title, breadcrumb, bg_hex, category_label_text=None, out_path=None):
    W, H = 1200, 630
    bg_rgb = hex_to_rgb(bg_hex)
    bottom_rgb = darken(bg_rgb, 0.55)
    img = make_gradient((W, H), bg_rgb, bottom_rgb)
    draw = ImageDraw.Draw(img, "RGBA")

    # 上部アクセント線
    draw.rectangle([(0, 0), (W, 14)], fill=(255, 255, 255, 255))

    # breadcrumb ( 上部 )
    breadcrumb_font = ImageFont.truetype(FONT_BOLD, 30)
    draw.text((64, 70), breadcrumb, font=breadcrumb_font, fill=(255, 255, 255, 220))

    # カテゴリラベル ( pill 型 ・ 暗色背景 + 白文字 )
    next_y = 130
    if category_label_text:
        label_font = ImageFont.truetype(FONT_BOLD, 26)
        bbox = draw.textbbox((0, 0), category_label_text, font=label_font)
        pad_x, pad_y = 18, 10
        label_w = bbox[2] - bbox[0] + pad_x * 2
        label_h = bbox[3] - bbox[1] + pad_y * 2
        # 暗色オーバーレイで pill ・ 白文字を確実に視認
        draw.rounded_rectangle(
            [(64, next_y), (64 + label_w, next_y + label_h)],
            radius=8, fill=(0, 0, 0, 90),
        )
        draw.text((64 + pad_x, next_y + pad_y - 4), category_label_text,
                  font=label_font, fill=(255, 255, 255, 255))
        next_y += label_h + 30
    else:
        next_y = 180

    # タイトル本体 ・ 折り返し
    # フォントサイズを適応
    max_w = W - 128
    for fs in (88, 78, 68, 58, 50):
        font = ImageFont.truetype(FONT_HEAVY, fs)
        lines = wrap_text(title, font, max_w, draw)
        # 3 行以内なら採用
        if len(lines) <= 3:
            break
    if len(lines) > 3:
        lines = lines[:3]
        lines[-1] = lines[-1][:-1] + "…"

    # タイトル描画
    line_h = int(fs * 1.22)
    title_block_h = line_h * len(lines)
    title_start = max(next_y + 20, 320 - title_block_h // 2)
    for i, line in enumerate(lines):
        draw.text((64, title_start + i * line_h), line, font=font, fill="white")

    # フッター ( URL + サイト名 )
    foot_url = ImageFont.truetype(FONT_BOLD, 24)
    foot_site = ImageFont.truetype(FONT_MEDIUM, 22)
    draw.text((64, 528), "hokkaido-research.lrg.jp", font=foot_url,
              fill=(255, 255, 255, 200))
    draw.text((64, 568), "北海道・地域課題リサーチ", font=foot_site,
              fill=(255, 255, 255, 160))

    img.convert("RGB").save(out_path, "PNG", optimize=True)


def parse_articles_from_generator():
    gen_path = ROOT / "_scripts" / "generate_articles.py"
    text = gen_path.read_text(encoding="utf-8")
    art_start = text.find("ARTICLES = [")
    if art_start < 0:
        return []
    entries = []
    pat = re.compile(
        r'"id":\s*"(?P<id>[a-z0-9-]+-2026-\d{2})",[\s\S]*?'
        r'"title":\s*"(?P<title>[^"]+)",[\s\S]*?'
        r'"category":\s*"(?P<category>[^"]+)",[\s\S]*?'
        r'"relatedIssueIds":\s*\[(?P<rel>[^\]]*)\]'
    )
    for m in pat.finditer(text[art_start:]):
        rel = re.findall(r'"([^"]+)"', m.group("rel"))
        entries.append({
            "id": m.group("id"),
            "title": m.group("title"),
            "category": m.group("category"),
            "relatedIssueIds": rel,
        })
    return entries


def parse_issues_from_data():
    data_path = ROOT / "data.js"
    text = data_path.read_text(encoding="utf-8")
    start = text.find("const ISSUES = [")
    end = text.find("];", start)
    section = text[start:end] if start >= 0 else ""
    issues = {}
    pat = re.compile(r'id:\s*"(?P<id>[a-z0-9-]+)",[\s\S]+?cat:\s*"(?P<cat>[^"]+)"')
    for m in pat.finditer(section):
        issues[m.group("id")] = m.group("cat")
    return issues


def main():
    # 1. カテゴリ別 OG
    for c in CATEGORIES:
        out = OG_DIR / f"category-{c['id']}.png"
        render_og(c["name"], "課題分類", c["color"], None, out)
    print(f"✓ カテゴリ別 OG ・ {len(CATEGORIES)} 件")

    # 2. 静的ページ用
    render_og("北海道の地域課題を構造から読み解く", "hokkaido-research",
              "#2C6E63", None, OG_DIR / "site.png")
    render_og("読み物一覧・構造分析と長期事例", "読み物",
              "#3A4A52", None, OG_DIR / "articles.png")
    render_og("用語集・65 専門用語を 16 カテゴリで整理", "用語集",
              "#5A7D8C", None, OG_DIR / "glossary.png")
    print("✓ 静的ページ用 OG ・ 3 件")

    # 3. 記事個別 OG
    issues_cat = parse_issues_from_data()
    arts = parse_articles_from_generator()
    for a in arts:
        cat_id = None
        for iid in a["relatedIssueIds"]:
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
        out = OG_DIR / f"article-{a['id']}.png"
        render_og(a["title"], a["category"], bg, label, out)
    print(f"✓ 記事個別 OG ・ {len(arts)} 件")

    # 4. 既存 SVG を削除
    for svg in OG_DIR.glob("*.svg"):
        svg.unlink()
    print("✓ 旧 SVG 削除")
    print(f"\n→ {OG_DIR.relative_to(ROOT)}/ に PNG {len(CATEGORIES) + 3 + len(arts)} 件")


if __name__ == "__main__":
    main()
