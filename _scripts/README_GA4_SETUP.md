# GA4 連携セットアップ手順

hokkaido-research 記事の品質スコアに GA4 エンゲージメントを取り込むための初期設定。

## 1. GA4 プロパティ ID を確認

GA4 管理画面 → 管理 → プロパティ設定 → プロパティ ID ( 9 桁の数値 )。

## 2. Google Cloud プロジェクトで service account を作成

1. https://console.cloud.google.com/ にログイン ( ohigashi@gmail.com )
2. 新規プロジェクト or 既存プロジェクトを選択 ( 例: largo-analytics )
3. メニュー → 「IAM と管理」 → 「サービス アカウント」 → 「サービス アカウントを作成」
   - 名前: `hokkaido-research-ga4`
   - 説明: `GA4 Data API 読み取り専用`
   - 役割は付与不要 ( プロジェクト権限不要 )
4. 作成後、サービスアカウント名をクリック → 「キー」タブ → 「鍵を追加」 → 「新しい鍵を作成」 → JSON
5. ダウンロードされた JSON を `_secrets/ga4-service-account.json` に配置 ( このリポジトリ直下に `_secrets/` を作る、 .gitignore 済み )

## 3. GA4 プロパティに service account を追加

1. GA4 → 管理 → プロパティアクセス管理 → 右上「+」
2. メールアドレス欄: service account のメール ( `xxx@<project>.iam.gserviceaccount.com` 形式、JSON 内 `client_email` )
3. 標準のロールから「閲覧者」を選択 → 追加

## 4. GA4 Data API を有効化

1. Google Cloud Console → 「API とサービス」 → 「ライブラリ」
2. 「Google Analytics Data API」を検索 → 「有効にする」
3. 同プロジェクトに対して有効化

## 5. プロパティ ID 設定

以下のいずれか:
- 環境変数: `export GA4_PROPERTY_ID=123456789`
- `_secrets/ga4-config.json`:
  ```json
  {"property_id": "123456789"}
  ```

## 6. Python ライブラリインストール

```bash
pip install google-analytics-data
```

## 7. 取得テスト

```bash
python3 _scripts/fetch_ga4_engagement.py
```

成功すると `_ga4_engagement.json` が生成され、 ga4Score 上位 10 件が表示される。

## 8. 品質スコアに統合

```bash
python3 _scripts/quality_assessment.py
python3 _scripts/inject_quality_score.py
python3 _scripts/generate_articles.py
```

これで data.js の各 ARTICLES に `ga4Score` が注入され、 TOP / 関連記事の合成スコアに反映される。

## 9. 週次自動化 ( オプション )

`_scripts/refresh_quality.sh` ( 後日作成 ) として:

```bash
#!/bin/bash
cd "$(dirname "$0")/.."
python3 _scripts/fetch_ga4_engagement.py
python3 _scripts/quality_assessment.py
python3 _scripts/inject_quality_score.py
python3 _scripts/generate_articles.py
git add data.js articles/ sitemap.xml _articles_quality.json _ga4_engagement.json
git commit -m "Weekly quality refresh ( GA4 + freshness )"
git push origin main
```

cron 例: 毎週月曜 11:00 ( 強化ルーチン適用後 )
```
0 11 * * 1 cd /path/to/hokkaido-research && _scripts/refresh_quality.sh
```

## トラブルシュート

- `Permission denied`: GA4 プロパティアクセス管理で service account のメールが「閲覧者」以上で追加されているか確認
- `API has not been used`: Google Analytics Data API が同プロジェクトで有効化されているか確認
- `No data`: 過去 28 日間にデータがない or pagePath フィルタが効きすぎ。期間や条件を緩める
