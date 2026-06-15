#!/bin/bash
# hokkaido-research の article HTML をすべて dohokuhub.com/story/{slug}/ への redirect に置換
# 副次的に他の top-level HTML ( glossary / data-sources / internal-archive / privacy / terms ) も
# トップに redirect する

set -e
cd "$(dirname "$0")/.."

DEST_BASE="https://dohokuhub.com"

make_redirect_html() {
  local target=$1
  local slug_text=$2
  cat <<EOF
<!doctype html>
<html lang="ja">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>このページは dohokuhub.com に移動しました</title>
<meta name="robots" content="noindex, follow" />
<link rel="canonical" href="${target}" />
<meta http-equiv="refresh" content="3; url=${target}" />
<style>
  body{font-family:"Noto Sans JP","Hiragino Sans",sans-serif;font-size:15px;line-height:1.85;color:#2a2c30;background:#fff;margin:0}
  .wrap{max-width:640px;margin:0 auto;padding:80px 24px}
  h1{font-family:"Noto Serif JP","Hiragino Mincho ProN",serif;font-size:22px;font-weight:700;border-left:4px solid #7ba37b;padding:6px 0 6px 14px;margin:0 0 18px}
  p{color:#4a4d52;margin:0 0 14px}
  a{color:#1a2a26;border-bottom:1px dotted #7ba37b;text-decoration:none}
  .cta{display:inline-block;margin-top:12px;padding:10px 20px;background:#2a2c30;color:#fff;border-radius:30px;border-bottom:none;font-weight:700;letter-spacing:.04em}
  .cta:hover{background:#1a2a26}
  .brand{font-family:Georgia,serif;font-size:24px;font-weight:700;color:#1a2a26;margin:0 0 6px}
  .brand a{color:inherit;border-bottom:none}
  .kicker{font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#6b6d72;margin:0 0 28px}
</style>
</head>
<body>
  <div class="wrap">
    <p class="brand"><a href="https://dohokuhub.com/">dohokuhub.com</a></p>
    <p class="kicker">INTELLIGENCE ON HOKKAIDO</p>
    <h1>このページは dohokuhub.com に移動しました</h1>
    <p>${slug_text}</p>
    <a class="cta" href="${target}">移動先を開く →</a>
    <p style="margin-top:24px;font-size:12px;color:#9a9da2">3秒後に自動で移動します。</p>
  </div>
  <script>setTimeout(function(){location.replace("${target}")},3000);</script>
</body>
</html>
EOF
}

# Article files → /story/{slug}/
echo "Article redirects:"
for f in articles/*.html; do
  name=$(basename "$f" .html)
  if [[ "$name" == "_article_styles" ]]; then continue; fi
  target="${DEST_BASE}/story/${name}/"
  make_redirect_html "$target" "「${name}」は dohokuhub.com の story 配下に再構成されています。" > "$f"
  echo "  $f → $target"
done

# Top-level pages → トップ系
echo
echo "Top-level redirects:"
for pair in \
  "glossary.html|${DEST_BASE}/|用語集は dohokuhub.com の各記事で個別に解説しています。" \
  "data-sources.html|${DEST_BASE}/data/|データソース一覧は dohokuhub.com/data/ に整理されています。" \
  "internal-archive.html|${DEST_BASE}/|内部アーカイブは公開ページに統合されました。" \
  "privacy.html|${DEST_BASE}/privacy/|プライバシーポリシーは dohokuhub.com に移動しました。" \
  "terms.html|${DEST_BASE}/terms/|利用規約は dohokuhub.com に移動しました。" \
  "404.html|${DEST_BASE}/|お探しのページは dohokuhub.com に統合されました。"; do
  IFS='|' read -r src target msg <<< "$pair"
  if [[ -f "$src" ]]; then
    make_redirect_html "$target" "$msg" > "$src"
    echo "  $src → $target"
  fi
done

echo
echo "Done."
