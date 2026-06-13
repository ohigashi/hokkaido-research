# hokkaido-research 機能追加・改修ログ

公開日: 2026-06-12
URL: https://hokkaido-research.lrg.jp/
記録: ローンチから集中改修期 ( 2026-06-12 → 2026-06-13 ) までの累積変更

---

## Phase 1 : ローンチ + コンテンツ基盤 ( 2026-06-12 )

### 1.1 ローンチ

- GitHub Pages 公開 + Cloudflare DNS で `hokkaido-research.lrg.jp` 公開
- 8つの課題分類 ( 人口・一次産業・地域 / インフラ・医療・産業・環境・観光・デジタル ) で 20 課題
- 構造分析 + 道内 / 道外取組事例の整理プラットフォームとして稼働

### 1.2 読み物機能

- `/articles/` 一覧ページ作成
- 課題と独立した「読み物」セクションを TOP に追加
- 既存 5 記事を完訳版で生成・後継記事 7本投入
- 「アイデア」「課題発見」「事例」の編集カテゴリ分け

### 1.3 ISSUE 拡張 ( 6/12 集中 )

- 「フードロス・廃棄物・食料自給」テーマ追加・関連記事
- 「子どもの貧困・教育格差」テーマ追加・構造分析記事
- 残り 5 記事を「議論メモ」と同等の深掘り型に書き直し
- ISSUE 数: 20 → 43 → 66件に拡張

### 1.4 「わたしたちにできること」横展開

- 既存 6 記事 + 全 ISSUE モーダルに「個人 / 企業組織」の行動変容セクション
- 行動変容を 3段ジャーニーの第 3段として明示化

---

## Phase 2 : 編集基盤・SEO・UX ( 2026-06-12 → 6-13 )

### 2.1 用語集 ( /glossary.html )

- 24 用語で初期化 → 16 カテゴリ × 65 用語へ拡張
- 記事本文中の専門用語を初出のみ自動でリンク化 ( link_glossary_terms )

### 2.2 表記統一

- 文章は半角英数字・半角スペース・機種依存文字 NG
- 中黒・数字+カウンタ周辺のスペース統一 ( fix_spacing.py で 2,781 中黒 + 700 数字カウンタを一括修正 )
- 大東個人名アピール NG → 「運営者」表記に統一

### 2.3 SEO 強化

- JSON-LD ( Article + BreadcrumbList )
- sitemap.xml 自動生成 ( 109 URL )
- robots.txt
- canonical / OG / Twitter Card / article:published_time + article:modified_time
- 記事ページの GA タグを TOP と同じ G-45HHCDR0LB に統一
- フィルタ・関連記事・TOC・パンくず・rel-articles 等で内部リンク強化

### 2.4 TOP / 課題カードのデザイン refresh

- ヒーロー再構成 ( 19px section titles・info-stats-bar に 読み物 N 件 + 課題 N 件 )
- フィルタ ( 課題分類 / キーワード / 地域 / 地域特性 + 新着切替 + ブックマーク )
- 主観指標 ( urgency / severity ) 撤去 → 取組数・外部事例数・深掘り数・鮮度の客観指標へ
- 気になる アイコン: ハート → クリップ ( 📎 )

---

## Phase 3 : 情報源連携 ( 2026-06-12 )

### 3.1 Notion DB「hokkaido-research 情報ソース監視・リリース DB」

- PR TIMES + tanoshimo.jp の週次監視
- 「道内課題取材」「道外解決策参考」「道内取組事例」「道外取組事例」の 4 区分で分類
- 大東のレビューを経て data.js の ISSUE・記事に反映するワークフロー

### 3.2 RemoteTrigger ルーチン

- 月曜 09:00 JST : 情報ソース監視・PR TIMES + tanoshimo.jp 巡回
- 自動投入 → 大東がレビュー

---

## Phase 4 : 品質強化サイクル ( 2026-06-13 )

### 4.1 品質スコア体系

- `_scripts/quality_assessment.py` で全記事を 8 軸で採点 ( length / tables / specific_data / case_detail / sources / habits / central / assets・構造スコア 0-100 )
- `_articles_quality.json` に保存

### 4.2 Notion DB「hokkaido-research 記事品質強化キュー」

- 弱い記事・強い記事・ステール記事を分類して強化ドラフトを蓄積

### 4.3 RemoteTrigger ルーチン

- 月曜 10:00 JST : 記事品質強化サイクル
- 弱 6 + 強 2 + ステール 2 の 10件を自動選定 → ドラフト → Notion DB

### 4.4 編集方針メモリ化

- **情報ソース戦略**: 課題抽出は道内重視 / 解決策は道内外を広く参照
- **質の定義**: 内部回遊でよく読まれて、エンゲージメントも強い記事 = 質が高い ( 外部バズの PV は質の指標にしない )
- **鮮度 ≠ 品質**: 古くてもエンゲが強ければ高評価
- **マトリクス打ち手**: A 露出+SEO / B コンテンツ / C SEO 先 / D 維持 / E 根本見直し / F コンテンツ
- **記事=流入の起点 + 提供価値の両立**: SEO とコンテンツ質を独立した目標として設計

