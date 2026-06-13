#!/bin/bash
# hokkaido-research 品質スコア更新サイクル
#
# 実行: _scripts/refresh_quality.sh        ( push まで )
#       _scripts/refresh_quality.sh --no-push  ( ローカル更新のみ )
#
# フロー:
# 1. GA4 から engagement を取得 ( 失敗しても継続、既存 _ga4_engagement.json を使う )
# 2. quality_assessment.py で構造 + 鮮度を採点
# 3. inject_quality_score.py で data.js に注入
# 4. generate_articles.py で全記事 HTML を再生成
# 5. 差分があれば git add / commit / push

set -e
cd "$(dirname "$0")/.."

PUSH=true
[ "$1" = "--no-push" ] && PUSH=false

echo "=== Step 1: GA4 engagement 取得 ==="
if python3 _scripts/fetch_ga4_engagement.py 2>/tmp/ga4_err; then
  echo "✓ GA4 取得成功"
else
  echo "⚠ GA4 取得失敗 ( 既存 _ga4_engagement.json を継続使用 )"
  echo "  詳細: $(tail -3 /tmp/ga4_err)"
fi

echo
echo "=== Step 2: 品質採点 ==="
python3 _scripts/quality_assessment.py > /tmp/qa_log
tail -3 /tmp/qa_log

echo
echo "=== Step 3: data.js にスコア注入 ==="
python3 _scripts/inject_quality_score.py | tail -12

echo
echo "=== Step 4: 記事 HTML 再生成 ==="
python3 _scripts/generate_articles.py | tail -3

echo
echo "=== Step 5: git 差分 ==="
CHANGES=$(git status --porcelain | wc -l | tr -d ' ')
if [ "$CHANGES" = "0" ]; then
  echo "差分なし - commit/push 不要"
  exit 0
fi

echo "$CHANGES 件の変更あり"
git status --porcelain | head -10

if [ "$PUSH" = false ]; then
  echo
  echo "→ --no-push 指定。手動で git commit/push してください。"
  exit 0
fi

NOW=$(date +"%Y-%m-%d %H:%M")
git add -A
git commit -m "Weekly quality refresh ( ${NOW} )

GA4 engagement / freshness / quality を再計算し data.js + 記事 HTML を更新。
TOP / 関連記事の選定が最新スコアで再ランクされる。"
git push origin main 2>&1 | tail -3

echo
echo "✓ 完了"
