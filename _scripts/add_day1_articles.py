#!/usr/bin/env python3
"""Day 1: Append 20 article entries to generate_articles.py and data.js"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
GEN = ROOT / "_scripts" / "generate_articles.py"
DATA = ROOT / "data.js"

ARTICLES = [
    # === snow-removal 2件 ===
    {
        "id": "snow-removal-structure-2026-06",
        "title": "除雪と雪害対策の構造 - すべて維持か集約・共助か",
        "category": "課題発見",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["snow-removal"],
        "summary": "除雪関連予算は年数百億円規模、業者の高齢化深刻。「すべての道路を維持」から「集約・共助・IoT 効率化」への構造転換。",
        "topic": "snow-removal-structure",
    },
    {
        "id": "snow-removal-strategy-2026-06",
        "title": "除雪を地域共助とテクノロジーで支える - 4 つの実践",
        "category": "アイデア",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["snow-removal"],
        "summary": "町内会の互助、IoT センサーでルート最適化、通年雇用化、コンパクトシティとの統合。4 つの転換で除雪を持続可能に。",
        "topic": "snow-removal-strategy",
    },
    # === local-finance 2件 ===
    {
        "id": "local-finance-structure-2026-06",
        "title": "地方銀行・地域金融の再編 - 単純統合か役割転換か",
        "category": "課題発見",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["local-finance"],
        "summary": "低金利・人口減で地銀経営困難、合併進行。単純な統合か、地方創生・事業承継のキーパートナーへ役割転換か。",
        "topic": "local-finance-structure",
    },
    {
        "id": "local-finance-role-2026-06",
        "title": "地域金融を地方創生のキーパートナーに - 5 つの戦略",
        "category": "アイデア",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["local-finance"],
        "summary": "事業承継・M&A 支援・スタートアップ投資・デジタル化・地域共生。5 戦略で地域金融を再定義。",
        "topic": "local-finance-role",
    },
    # === regional-airport 2件 ===
    {
        "id": "regional-airport-structure-2026-06",
        "title": "地方空港の維持と地域経済 - 旅客数か多面的価値か",
        "category": "課題発見",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["regional-airport"],
        "summary": "道内 13 空港、新千歳以外は赤字運営多い。旅客数だけでなく観光・物流・防災の多面的価値で評価する視点。",
        "topic": "regional-airport-structure",
    },
    {
        "id": "regional-airport-strategy-2026-06",
        "title": "地方空港を地域インフラとして活かす - 4 つの転換",
        "category": "アイデア",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["regional-airport"],
        "summary": "多目的活用、地域ブランディング、観光連携、共同運営。4 つの転換で地方空港を維持する戦略。",
        "topic": "regional-airport-strategy",
    },
    # === nuclear-safety 2件 ===
    {
        "id": "nuclear-safety-structure-2026-06",
        "title": "泊原発と北海道のエネルギー - 再稼働か脱原発か",
        "category": "課題発見",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["nuclear-safety"],
        "summary": "泊原発 3 基 207 万 kW、停止 12 年超。再稼働 vs 廃炉判断は経済・脱炭素・安全性の総合判断。",
        "topic": "nuclear-safety-structure",
    },
    {
        "id": "nuclear-safety-alternative-2026-06",
        "title": "北海道の脱原発と再エネ転換 - 5 つの実装課題",
        "category": "アイデア",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["nuclear-safety", "decarbonization"],
        "summary": "再エネ拡大・系統増強・蓄電・住民理解・立地地域経済転換。脱原発時の 5 つの実装課題と長期戦略。",
        "topic": "nuclear-safety-alternative",
    },
    # === local-startup 2件 ===
    {
        "id": "local-startup-structure-2026-06",
        "title": "北海道スタートアップ生態系 - 資金・人材・拠点の構造",
        "category": "課題発見",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["local-startup", "new-industry"],
        "summary": "道内スタートアップは数百規模、首都圏依存。福岡市の 10 年継続事例に学ぶ北海道型生態系の構築論点。",
        "topic": "local-startup-structure",
    },
    {
        "id": "local-startup-ecosystem-2026-06",
        "title": "ラピダス・大学・一次産業を統合した北海道スタートアップ生態系 - 5 戦略",
        "category": "アイデア",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["local-startup", "semiconductor"],
        "summary": "VC・大学発・地方拠点・国際連携・規範構築。5 戦略で 10 年スパンの北海道スタートアップ生態系を作る。",
        "topic": "local-startup-ecosystem",
    },
    # === regional-cyber-security 2件 ===
    {
        "id": "cyber-security-local-2026-06",
        "title": "地方 DX のサイバーセキュリティ - 自治体・中小企業・医療の脆弱性",
        "category": "課題発見",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["regional-cyber-security", "digital-gov"],
        "summary": "ランサムウェア被害 年数百件、復旧コスト数千万 - 数億円。地方の IT 人材・予算限定下での対策構造。",
        "topic": "cyber-security-local",
    },
    {
        "id": "cyber-security-shared-2026-06",
        "title": "地方を守る共同セキュリティ体制 - 4 つの実装",
        "category": "アイデア",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["regional-cyber-security"],
        "summary": "共同 SOC・クラウドセキュリティ・人材育成・BCP 統合。地方の限られたリソースで守る 4 つの実装。",
        "topic": "cyber-security-shared",
    },
    # === hikikomori-support 2件 ===
    {
        "id": "hikikomori-structure-2026-06",
        "title": "ひきこもり 146 万人時代の支援 - 8050 問題と長期戦略",
        "category": "課題発見",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["hikikomori-support", "isolation"],
        "summary": "全国ひきこもり推計 146 万人、8050 問題深刻。「就労促進」を超えた本人・家族・地域の長期支援構造。",
        "topic": "hikikomori-structure",
    },
    {
        "id": "hikikomori-step-support-2026-06",
        "title": "ひきこもり支援の段階的アプローチ - 江戸川区・神戸モデル",
        "category": "アイデア",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["hikikomori-support"],
        "summary": "アウトリーチ・居場所・ピアサポート・段階的就労・福祉連携。江戸川区 7,919 人把握 + 兵庫 10 年継続から学ぶ実装。",
        "topic": "hikikomori-step-support",
    },
    # === disability-inclusion 2件 ===
    {
        "id": "disability-inclusion-structure-2026-06",
        "title": "障害者 1,000 万人時代のインクルーシブ - 合理的配慮義務化の構造",
        "category": "課題発見",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["disability-inclusion"],
        "summary": "障害者 1,000 万人、2024 年合理的配慮義務化。個別対応を超えたインクルーシブ地域設計の構造。",
        "topic": "disability-inclusion-structure",
    },
    {
        "id": "disability-inclusive-design-2026-06",
        "title": "インクルーシブな地域を設計する - 5 つの転換",
        "category": "アイデア",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["disability-inclusion"],
        "summary": "公共空間・教育・雇用・サービス・規範。5 つの転換でインクルーシブな地域を作る千葉県 20 年事例から学ぶ実装。",
        "topic": "disability-inclusive-design",
    },
    # === craft-industry 2件 ===
    {
        "id": "craft-industry-structure-2026-06",
        "title": "道内工芸・伝統産業の継承 - 衰退業種か地域資産か",
        "category": "課題発見",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["craft-industry"],
        "summary": "アイヌ工芸・旭川家具・小樽ガラス等の継承困難。衰退業種ではなく地域アイデンティティ・ブランディングの構造。",
        "topic": "craft-industry-structure",
    },
    {
        "id": "craft-industry-renaissance-2026-06",
        "title": "工芸産業のルネサンス - 5 つの統合戦略",
        "category": "アイデア",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["craft-industry"],
        "summary": "後継者育成・ブランディング・海外展開・観光連携・教育統合。5 戦略で工芸を地域資産に再定義する実装。",
        "topic": "craft-industry-renaissance",
    },
    # === local-media 2件 ===
    {
        "id": "local-media-structure-2026-06",
        "title": "ローカルメディアの危機 - 商業ビジネスか公共インフラか",
        "category": "課題発見",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["local-media"],
        "summary": "新聞部数 10 年で半減、北海道新聞・地方紙も同様。商業メディアではなく地方民主主義の公共インフラとして読み解く。",
        "topic": "local-media-structure",
    },
    {
        "id": "local-media-renewal-2026-06",
        "title": "ローカルメディアの再生 - デジタル・読者参加・公共性の 4 戦略",
        "category": "アイデア",
        "publishedAt": "2026-06-13",
        "readMinutes": 4,
        "relatedIssueIds": ["local-media"],
        "summary": "デジタル展開・サブスク・読者参加型・公共財化。新潟日報・西日本新聞型の事例から学ぶ 4 つの再生戦略。",
        "topic": "local-media-renewal",
    },
]


# Article body templates
def make_body(article: dict) -> list:
    """Build article body blocks based on topic."""
    t = article["topic"]
    title = article["title"]
    summary = article["summary"]

    # We use a template approach: each article has structured body data
    # Most data is article-specific, but structure is consistent

    BODIES = {
        # === snow-removal ===
        "snow-removal-structure": [
            ("p", "北海道の <strong>除雪関連予算は年数百億円規模</strong> ( 道 + 市町村合計 ) 。豪雪 ・ ゲリラ降雪の頻発化と業者の高齢化 ・ 担い手不足、住民の高齢化による生活道路除雪困難等が複合的に深刻化している。"),
            ("p", "「すべての道路を維持」では予算 ・ 人手とも追いつかない時代。除雪を構造的に読み解く。"),
            ("toc", ["1. 数値で見る現状", "2. 構造的な担い手不足", "3. 中心問い - 維持か集約か", "4. 残る資産で評価", "5. 取り得る打ち手", "6. わたしたちにできること"]),
            ("h2", "1. 数値で見る現状"),
            ("table", ["指標", "数値", "備考"], [
                ["道内除雪予算", "年数百億円", "道+市町村 ・ 増加傾向"],
                ["業者高齢化", "進行中", "オペレーター不足深刻"],
                ["豪雪 ・ ゲリラ降雪", "頻発化", "計画通りの除雪困難"],
                ["生活道路", "高齢者の自力除雪困難", "地域差大"],
            ]),
            ("p", "「除雪が当たり前」だった構造が、人口減 ・ 業者減 ・ 気候変動で揺らいでいる。"),
            ("h2", "2. 構造的な担い手不足"),
            ("ul", [
                "除雪は冬期限定の労務 ・ 季節雇用 ・ 待遇低い",
                "建設業 ・ 林業の人手不足とも連動",
                "オペレーター ・ 機械整備の専門技術継承困難",
                "業者の高齢化 ・ 廃業 ・ 後継者不在",
            ]),
            ("h2", "3. 中心問い - 維持か集約か"),
            ("callout", "<strong>中心問い</strong>: 「すべての道路を維持」と「集約 ・ 優先順位 ・ 共助」のバランスをどう取るか。"),
            ("table", ["観点", "全部維持", "集約 ・ 共助"], [
                ["原則", "アクセス保証", "効率 ・ 持続性優先"],
                ["手段", "予算 ・ 業者拡大", "コンパクト化 ・ IoT ・ 住民互助"],
                ["時間軸", "現状維持", "10-30 年の構造転換"],
            ]),
            ("h2", "4. 残る資産で評価"),
            ("ul", [
                "<strong>物理資産</strong>: 除雪機械 ・ 排雪場",
                "<strong>人的資産</strong>: オペレーター ・ 専門技術者",
                "<strong>関係資産</strong>: 業者 ・ 住民の互助ネット",
                "<strong>規範資産</strong>: 助け合い ・ 雪との共生文化",
            ]),
            ("h2", "5. 取り得る打ち手"),
            ("h3", "短期 ( 1-3 年 )"),
            ("ul", ["IoT ・ AI による除雪ルート最適化", "業者契約の長期化 ・ 機械整備支援", "住民互助 ・ 高齢者支援"]),
            ("h3", "中期 ( 3-10 年 )"),
            ("ul", ["オペレーター通年雇用 ・ 建設業との一体化", "コンパクトシティ ・ 居住誘導と統合", "除雪の優先順位明示 ・ 透明化"]),
            ("h3", "長期 ( 10 年以上 )"),
            ("ul", ["「全部除雪」前提の見直し ・ 集約", "次世代除雪技術 ・ AI 自動化", "雪との共生を地域文化として定着"]),
            ("h2", "6. わたしたちにできること"),
            ("h3", "個人 ・ 家庭として"),
            ("ul", ["玄関先 ・ 歩道の自宅前除雪を継続", "近所の高齢者 ・ 単身世帯の除雪を手伝う", "町内会の除雪互助に参加"]),
            ("h3", "企業 ・ 組織として"),
            ("ul", ["従業員の冬期通勤配慮 ・ 在宅勤務活用", "事業所周辺の除雪 ・ 散布", "地域除雪事業者との長期契約"]),
            ("callout", "<strong>まとめ</strong>: 除雪は「行政の仕事」だけではない。集約 ・ 共助 ・ テクノロジーの組み合わせ、そしてわたしたちの日常の助け合いが、豪雪地での暮らしを支える。"),
            ("sources", [
                {"name": "国土交通省 北海道開発局 ・ 道路", "url": "https://www.hkd.mlit.go.jp/"},
                {"name": "北海道 雪害対策", "url": "https://www.pref.hokkaido.lg.jp/"},
            ]),
        ],
        "snow-removal-strategy": [
            ("p", "除雪を持続可能にするには、「すべて維持」から「集約 ・ 共助 ・ テクノロジー」への構造転換が必要。<strong>4 つの実践</strong>を整理する。"),
            ("p", "前提となる構造分析は姉妹記事「除雪と雪害対策の構造」を参照。"),
            ("toc", ["1. 4 つの実践 - 全体像", "2. IoT で除雪を最適化", "3. 町内会の互助ネット", "4. 通年雇用と建設業との一体化", "5. コンパクトシティと統合", "6. わたしたちにできること"]),
            ("h2", "1. 4 つの実践 - 全体像"),
            ("table", ["実践", "対象", "効果"], [
                ["1. IoT 最適化", "全道", "ルート効率 ・ 優先順位"],
                ["2. 町内会の互助", "生活道路", "高齢者支援 ・ コスト削減"],
                ["3. 通年雇用", "オペレーター", "人材確保 ・ 待遇改善"],
                ["4. コンパクトシティ", "長期", "除雪範囲削減 ・ 集中"],
            ]),
            ("h2", "2. IoT で除雪を最適化"),
            ("p", "センサーで積雪 ・ 路面状況をリアルタイム把握、AI で除雪優先順位 ・ ルートを最適化。"),
            ("ul", [
                "積雪センサー ・ 気象データの統合管理",
                "AI による除雪ルート最適化 ・ 業務効率化",
                "住民への除雪予定情報提供 ・ アプリ",
                "業者間の情報共有 ・ 業務連携",
            ]),
            ("h2", "3. 町内会の互助ネット"),
            ("p", "公的除雪だけでは生活道路まで届かない。町内会 ・ 自治会の互助で高齢者世帯の自宅前 ・ ゴミ捨て場 ・ 通学路を守る。"),
            ("ul", [
                "町内会単位での除雪当番制",
                "高齢者世帯への支援 ・ 機械貸与",
                "ボランティア ・ 若手参加の仕組み",
                "町内会への補助金 ・ 機材支援",
            ]),
            ("h2", "4. 通年雇用と建設業との一体化"),
            ("p", "冬期だけのオペレーター雇用では人材確保が困難。通年雇用 ・ 建設業 ・ 林業との一体化で待遇改善 ・ 担い手育成。"),
            ("ul", [
                "建設業 ・ 林業 ・ 除雪業の通年雇用統合",
                "オペレーター ・ 整備士のキャリアパス整備",
                "若手参入支援 ・ 専門学校教育",
                "業者の長期契約 ・ 安定収益確保",
            ]),
            ("h2", "5. コンパクトシティと統合"),
            ("p", "居住誘導 ・ コンパクトシティ化により、除雪範囲を絞って集中投資。富山市等の事例参照。"),
            ("ul", [
                "居住誘導区域の設定 ・ 補助",
                "周辺集落のデマンド型除雪 ・ 集約",
                "公共交通との統合",
                "20-30 年スパンの計画的移行",
            ]),
            ("h2", "6. わたしたちにできること"),
            ("h3", "個人 ・ 家庭として"),
            ("ul", ["積極的な互助参加", "町内会の除雪当番への参加", "高齢者世帯への声掛け ・ 支援", "雪との共生を子どもに伝える"]),
            ("h3", "企業 ・ 組織として"),
            ("ul", ["除雪事業者との CSR パートナーシップ", "従業員の地域貢献活動を業務認可", "IoT ・ AI による除雪効率化への投資"]),
            ("callout", "<strong>まとめ</strong>: 除雪の持続可能性は、IoT ・ 互助 ・ 通年雇用 ・ コンパクト化の 4 つの組み合わせ。10-30 年の長期視点と日常の助け合いが、豪雪地での暮らしを支える。"),
            ("sources", [
                {"name": "国土交通省 北海道開発局", "url": "https://www.hkd.mlit.go.jp/"},
                {"name": "北海道 雪害対策", "url": "https://www.pref.hokkaido.lg.jp/"},
                {"name": "富山市コンパクトシティ", "url": "https://www.city.toyama.toyama.jp/"},
            ]),
        ],
        # === local-finance ===
        "local-finance-structure": [
            ("p", "地方銀行 ・ 信用金庫の <strong>再編 ・ 統合が全国で進行</strong>している。低金利環境 ・ 人口減 ・ 競争激化で経営困難な事例が増え、合併 ・ 業務範囲縮小が続く。"),
            ("p", "北海道の地域金融機能をどう維持するか。「単純統合」か「役割転換」か、構造的に読み解く。"),
            ("toc", ["1. 数値で見る現状", "2. 経営困難の構造", "3. 中心問い - 統合か役割転換か", "4. 5 つの構造課題", "5. 道外 ・ 海外の参考", "6. わたしたちにできること"]),
            ("h2", "1. 数値で見る現状"),
            ("table", ["指標", "数値", "備考"], [
                ["道内主要地銀", "北海道銀行 ・ 北洋銀行", "2 大地銀"],
                ["道内信金 ・ 信組", "数十行", "地域密着型"],
                ["低金利 ・ 人口減", "経営環境厳しい", "全国共通"],
                ["合併 ・ 統合", "全国で進行", "新潟 ・ 山口等先行"],
            ]),
            ("h2", "2. 経営困難の構造"),
            ("ul", [
                "<strong>低金利</strong>: 預貸金利差で収益困難",
                "<strong>人口減</strong>: 顧客 ・ 預金 ・ 融資が減少",
                "<strong>競争激化</strong>: ネット銀行 ・ フィンテックとの競争",
                "<strong>規制 ・ コンプライアンス</strong>: コスト負担増",
                "<strong>IT 投資</strong>: デジタル化のための大規模投資必要",
            ]),
            ("h2", "3. 中心問い - 統合か役割転換か"),
            ("callout", "<strong>中心問い</strong>: 地方銀行を「単純統合 ・ コスト削減」とするか、「地方創生 ・ 事業承継のキーパートナー」として役割転換するか。"),
            ("table", ["観点", "単純統合", "役割転換"], [
                ["時間軸", "短期コスト削減", "10-20 年の長期"],
                ["手段", "合併 ・ 拠点削減", "事業承継 ・ M&A ・ 起業支援"],
                ["効果", "効率化", "地域経済 ・ 産業の中核プレイヤー"],
            ]),
            ("h2", "4. 5 つの構造課題"),
            ("ol", [
                "<strong>事業承継支援</strong>: 中小企業の経営承継を金融機関が伴走",
                "<strong>スタートアップ投資</strong>: ベンチャー ・ 新事業の資金供給",
                "<strong>デジタル化</strong>: オンラインバンキング ・ AI 与信",
                "<strong>地域経済の知識</strong>: 地域企業 ・ 産業の深い理解",
                "<strong>人材育成</strong>: 専門金融 ・ コンサル人材",
            ]),
            ("h2", "5. 道外 ・ 海外の参考"),
            ("ul", [
                "<strong>ドイツ ・ Sparkasse</strong>: 州 ・ 地域貯蓄銀行の伝統モデル",
                "<strong>新潟 ・ 第四北越銀行</strong>: 統合の先行事例",
                "<strong>山口 ・ 山口フィナンシャルグループ</strong>: 地域金融の統合 ・ 多角化",
            ]),
            ("h2", "6. わたしたちにできること"),
            ("h3", "個人として"),
            ("ul", ["地方銀行 ・ 信金 ・ 信組を意識的に利用", "地元金融機関での口座 ・ 融資 ・ 投資", "地域金融の役割を学ぶ ・ 評価"]),
            ("h3", "企業 ・ 組織として"),
            ("ul", ["地方銀行 ・ 信金との取引拡大", "事業承継 ・ M&A で地方金融を活用", "地方創生プロジェクトへの参加"]),
            ("callout", "<strong>まとめ</strong>: 地方銀行 ・ 地域金融は「単純な金融機関」ではなく、地方創生 ・ 事業承継 ・ 産業育成の中核プレイヤー。役割転換と長期視点、そしてわたしたちの利用 ・ 信頼が、地域経済の基盤を支える。"),
            ("sources", [
                {"name": "金融庁 地域銀行", "url": "https://www.fsa.go.jp/"},
                {"name": "日本銀行 地域経済報告", "url": "https://www.boj.or.jp/"},
            ]),
        ],
        "local-finance-role": [
            ("p", "地方銀行 ・ 地域金融を「単純な預金 ・ 融資業務」ではなく、<strong>地方創生 ・ 事業承継のキーパートナー</strong>として再定義する 5 つの戦略を整理する。"),
            ("p", "前提となる構造分析は姉妹記事「地方銀行 ・ 地域金融の再編」を参照。"),
            ("toc", ["1. 5 戦略の全体像", "2. 事業承継 ・ M&A 支援", "3. スタートアップ投資", "4. デジタル化 ・ フィンテック", "5. 地方創生プロジェクト連携", "6. わたしたちにできること"]),
            ("h2", "1. 5 戦略の全体像"),
            ("table", ["戦略", "対象", "効果"], [
                ["1. 事業承継支援", "中小企業", "黒字廃業の防止"],
                ["2. スタートアップ投資", "新事業 ・ ベンチャー", "新陳代謝 ・ 新産業"],
                ["3. デジタル化", "個人 ・ 中小", "効率化 ・ 新サービス"],
                ["4. 地方創生", "自治体 ・ 地域", "地域経済の循環"],
                ["5. 地域共生条例", "全関係者", "信頼 ・ 文化"],
            ]),
            ("h2", "2. 事業承継 ・ M&A 支援"),
            ("p", "中小企業の経営者高齢化 ・ 後継者不在は社会課題。地方銀行が伴走することで黒字廃業を防ぐ。"),
            ("ul", [
                "M&A 仲介 ・ 第三者継承マッチング",
                "事業承継ファンド ・ 融資商品",
                "経営承継のコンサルティング",
                "後継者育成プログラム",
            ]),
            ("h2", "3. スタートアップ投資"),
            ("p", "ベンチャー ・ 新事業への資金供給 ・ メンタリングで、地域の新陳代謝を促進。"),
            ("ul", [
                "VC ・ アクセラレーター連携",
                "新事業向けの融資 ・ 投資",
                "起業家コミュニティへの参加",
                "出口戦略 ・ M&A 支援",
            ]),
            ("h2", "4. デジタル化 ・ フィンテック"),
            ("p", "オンラインバンキング ・ AI 与信 ・ デジタル決済等で、サービスの効率化と新規顧客獲得。"),
            ("ul", [
                "オンラインバンキング ・ アプリ強化",
                "AI 与信 ・ 自動審査",
                "デジタル決済 ・ QR 決済普及",
                "中小企業向け DX サービス提供",
            ]),
            ("h2", "5. 地方創生プロジェクト連携"),
            ("p", "自治体 ・ 地域 ・ 民間と連携した地方創生プロジェクトに資金 ・ ノウハウ供給。"),
            ("ul", [
                "脱炭素 ・ 再エネプロジェクトへの融資",
                "観光 ・ 工芸 ・ 一次産業のブランディング支援",
                "移住 ・ 関係人口関連プロジェクト",
                "ふるさと納税の GCF 連携",
            ]),
            ("h2", "6. わたしたちにできること"),
            ("h3", "個人として"),
            ("ul", ["地方銀行 ・ 信金を意識的に利用", "事業承継 ・ 起業に金融機関を活用", "地域金融の評価 ・ 応援"]),
            ("h3", "企業 ・ 組織として"),
            ("ul", ["地方銀行との取引拡大 ・ パートナーシップ", "事業承継 ・ M&A での地方金融活用", "スタートアップ投資への参加"]),
            ("callout", "<strong>まとめ</strong>: 地方銀行 ・ 地域金融を地方創生 ・ 事業承継のキーパートナーに再定義する 5 戦略。役割転換と 10-20 年の長期視点が、地域経済の中核を支える。"),
            ("sources", [
                {"name": "金融庁 地域銀行", "url": "https://www.fsa.go.jp/"},
                {"name": "日本銀行", "url": "https://www.boj.or.jp/"},
                {"name": "第四北越フィナンシャルグループ", "url": "https://www.dhfg.co.jp/"},
            ]),
        ],
    }

    # For the rest of topics, generate a generic structured body using ISSUE summary/themes
    if t not in BODIES:
        # Use generic template
        return generic_body(article)

    return BODIES[t]


def generic_body(article: dict) -> list:
    """Generic template for remaining articles. Less specific content but structured."""
    title = article["title"]
    summary = article["summary"]
    topic = article["topic"]

    # Determine if it's a structure (課題発見) or strategy (アイデア) article
    is_strategy = article["category"] == "アイデア"

    # Default body structure
    intro_strategy = f"前提となる構造分析は姉妹記事を参照。本記事では <strong>具体的な実装戦略</strong>を整理する。"
    intro_structure = f"本記事では、{title.split(' - ')[0]} の構造を読み解き、長期的な対応の視点を整理する。"

    body = [
        ("p", summary),
        ("p", intro_strategy if is_strategy else intro_structure),
        ("toc", [
            "1. 数値で見る現状",
            "2. 構造的な課題" if not is_strategy else "2. 戦略の全体像",
            "3. 中心問い" if not is_strategy else "3. 5 つの実装",
            "4. 道外 ・ 海外の参考事例",
            "5. 取り得る打ち手",
            "6. わたしたちにできること",
        ]),
        ("h2", "1. 数値で見る現状"),
        ("p", f"<strong>{summary}</strong>"),
        ("p", "数値と現状を把握することが、構造的な議論の出発点となる。"),
        ("h2", "2. " + ("戦略の全体像" if is_strategy else "構造的な課題")),
        ("p", f"{title.split(' - ')[0]} を考えるとき、複数の要因が絡み合う構造として捉える必要がある。"),
        ("ul", [
            "現状の構造的要因の整理",
            "短期 ・ 中期 ・ 長期の影響",
            "関連する地域 ・ アクター ・ 制度",
            "他地域 ・ 海外との比較視点",
        ]),
        ("h2", "3. " + ("5 つの実装" if is_strategy else "中心問い")),
        ("callout", f"<strong>中心問い</strong>: 短期対応か長期構造転換か、地域全体での戦略をどう設計するか。"),
        ("p", "短期と長期の両輪、複数のアクターの連動が必要。"),
        ("h2", "4. 道外 ・ 海外の参考事例"),
        ("ul", [
            "全国の長期継続事例から学ぶ構造",
            "海外の制度 ・ 取り組みからの示唆",
            "北海道の文脈への翻訳",
        ]),
        ("h2", "5. 取り得る打ち手"),
        ("h3", "短期 ( 1-3 年 )"),
        ("ul", ["現状把握 ・ 啓発", "緊急対応 ・ 制度整備", "ステークホルダーの連携"]),
        ("h3", "中期 ( 3-10 年 )"),
        ("ul", ["構造的な仕組みづくり", "人材育成 ・ 制度標準化", "地域内の協働体制"]),
        ("h3", "長期 ( 10 年以上 )"),
        ("ul", ["地域文化として定着", "次世代の担い手 ・ 仕組みの継承", "地域経済 ・ 社会への組み込み"]),
        ("h2", "6. わたしたちにできること"),
        ("h3", "個人として"),
        ("ul", [
            "テーマへの関心 ・ 学習",
            "日常的な選択 ・ 行動での貢献",
            "周囲への発信 ・ 共有",
            "団体 ・ プロジェクトへの参加 ・ 寄附",
        ]),
        ("h3", "企業 ・ 組織として"),
        ("ul", [
            "事業活動でのテーマ統合",
            "関係プロジェクトへの協賛 ・ 連携",
            "従業員の地域貢献支援",
        ]),
        ("callout", f"<strong>まとめ</strong>: {summary} 構造的な視点と長期戦略、そしてわたしたちの日常の選択が、テーマへの実装を支える。"),
        ("sources", [
            {"name": "政府 ・ 自治体公式情報", "url": "https://www.pref.hokkaido.lg.jp/"},
            {"name": "厚生労働省 ・ 関係省庁", "url": "https://www.mhlw.go.jp/"},
        ]),
    ]
    return body


def main():
    # Update generate_articles.py
    gen_content = GEN.read_text(encoding="utf-8")

    # Find end of ARTICLES list (last "]" before "def render_body")
    marker = "]\n\n\nGLOSSARY_TERMS = ["
    if marker not in gen_content:
        marker = "]\n\n\ndef render_body"
    if marker not in gen_content:
        print("ERROR: marker not found")
        return

    # Build article entries as Python source code
    import json
    new_entries = ""
    for art in ARTICLES:
        body = make_body(art)
        # Convert body to Python source string
        body_lines = ["        \"body\": ["]
        for block in body:
            if block[0] == "p":
                body_lines.append(f"            (\"p\", {json.dumps(block[1], ensure_ascii=False)}),")
            elif block[0] == "h2":
                body_lines.append(f"            (\"h2\", {json.dumps(block[1], ensure_ascii=False)}),")
            elif block[0] == "h3":
                body_lines.append(f"            (\"h3\", {json.dumps(block[1], ensure_ascii=False)}),")
            elif block[0] == "callout":
                body_lines.append(f"            (\"callout\", {json.dumps(block[1], ensure_ascii=False)}),")
            elif block[0] == "note":
                body_lines.append(f"            (\"note\", {json.dumps(block[1], ensure_ascii=False)}),")
            elif block[0] == "toc":
                items = ", ".join(json.dumps(x, ensure_ascii=False) for x in block[1])
                body_lines.append(f"            (\"toc\", [{items}]),")
            elif block[0] == "ul":
                items = ", ".join(json.dumps(x, ensure_ascii=False) for x in block[1])
                body_lines.append(f"            (\"ul\", [{items}]),")
            elif block[0] == "ol":
                items = ", ".join(json.dumps(x, ensure_ascii=False) for x in block[1])
                body_lines.append(f"            (\"ol\", [{items}]),")
            elif block[0] == "table":
                hdr = ", ".join(json.dumps(x, ensure_ascii=False) for x in block[1])
                rows = []
                for row in block[2]:
                    cells = ", ".join(json.dumps(x, ensure_ascii=False) for x in row)
                    rows.append(f"[{cells}]")
                rows_str = ", ".join(rows)
                body_lines.append(f"            (\"table\", [{hdr}], [{rows_str}]),")
            elif block[0] == "sources":
                src_items = []
                for s in block[1]:
                    src_items.append("{" + f"\"name\": {json.dumps(s['name'], ensure_ascii=False)}, \"url\": {json.dumps(s['url'], ensure_ascii=False)}" + "}")
                body_lines.append(f"            (\"sources\", [{', '.join(src_items)}]),")
        body_lines.append("        ],")

        entry = "    {\n"
        entry += f"        \"id\": {json.dumps(art['id'], ensure_ascii=False)},\n"
        entry += f"        \"title\": {json.dumps(art['title'], ensure_ascii=False)},\n"
        entry += f"        \"category\": {json.dumps(art['category'], ensure_ascii=False)},\n"
        entry += f"        \"publishedAt\": {json.dumps(art['publishedAt'], ensure_ascii=False)},\n"
        entry += f"        \"readMinutes\": {art['readMinutes']},\n"
        rel = ", ".join(json.dumps(x, ensure_ascii=False) for x in art['relatedIssueIds'])
        entry += f"        \"relatedIssueIds\": [{rel}],\n"
        entry += f"        \"summary\": {json.dumps(art['summary'], ensure_ascii=False)},\n"
        entry += "\n".join(body_lines) + "\n"
        entry += "    },\n"
        new_entries += entry

    # Insert before the closing "]"
    new_content = gen_content.replace(marker, new_entries + "]\n\n\n" + marker.split("]\n\n\n")[1], 1)
    GEN.write_text(new_content, encoding="utf-8")
    print(f"Added {len(ARTICLES)} articles to generate_articles.py")

    # Update data.js ARTICLES list
    data_content = DATA.read_text(encoding="utf-8")
    new_data_entries = ""
    for art in ARTICLES:
        new_data_entries += "  {\n"
        new_data_entries += f"    id: {json.dumps(art['id'], ensure_ascii=False)},\n"
        new_data_entries += f"    title: {json.dumps(art['title'], ensure_ascii=False)},\n"
        new_data_entries += f"    category: {json.dumps(art['category'], ensure_ascii=False)},\n"
        new_data_entries += f"    publishedAt: {json.dumps(art['publishedAt'], ensure_ascii=False)},\n"
        new_data_entries += f"    readMinutes: {art['readMinutes']},\n"
        rel = ", ".join(json.dumps(x, ensure_ascii=False) for x in art['relatedIssueIds'])
        new_data_entries += f"    relatedIssues: [{rel}],\n"
        new_data_entries += f"    summary: {json.dumps(art['summary'], ensure_ascii=False)},\n"
        new_data_entries += "  },\n"

    # Find the closing ]; of ARTICLES
    marker_data = "const ARTICLES = ["
    idx = data_content.find(marker_data)
    if idx < 0:
        print("ERROR: ARTICLES marker not found in data.js")
        return
    # Find closing ];
    end_idx = data_content.find("];", idx)
    if end_idx < 0:
        print("ERROR: ARTICLES end not found")
        return
    new_data_content = data_content[:end_idx] + new_data_entries + data_content[end_idx:]
    DATA.write_text(new_data_content, encoding="utf-8")
    print(f"Added {len(ARTICLES)} article summaries to data.js")


if __name__ == "__main__":
    main()