---

## Phase 5 : スコアアルゴリズム拡張 ( 2026-06-13 )

### 5.1 updatedAt フィールド

- 全 104 記事に `updatedAt` 注入 ( 初期値 = publishedAt )
- `_scripts/inject_updated_at.py --stamp <slug>` でリライト時に today へ更新
- JSON-LD `dateModified` + OG `article:modified_time` 出力 ( SEO・Google Discover 反映 )

### 5.2 GA4 連携

- service account 設定 ( Google Cloud + GA4 閲覧者権限 + Data API 有効化 )
- `_scripts/fetch_ga4_engagement.py` で pageReferrer 経由 internal / external PV を分解
- ga4Score ( 0-25 ) を internal_pv × engagement_seconds_avg ベースで算出
- 記事 GA タグを統一して計測経路を一本化

### 5.3 推定スコア + 打席ブースト

- GA4 蓄積前の「スタート地点」を作るため、char_count / table_count / 関連 ISSUE 数 / カテゴリから internal_pv・engagement_seconds_avg を <strong>推定</strong>
- `ga4Source: estimated / actual` を区別・推定値は重みを半分に
- 新規・リライト記事は updatedAt から 21日間 boostScore (15→10→5→0) で TOP / 関連記事に <strong>打席ブースト</strong>

### 5.4 composite スコア式

```
composite = quality ( 構造 0-100 ) + ga4Score ( エンゲ 0-25 ) + boostScore ( 0-15 )
          → 同点は freshness → publishedAt
```

- 鮮度 ( freshness ) は <strong>tiebreaker のみ</strong>・品質には加算しない
- TOP / 関連記事 / 一覧ソートの全箇所で 同一ロジックを使用

### 5.5 PV × エンゲ マトリクス

- A / B / C / D / E / F / NODATA の 7 タイプ判定
- priorityType フィールドを data.js に注入
- 強化ルーチンの prompt にタイプ別の打ち手を組み込み

---

## Phase 6 : 回遊強化 ( 2026-06-13 )

### 6.1 TOP 読み物セクション

- 4件表示・フィルタ連動 ( アクティブな ISSUE 群との関連性スコア )
- composite + 関連性 で動的に選定

### 6.2 記事下 関連記事

- 共通 ISSUE 数 × 15 + カテゴリ一致 +10 を関連性スコアとして合成
- 関連性 > 0 を優先 → 不足分は composite Top で補完
- 4件まで常時表示・summary 付き

### 6.3 シリーズ化 ( seriesId )

- ARTICLES に optional `seriesId` フィールド ( 例 : `jr_hokkaido_v1` )
- シリーズ続編記事を関連記事の上位に表示する設計 ( JS 加算は次のターン予定 )

---

## Phase 7 : 編集装置・ラベル ( 2026-06-13 )

### 7.1 ファクト / 仮説 / 推測のバッジ装置

- `fact` ( 緑 )・`hypo` ( オレンジ )・`spec` ( 灰 ) の 3種ブロック
- fact は出典必須・hypo / spec は編集部の解釈 / 推測を明示
- CSS pill + border-left + 出典リンクの cite 要素

### 7.2 NEW / UPDATED ラベル

- 公開 5日以内 = `NEW` ( 緑 )
- 更新 5日以内 = `UPDATED` ( 青 )
- 競合時は UPDATED 優先
- TOP / `/articles/` 一覧 / 記事ページ全てに SSR + JS で表示

### 7.3 update_note ブロック

- 記事内アップデート箇所を明示する装置
- `('update_note', "変更内容", "2026-XX-XX")` で挿入可能
- リライト時に冒頭または該当 section に置く

---

## Phase 8 : /articles/ 一覧フィルタ ( 2026-06-13 )

TOP の課題カードと同役割同デザインで踏襲:

- **並び順**: おすすめ ( composite + boost ) / 新しい順 ( publishedAt ) / アップデート順 ( updatedAt )
- **課題分類**: TOP と同じ CATEGORIES の 8分類・ISSUE.cat 経由で記事をフィルタ
- **キーワード**: 関連 ISSUE.tags 頻度上位 5件 chip + フリーワード input ( タイトル / 概要 / tag を横断検索 )
- **地域**: REGIONS から 6 chip ( 道央 / 道南 / 道北 / オホーツク / 十勝 / 釧路根室 )
- **地域特性**: TRAITS から 7 chip ( 都市部 / 中山間 / 漁村 / 酪農 / 農業 / 観光地 / 産業集積 )
- **リセット**: 全状態を初期化

---

## Phase 9 : つぶやき編集フロー ( 2026-06-13 )

大東の取材・インタビュー・思いつき・データを記事に反映するルート B を制度化:

### 9.1 Notion DB「hokkaido-research つぶやきメモ」

- 親ページ: 「hokkaido-research 運用ハブ」 ( 個人作業・非公開 )
- スキーマ: 内容 / 受領日 / 種別 / 取材源 / 関連トピック / 判断 / 関連 slug / ステータス / 適用日 / メモ ID / 添付 / Drive URL

### 9.2 Google Drive 連携

- 「hokkaido-research/取材アーカイブ」フォルダ作成
- 写真・音声・PDF を Drive にアップ → URL を Notion に貼り付け
- Claude が Drive MCP で画像認識 / PDF 解析

### 9.3 スマホ運用 ( 4 チャネル )

- Notion 公式アプリ ( メイン手段 )
- Google Drive アップ + Notion に URL
- Gmail 経由 ( 件名 `[hokkaido-tweet]` )
- GitHub Issue 経由

### 9.4 トリガーワード

- Claude に「**つぶやきメモ取得**」と発話 → 未処理メモを判断 ( 新規 / リライト / ISSUE 更新 / スルー )

---

## Phase 10 : リライト 第 1 弾 ( 2026-06-13 )

5本を全面リライト ( 5分読了・ファクト / 仮説 / 推測の区別・推移データ・シリーズ化 ):

1. **depopulation-recover** - 道人口 498万 ( -4.6%・70年ぶり 500万割れ )・海士町 18年・神山町 16年・上士幌
2. **semiconductor-rapidus-strategy** - 政府支援 累計 2.9兆円・2025/4 試作・2027 量産予定・新竹 / Intel / 韓国
3. **jr-hokkaido-future-structure** - 営業赤字 ▲ 582億円・11年連続全区間赤字・JR 西 17 線区・いすみ・SBB
4. **tourism-sustainability-dual** - 倶知安地価 +44%・ニセコ外国人宿泊 73.88万・京都宿泊税・Amsterdam・アイスランド
5. **childcare-shortage-strategy** - 全国保育士求人倍率 3.78・道出生率 1.06・流山・明石・北欧

---

## Phase 11 : リライト 第 2 弾 ( 2026-06-13 )

シリーズ連動 + 高品質化で 5本:

1. **elderly-care-staff-strategy** ( `elderly_care_v1` ) - 全国不足 32 → 69万・求人倍率 4.08・道高齢化 33.2%・豊岡 / Buurtzorg / ドイツ
2. **fisheries-climate-strategy** ( `fisheries_v1` ) - サケ 14.4 → 5.0万 t・サンマ 35 → 2.5万 t・ブリ急増・ノルウェー / アイスランド ITQ / MSC
3. **low-birthrate-structure** ( `childcare_v1` ) - 道出生率 1.27 → 1.01・札幌 0.96・流山 / 明石 / 北欧
4. **rail-transit-structure** ( `jr_hokkaido_v1` ) - 中央バス廃止・いさりび 10年・道北バス統合・富山 LRT・SBB / Whim
5. **energy-security-structure** ( `energy_v1` ) - 太陽光 90 → 231万 kW・風力 30 → 136万 kW・出力制御・デンマーク / ドイツ / 上士幌

---

## Phase 12 : 運用シェル + パイプライン整備 ( 2026-06-13 )

### 12.1 `_scripts/refresh_quality.sh`

- 1 コマンドで GA4 取得 → 採点 → スコア注入 → 記事再生成 → push まで実行
- フロー: <strong>生成 → 採点 → 注入 → 再生成</strong> の 2段階生成 ( リライト直後でも最新スコアが反映 )

### 12.2 補助スクリプト

- `_scripts/quality_assessment.py` ( 構造 + 鮮度 + 推定 GA4 + priorityType )
- `_scripts/inject_quality_score.py` ( data.js の各 ARTICLES に注入 )
- `_scripts/inject_updated_at.py` ( --stamp <slug> でリライト stamp )
- `_scripts/fetch_ga4_engagement.py` ( GA4 Data API )
- `_scripts/generate_articles.py` ( ARTICLES → 記事 HTML 一括生成 )

---

## サマリ・数値

- 公開記事数: 約 30 → 104件
- ISSUE 数: 20 → 66件
- 用語集: 24 → 65 用語
- リライト累計: 14本 ( 第 1 弾 5 + 第 2 弾 5 + 4本の段階的補強 )
- スクリプト: 7個 ( 自動化パイプライン )
- 強化ドラフト Notion DB: 2個 ( 品質強化 + 情報ソース )
- メモリ追加: 5個 ( 編集方針 / 情報源戦略 / 優先マトリクス / 執筆ルール / つぶやき intake )

---

## 次のフェーズ ( 想定 )

- seriesId のスコア加算実装 ( 関連記事 +30 )
- 残り構造弱記事の継続リライト
- Whisper / Notion AI 音声文字起こし連携
- GA4 データ蓄積に伴う 推定スコア → 実スコアへの自動切り替え
- つぶやきメモ運用開始・Drive 取材アーカイブ蓄積
- iOS ショートカット・Telegram / LINE Bot などの追加チャネル
