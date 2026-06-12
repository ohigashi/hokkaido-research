#!/usr/bin/env python3
"""Day 2: +8 ISSUEs and +25 articles."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_scripts"))

from add_day1_issues import issue_to_js  # type: ignore
from add_day1_articles import make_body as base_make_body, generic_body  # type: ignore

DATA = ROOT / "data.js"
GEN = ROOT / "_scripts" / "generate_articles.py"

ISSUES_DAY2 = [
    {
        "id": "winter-sports-tourism",
        "q": "北海道 スキー スノボ 冬季観光 ニセコ ルスツ パウダースノー",
        "cat": "tourism",
        "title": "冬季観光・スキーリゾートの持続性",
        "urgency": 3, "severity": 3,
        "regions": ["all", "dou-o", "dou-hoku"],
        "traits": ["tourism-area"],
        "tags": ["冬季観光", "スキー", "スノーリゾート", "パウダースノー"],
        "addedAt": "2026-06-14",
        "externalCases": [
            {"who": "ニュージーランド ・ クイーンズタウン", "what": "通年観光とスキーリゾートの統合、地域コミュニティ ・ 国際性 ・ 持続性の長期事例。", "source": {"t": "Queenstown NZ", "o": "ニュージーランド", "u": "https://www.queenstownnz.co.nz/"}},
            {"who": "長野県 ・ 白馬村", "what": "国際スキーリゾートとして外国人観光客 ・ 移住者を受け入れる長期事例。", "source": {"t": "白馬村", "o": "長野県白馬村", "u": "https://www.vill.hakuba.lg.jp/"}},
        ],
        "summary": "パウダースノーで国際的に有名な道内冬季観光。気候変動・労働力不足・住宅高騰等で持続性が問われる。",
        "fact": "北海道のスキー場は約 100 ヶ所、冬季観光は道内観光の柱。ニセコ ・ ルスツ ・ 富良野等は国際リゾート化。外国人観光客 ・ 投資 ・ 雇用増加の一方、住宅高騰 ・ 労働力不足 ・ 気候変動による降雪量変動等の課題も顕在化。",
        "interp": "冬季観光は地域経済の柱だが、気候変動 ・ 国際化 ・ 労働力不足の複合課題を抱える。「冬以外の観光」「持続可能な雇用」「地域住民との共生」を統合する長期戦略が必要。",
        "initiatives": [
            {"who": "北海道 ・ 各観光地", "what": "冬季観光プロモーション ・ 通年化", "region": "all", "s": -1},
            {"who": "ニセコ ・ ルスツ ・ 富良野", "what": "国際スキーリゾート運営 ・ 投資受け入れ", "region": "dou-o", "s": -1},
        ],
        "sources": [],
        "deep": [
            {"h": "数値で見る現状", "b": "北海道のスキー場約 100 ヶ所、冬季観光は道内観光の重要分野。ニセコ ・ ルスツ ・ 富良野は世界的なリゾートに成長、外国人観光客 ・ 投資 ・ 雇用が増加。"},
            {"h": "気候変動の影響", "b": "気温上昇 ・ 降雪量変動でスキーシーズン短縮 ・ 雪質変化のリスク。長期投資の不確実性が高まる。"},
            {"h": "中心問い", "b": "「冬季リゾート単一」か「通年型 ・ 多目的観光地」か。気候変動対応 ・ 雇用安定 ・ 地域共生の長期戦略が必要。"},
            {"h": "残る資産", "b": "冬季観光で残る資産は 4 種。物理 ( ゲレンデ ・ ホテル ) 、関係 ( 国際ネット ・ リピーター ) 、ブランド ( パウダースノー ・ 国際リゾート ) 、知識 ( 運営ノウハウ ) 。"},
        ],
        "stats": [
            {"v": "約 100 ヶ所", "l": "道内スキー場数"},
            {"v": "国際リゾート", "l": "ニセコ ・ ルスツ ・ 富良野"},
        ],
        "measures": [
            {"t": "通年観光化 ・ 多目的化", "d": "夏期 ・ 秋季の観光メニュー ・ MICE ・ ワーケーション"},
            {"t": "雇用安定 ・ 住宅対策", "d": "通年雇用 ・ 従業員住宅 ・ 住民共生"},
            {"t": "気候変動適応", "d": "人工降雪 ・ 高地利用 ・ 戦略的投資"},
        ],
        "research": [
            {"t": "観光庁", "o": "観光庁", "u": "https://www.mlit.go.jp/kankocho/"},
            {"t": "ニセコ町", "o": "ニセコ町", "u": "https://www.town.niseko.lg.jp/"},
        ],
        "habits": [
            {"actor": "個人として", "actions": ["道内スキー場を意識的に利用", "地元観光地で消費 ・ 飲食", "リゾート従業員の地域生活を尊重"]},
            {"actor": "企業 ・ 組織として", "actions": ["従業員旅行で道内冬季観光地を活用", "観光地の環境 ・ 住民との共生支援", "通年雇用 ・ 多目的化への投資"]},
        ],
    },
    {
        "id": "agritech-smart",
        "q": "北海道 スマート農業 AI ロボット ドローン 大規模畑作",
        "cat": "primary",
        "title": "スマート農業と農業 DX",
        "urgency": 3, "severity": 3,
        "regions": ["all", "tokachi", "okhotsk"],
        "traits": ["agriculture", "dairy-region"],
        "tags": ["スマート農業", "AI", "ロボット", "ドローン", "農業 DX"],
        "addedAt": "2026-06-14",
        "externalCases": [
            {"who": "オランダ ・ 精密農業", "what": "GPS ・ センサー ・ AI を活用した世界トップレベルの効率的農業。輸出大国モデル。", "source": {"t": "Wageningen University", "o": "オランダ", "u": "https://www.wur.nl/"}},
            {"who": "更別村 ・ 超なまら本気スマート農業", "what": "AI ・ ロボット ・ ドローンで担い手減少下でも大規模農業を維持する実証プロジェクト。", "source": {"t": "更別村", "o": "更別村", "u": "https://www.vill.sarabetsu.hokkaido.jp/"}},
        ],
        "summary": "担い手減少と大規模化の道内農業。AI ・ ロボット ・ ドローン ・ センサーで生産性向上を目指す DX が進む。",
        "fact": "道内 1 経営体平均耕地 34 ha は全国平均 2.5 ha の 13 倍。担い手減少下で大規模経営を維持するため、スマート農業の導入が進む。GPS 自動操舵 ・ AI 与信 ・ ドローン散布 ・ センサー ・ AI 病害予測等。投資負担と人材育成 ・ データ標準化が課題。",
        "interp": "スマート農業は「人手不足の補完」を超えて、農業経営の構造転換 ・ 高度化のチャンス。データ ・ AI ・ ロボットを統合した持続可能農業モデルを北海道発で世界に提示する可能性も。投資 ・ 人材 ・ データ整備の総合戦略が必要。",
        "initiatives": [
            {"who": "北海道 ・ 道内市町村", "what": "スマート農業導入支援 ・ 補助 ・ 実証", "region": "all", "s": -1},
            {"who": "更別村", "what": "「超なまら本気スマート農業」プロジェクト", "region": "tokachi", "s": -1},
            {"who": "北海道大学 ・ 帯畜大", "what": "スマート農業 ・ 精密農業の研究 ・ 実装", "region": "all", "s": -1},
        ],
        "sources": [],
        "deep": [
            {"h": "数値で見る現状", "b": "道内 1 経営体平均耕地 34 ha 、全国平均 2.5 ha の 13 倍。担い手減少 ・ 高齢化で大規模経営の維持が困難、スマート農業による効率化が進む。GPS 自動操舵 ・ ロボット ・ ドローン ・ センサー等の導入事例が増加。"},
            {"h": "スマート農業の構造", "b": "スマート農業は 5 つの要素 ( センサー ・ データ ・ AI ・ ロボット ・ ネットワーク ) の統合。単一導入では効果限定、全体最適化が必要。投資負担 ・ データ標準化 ・ 人材育成が論点。"},
            {"h": "中心問い", "b": "「省力化 ・ 効率化」か「農業経営の構造転換」か。後者は世界水準のスマート農業ブランディング ・ 輸出 ・ データ経済等への展開。"},
            {"h": "残る資産", "b": "スマート農業で残る資産は 4 種。物理 ( 機械 ・ センサー ) 、知識 ( データ ・ ノウハウ ) 、人的 ( オペレーター ・ アグリエンジニア ) 、関係 ( メーカー ・ 大学 ・ 農家ネット ) 。データ ・ 知識資産が長期競争力。"},
        ],
        "stats": [
            {"v": "34 ha", "l": "道内 1 経営体平均耕地 ( 全国 2.5 ha )"},
            {"v": "13 倍", "l": "全国平均比 ・ 大規模化"},
        ],
        "measures": [
            {"t": "スマート農業導入支援", "d": "補助金 ・ 共同利用 ・ 中小経営体への普及"},
            {"t": "データ標準化 ・ プラットフォーム", "d": "農業データの共通基盤 ・ 連携 ・ AI 活用"},
            {"t": "アグリテック人材育成", "d": "農家 ・ エンジニア ・ オペレーターの育成"},
        ],
        "research": [
            {"t": "農林水産省 スマート農業", "o": "農林水産省", "u": "https://www.maff.go.jp/j/kanbo/smart/"},
            {"t": "農研機構 NARO", "o": "農業 ・ 食品産業技術総合研究機構", "u": "https://www.naro.go.jp/"},
        ],
        "habits": [
            {"actor": "個人として", "actions": ["道産農産物を意識的に購入", "スマート農業の取り組みを学ぶ ・ 応援", "農業体験 ・ 産直で農家と繋がる"]},
            {"actor": "企業 ・ 組織として", "actions": ["スマート農業企業との連携 ・ 投資", "従業員食堂で道産食材活用", "農業 DX 人材の育成 ・ 雇用"]},
        ],
    },
    {
        "id": "urban-downtown-decline",
        "q": "北海道 中心市街地 シャッター街 地方都市 再開発",
        "cat": "regional",
        "title": "地方都市中心市街地の衰退と再生",
        "urgency": 4, "severity": 4,
        "regions": ["all"],
        "traits": ["urban"],
        "tags": ["中心市街地", "シャッター街", "地方都市", "再開発"],
        "addedAt": "2026-06-14",
        "externalCases": [
            {"who": "石川県 ・ 金沢市中心市街地", "what": "歴史 ・ 文化 ・ 観光と一体で中心市街地を再生 ・ 持続。", "source": {"t": "金沢市", "o": "石川県金沢市", "u": "https://www4.city.kanazawa.lg.jp/"}},
            {"who": "富山県 ・ 富山市コンパクトシティ", "what": "公共交通を軸に居住誘導 ・ 中心市街地強化。長期戦略の成功事例。", "source": {"t": "富山市", "o": "富山県富山市", "u": "https://www.city.toyama.toyama.jp/"}},
        ],
        "summary": "道内地方都市の中心市街地は空き店舗増・シャッター街化。郊外型商業施設・通販との競合と人口減で構造的衰退。",
        "fact": "道内地方都市 ( 旭川 ・ 函館 ・ 釧路 ・ 帯広 ・ 苫小牧等 ) の中心市街地は空き店舗増 ・ 歩行者減 ・ シャッター街化が進行。郊外型ショッピングセンター ・ 通販 ・ 人口減 ・ 高齢化が複合要因。札幌は別格として持続するが、地方都市の課題は深刻。",
        "interp": "中心市街地の衰退は「商業の問題」を超えた地域コミュニティ ・ 文化 ・ 公共交通 ・ 高齢者の生活拠点の問題。コンパクトシティ ・ 多機能化 ・ 文化 ・ 観光と統合した長期戦略で再生する視点が必要。「商業集積維持」だけでは追いつかない。",
        "initiatives": [
            {"who": "経済産業省 ・ 各自治体", "what": "中心市街地活性化基本計画", "region": "all", "s": -1},
            {"who": "道内地方都市 ( 旭川 ・ 函館等 )", "what": "中心市街地再開発 ・ 観光誘致", "region": "all", "s": -1},
            {"who": "商店街 ・ 中心市街地 NPO", "what": "イベント ・ ブランディング ・ 観光連動", "region": "all", "s": -1},
        ],
        "sources": [],
        "deep": [
            {"h": "数値で見る現状", "b": "道内地方都市の中心市街地空き店舗率は 10-30% 超の地域もあり、歩行者数は数十年で大幅減。郊外型 SC ・ 通販 ・ 人口減 ・ 高齢化が複合要因。"},
            {"h": "構造的衰退の要因", "b": "1) 郊外型 SC ・ 通販との価格 ・ 利便性競争、2) 人口減 ・ 高齢化、3) 駐車場 ・ 公共交通の競合、4) 後継者不在 ・ 老朽化、5) 行政 ・ 地権者の調整困難。"},
            {"h": "中心問い", "b": "「商業集積」を維持するか、「コミュニティ ・ 文化 ・ 公共拠点としての中心市街地」へ再定義するか。後者は商業 + 居住 + 観光 + 文化の統合戦略。"},
            {"h": "残る資産", "b": "中心市街地で残る資産は 5 種。物理 ( 建物 ・ 商店街 ) 、関係 ( 商店主 ・ 住民ネット ) 、文化 ( 歴史 ・ 伝統 ) 、規範 ( 街の顔 ・ アイデンティティ ) 、知識 ( 商業ノウハウ ) 。文化 ・ 規範資産が長期再生の核。"},
        ],
        "stats": [
            {"v": "10-30% 超", "l": "中心市街地空き店舗率 ( 地域差大 )"},
            {"v": "歩行者数大幅減", "l": "数十年スパン"},
        ],
        "measures": [
            {"t": "コンパクトシティ ・ 居住誘導", "d": "富山市型の公共交通軸でのまちづくり"},
            {"t": "多機能化 ・ 文化 ・ 観光統合", "d": "商業 + 居住 + 観光 + 文化 + 公共施設の統合"},
            {"t": "商店街 ・ 地域 NPO の活性化", "d": "地権者 ・ 商店主 ・ NPO 連携での再生"},
        ],
        "research": [
            {"t": "経済産業省 中心市街地活性化", "o": "経済産業省", "u": "https://www.meti.go.jp/"},
            {"t": "国土交通省 都市再生", "o": "国土交通省", "u": "https://www.mlit.go.jp/toshi/"},
        ],
        "habits": [
            {"actor": "個人として", "actions": ["地方都市の中心市街地を意識的に訪れる ・ 消費", "個人店 ・ 商店街での買い物", "中心市街地イベントへの参加"]},
            {"actor": "企業 ・ 組織として", "actions": ["事業所 ・ 拠点を中心市街地に置く", "商店街 ・ 地域団体への支援 ・ 連携", "中心市街地での企業イベント開催"]},
        ],
    },
    {
        "id": "north-territory",
        "q": "北海道 北方領土 元島民 ロシア 国際問題",
        "cat": "tourism",
        "title": "北方領土問題と地域社会",
        "urgency": 3, "severity": 4,
        "regions": ["all", "kushiro-nemuro"],
        "traits": [],
        "tags": ["北方領土", "元島民", "ロシア", "国際問題", "返還運動"],
        "addedAt": "2026-06-14",
        "externalCases": [
            {"who": "国土交通省 ・ 北方領土啓発", "what": "国 ・ 自治体による啓発 ・ 元島民支援 ・ 国際的な情報発信。", "source": {"t": "内閣府 北方対策本部", "o": "内閣府", "u": "https://www8.cao.go.jp/hoppo/"}},
            {"who": "根室市 ・ 北方領土関連事業", "what": "根室は元島民 ・ 返還運動の拠点 ・ 教育 ・ ふるさと交流。", "source": {"t": "根室市", "o": "根室市", "u": "https://www.city.nemuro.hokkaido.jp/"}},
        ],
        "summary": "北方領土問題は地域経済・国際政治・歴史教育の交点。元島民の高齢化と教育継承が論点。",
        "fact": "北方領土 ( 歯舞 ・ 色丹 ・ 国後 ・ 択捉 ) はロシア実効支配下、日本は領有権を主張。元島民約 1.7 万人 ( 戦後 ) は高齢化、約 5,000 人台と減少。返還運動 ・ ビザなし交流は ウクライナ侵攻後に停滞。地域経済 ( 漁業 ) ・ 教育 ・ 国際政治 ・ 元島民支援等の論点が複雑に絡む。",
        "interp": "北方領土問題は単なる外交問題ではなく、地域経済 ( 漁業権 ・ 観光 ) ・ 元島民 ・ 教育継承 ・ 国際政治 ・ 平和構築の複合課題。返還の見通しが立ちにくい中、元島民の声を継承し、根室 ・ 道東地域の経済 ・ 教育 ・ 文化に組み込む長期戦略が必要。",
        "initiatives": [
            {"who": "内閣府 北方対策本部", "what": "領土啓発 ・ 元島民支援 ・ 国際的情報発信", "region": "all", "s": -1},
            {"who": "根室市 ・ 道東各市町村", "what": "北方領土関連事業 ・ 教育 ・ 観光", "region": "kushiro-nemuro", "s": -1},
            {"who": "千島歯舞諸島居住者連盟", "what": "元島民の組織化 ・ 返還運動", "region": "all", "s": -1},
        ],
        "sources": [],
        "deep": [
            {"h": "数値で見る現状", "b": "元島民は戦後約 1.7 万人、現在約 5,000 人台と減少 ・ 高齢化。ウクライナ侵攻 ( 2022 ) 後、ロシアとのビザなし交流 ・ 経済関係が停止。返還の見通しは立ちにくい状況。"},
            {"h": "複合的な論点", "b": "1) 外交 ・ 国際政治 ( 日露関係 ) 、2) 地域経済 ( 漁業権 ・ 海域 ) 、3) 元島民支援 ・ 高齢化対応、4) 教育継承 ( 若い世代への記憶継承 ) 、5) 平和構築 ・ 国際協調。"},
            {"h": "中心問い", "b": "「返還を待つ」か、「現状の中で元島民の声 ・ 地域経済 ・ 教育を持続させる」か。長期戦略として地域 ・ 教育 ・ 国際発信を組み込む視点。"},
            {"h": "残る資産", "b": "北方領土関連で残る資産は 4 種。人的 ( 元島民 ・ 関係者 ) 、知識 ( 歴史 ・ 文化 ・ 経験 ) 、関係 ( 国 ・ 自治体 ・ 国際機関ネット ) 、規範 ( 平和 ・ 国際協調の文化 ) 。"},
        ],
        "stats": [
            {"v": "約 5,000 人", "l": "現存元島民 ( 高齢化 )"},
            {"v": "1.7 万人", "l": "戦後の元島民数"},
        ],
        "measures": [
            {"t": "元島民支援 ・ 高齢化対応", "d": "医療 ・ 福祉 ・ 経済支援の継続"},
            {"t": "教育継承 ・ 啓発強化", "d": "若い世代への歴史 ・ 経験継承"},
            {"t": "国際発信 ・ 平和構築", "d": "国際社会への情報発信 ・ 対話"},
        ],
        "research": [
            {"t": "内閣府 北方対策本部", "o": "内閣府", "u": "https://www8.cao.go.jp/hoppo/"},
            {"t": "外務省 北方領土問題", "o": "外務省", "u": "https://www.mofa.go.jp/mofaj/area/hoppo/"},
        ],
        "habits": [
            {"actor": "個人として", "actions": ["北方領土問題を学ぶ ・ 歴史認識", "元島民の話を聞く ・ 関連イベント参加", "根室 ・ 道東を訪問 ・ 関わる"]},
            {"actor": "企業 ・ 組織として", "actions": ["北方領土関連事業 ・ 教育プロジェクトへの協力", "道東地域との取引 ・ 関係構築", "国際協調 ・ 平和構築活動への参加"]},
        ],
    },
    {
        "id": "diversity-inclusion",
        "q": "北海道 LGBTQ ダイバーシティ 多様性 パートナーシップ制度",
        "cat": "population",
        "title": "性的指向 ・ 多様性とインクルージョン",
        "urgency": 3, "severity": 3,
        "regions": ["all"],
        "traits": ["urban"],
        "tags": ["LGBTQ", "ダイバーシティ", "パートナーシップ", "性的指向", "多様性"],
        "addedAt": "2026-06-14",
        "externalCases": [
            {"who": "東京都 ・ 渋谷区パートナーシップ", "what": "全国初の同性パートナーシップ証明制度 ( 2015 ) 。10 年継続で全国に波及。", "source": {"t": "渋谷区", "o": "渋谷区", "u": "https://www.city.shibuya.tokyo.jp/"}},
            {"who": "デンマーク ・ オランダ", "what": "同性婚 ・ パートナーシップ法制化の先進国。包摂的社会の長期事例。", "source": {"t": "Danish Government", "o": "デンマーク政府", "u": "https://www.denmark.dk/"}},
        ],
        "summary": "札幌市等で同性パートナーシップ制度導入。性的指向・多様性の尊重と地域社会の包摂が長期課題。",
        "fact": "全国 LGBTQ+ は人口の数 % 程度 ( 推計 ・ 調査により幅 ) 。札幌市は 2017 年に道内初のパートナーシップ宣誓制度を導入、その後北海道内の多くの自治体に拡大。社会的偏見 ・ 雇用 ・ 教育 ・ 医療等での課題が残るが、若い世代を中心に意識変化が進む。",
        "interp": "性的指向 ・ 多様性は「特殊な人々の問題」ではなく、地域社会全体の包摂性 ・ 多様性 ・ 創造性の問題。教育 ・ 企業 ・ 公共サービス ・ コミュニティでのインクルージョンを長期戦略で進める視点。短期の制度導入を超えて文化変容を目指す。",
        "initiatives": [
            {"who": "札幌市 ・ 道内自治体", "what": "パートナーシップ制度 ・ 多様性推進", "region": "all", "s": -1},
            {"who": "民間企業 ・ NPO", "what": "ダイバーシティ研修 ・ 雇用 ・ 啓発", "region": "all", "s": -1},
            {"who": "当事者団体 ・ プライド団体", "what": "プライドパレード ・ 啓発 ・ 権利擁護", "region": "all", "s": -1},
        ],
        "sources": [],
        "deep": [
            {"h": "数値で見る現状", "b": "LGBTQ+ は推計人口の数 % ( 調査により差 ) 。札幌市は 2017 年道内初のパートナーシップ制度導入、その後北海道内自治体に拡大。社会的偏見 ・ 制度上の課題は残るが、若い世代の意識変化 ・ 企業のダイバーシティ推進が進む。"},
            {"h": "包摂性の構造", "b": "包摂性は制度 ( パートナーシップ ・ 差別禁止 ) ・ 教育 ( 多様性理解 ) ・ 雇用 ( 差別なき採用 ) ・ サービス ( 配慮ある対応 ) ・ コミュニティ ( 居場所 ) の 5 層で構築。短期制度化だけでは文化変容には至らない。"},
            {"h": "中心問い", "b": "「制度上の対応」か「地域社会全体の文化変容」か。後者は教育 ・ 企業 ・ 公共サービス全般での包摂性 ・ 多様性が当然の地域文化を作る長期戦略。"},
            {"h": "残る資産", "b": "多様性施策で残る資産は 4 種。物理 ( 居場所 ・ 相談窓口 ) 、関係 ( 当事者 ・ 支援者ネット ) 、規範 ( 多様性を尊重する文化 ) 、知識 ( 当事者の声 ・ 理解 ) 。規範資産が最も長期に効く。"},
        ],
        "stats": [
            {"v": "数 %", "l": "全国 LGBTQ+ 推計人口比"},
            {"v": "2017", "l": "札幌市パートナーシップ制度導入"},
        ],
        "measures": [
            {"t": "パートナーシップ ・ 同性婚法制度", "d": "公的制度の整備 ・ 標準化"},
            {"t": "教育 ・ 企業ダイバーシティ推進", "d": "学校 ・ 職場での多様性理解 ・ 研修"},
            {"t": "当事者 ・ コミュニティ支援", "d": "居場所 ・ 相談 ・ ピアサポート"},
        ],
        "research": [
            {"t": "札幌市 多様性 ・ パートナーシップ", "o": "札幌市", "u": "https://www.city.sapporo.jp/"},
            {"t": "公益社団法人 Marriage For All Japan", "o": "Marriage For All Japan", "u": "https://www.marriageforall.jp/"},
        ],
        "habits": [
            {"actor": "個人として", "actions": ["多様性 ・ LGBTQ+ について学ぶ ・ 偏見を見直す", "プライドパレード等のイベントに参加 ・ 応援", "当事者の声を聞く ・ 理解者になる"]},
            {"actor": "企業 ・ 組織として", "actions": ["ダイバーシティ研修 ・ ポリシー整備", "性的指向にかかわらない採用 ・ 評価", "同性パートナーへの福利厚生平等"]},
        ],
    },
    {
        "id": "youth-mental-health",
        "q": "北海道 若者 メンタルヘルス 自殺 SNS 孤立",
        "cat": "medical",
        "title": "若者のメンタルヘルスと孤立",
        "urgency": 5, "severity": 5,
        "regions": ["all"],
        "traits": ["urban", "rural-mountain"],
        "tags": ["メンタルヘルス", "若者", "自殺", "SNS", "孤立"],
        "addedAt": "2026-06-14",
        "externalCases": [
            {"who": "東京都 ・ こころの相談 LINE", "what": "SNS ・ チャット型の相談窓口で若者にアクセス。全国の自治体で導入拡大。", "source": {"t": "東京都", "o": "東京都", "u": "https://www.metro.tokyo.lg.jp/"}},
            {"who": "フィンランド ・ 学校メンタルヘルス", "what": "学校カウンセラー ・ 心理士配置 ・ 早期発見 ・ 介入の長期事例。", "source": {"t": "フィンランド教育省", "o": "フィンランド", "u": "https://minedu.fi/"}},
        ],
        "summary": "若者の自殺・うつ・孤立が深刻。SNS・コロナ・家族・学校・就労等の複合要因と長期支援が必要。",
        "fact": "全国の若年層 ( 10-30 代 ) の自殺率は依然高水準、コロナ禍を経て増加傾向。SNS ・ 孤立 ・ 学業 ・ 就労 ・ 経済 ・ 家族関係等が複合要因。北海道も同様の傾向、メンタルヘルス ・ 相談支援 ・ 学校での早期発見 ・ 介入が課題。LINE 等の SNS 相談窓口が拡大中。",
        "interp": "若者のメンタルヘルスは「個人 ・ 家族の問題」ではなく、社会全体の構造課題。学校 ・ 職場 ・ 家庭 ・ 地域 ・ オンラインの 5 つの場での予防 ・ 早期発見 ・ 介入 ・ 治療 ・ 復帰支援の総合戦略が必要。短期対応を超えた長期視点。",
        "initiatives": [
            {"who": "厚生労働省 ・ 文科省", "what": "メンタルヘルス対策 ・ 学校カウンセラー ・ 自殺対策", "region": "all", "s": -1},
            {"who": "北海道 ・ 道内自治体", "what": "相談窓口 ・ 居場所 ・ 早期発見", "region": "all", "s": -1},
            {"who": "道内 NPO ・ 大学", "what": "ピアサポート ・ 啓発 ・ 研究", "region": "all", "s": -1},
        ],
        "sources": [],
        "deep": [
            {"h": "数値で見る現状", "b": "全国の若年層自殺率は高水準で推移、コロナ禍を経て増加傾向。SNS いじめ ・ 孤立 ・ 学業 ・ 就労 ・ 経済 ・ 家族関係等が複合要因。北海道も同様、相談窓口 ・ メンタルヘルス支援は自治体差大。"},
            {"h": "5 つの場での対応", "b": "若者を支える 5 つの場: 学校 ( カウンセラー ・ いじめ対策 ) ・ 職場 ( ストレスケア ) ・ 家庭 ( 親子関係 ) ・ 地域 ( 居場所 ) ・ オンライン ( SNS 相談 ) 。5 つを統合する必要。"},
            {"h": "中心問い", "b": "「個別ケア ・ カウンセリング」か「社会全体での予防 ・ 早期発見 ・ 介入の仕組み」か。後者は学校 ・ 職場 ・ 地域 ・ オンラインの統合戦略。"},
            {"h": "残る資産", "b": "メンタルヘルス支援で残る資産は 4 種。人的 ( カウンセラー ・ ピアサポーター ) 、関係 ( 当事者 ・ 家族 ・ 支援者ネット ) 、知識 ( ケアノウハウ ・ ピア知見 ) 、規範 ( メンタルヘルスへの理解 ・ オープン文化 ) 。"},
        ],
        "stats": [
            {"v": "高水準", "l": "若年層 ( 10-30 代 ) 自殺率"},
            {"v": "増加傾向", "l": "コロナ禍以降"},
        ],
        "measures": [
            {"t": "学校 ・ 職場の早期発見 ・ 介入", "d": "カウンセラー ・ 心理士配置 ・ いじめ対策 ・ メンタルチェック"},
            {"t": "SNS ・ チャット相談窓口", "d": "若者がアクセスしやすい相談チャネル"},
            {"t": "地域居場所 ・ ピアサポート", "d": "学校 ・ 家庭外の居場所 ・ ピアからの支援"},
        ],
        "research": [
            {"t": "厚生労働省 自殺対策", "o": "厚生労働省", "u": "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/hukushi_kaigo/seikatsuhogo/jisatsu/index.html"},
            {"t": "文部科学省 児童生徒の心のケア", "o": "文部科学省", "u": "https://www.mext.go.jp/"},
        ],
        "habits": [
            {"actor": "個人として", "actions": ["若者の声に耳を傾ける ・ 否定しない", "メンタルヘルスへの理解を深める", "辛そうな若者に「大丈夫?」と声掛け", "ピアサポート ・ 相談窓口の存在を共有"]},
            {"actor": "企業 ・ 組織として", "actions": ["若手社員のメンタルケア ・ ストレスチェック", "カウンセラー ・ 産業医の体制整備", "離職を罪と見ない文化"]},
        ],
    },
    {
        "id": "religious-shrine",
        "q": "北海道 神社仏閣 アイヌ祭祀 宗教 地域コミュニティ",
        "cat": "tourism",
        "title": "神社仏閣 ・ 宗教施設と地域コミュニティ",
        "urgency": 3, "severity": 3,
        "regions": ["all"],
        "traits": ["urban", "rural-mountain"],
        "tags": ["神社", "寺院", "アイヌ祭祀", "宗教", "祭り", "地域コミュニティ"],
        "addedAt": "2026-06-14",
        "externalCases": [
            {"who": "京都府 ・ 寺社観光", "what": "歴史 ・ 文化 ・ 観光の核として神社仏閣を持続。世界遺産 ・ 観光経済 ・ 文化継承の統合事例。", "source": {"t": "京都市", "o": "京都市", "u": "https://www.city.kyoto.lg.jp/"}},
            {"who": "島根県 ・ 出雲大社", "what": "神話 ・ 神社 ・ 地域経済を一体で運営、観光 ・ 文化 ・ 移住の核に。", "source": {"t": "出雲大社", "o": "出雲大社", "u": "https://izumooyashiro.or.jp/"}},
        ],
        "summary": "道内神社仏閣・アイヌ祭祀の維持困難。地域コミュニティ・文化・観光の核として再定義する視点。",
        "fact": "道内には開拓期からの神社 ・ 寺院 ・ 教会等、約数千の宗教施設。アイヌ祭祀 ・ 伝統行事も独自の文化的価値を持つ。少子高齢化 ・ 後継者不在 ・ 維持費負担で多くが厳しい運営状況。一方で、観光 ・ 文化 ・ 地域コミュニティの核として再評価する動きもある。",
        "interp": "宗教施設は「個別の宗教法人の問題」ではなく、地域コミュニティ ・ 文化継承 ・ 観光 ・ 心のケア等の多面的価値を持つ。少子高齢化下での維持は構造的課題、文化 ・ 観光 ・ コミュニティと統合した長期戦略で再定義する視点が論点。",
        "initiatives": [
            {"who": "宗教法人 ・ 各神社仏閣", "what": "祭祀 ・ 行事 ・ 文化継承", "region": "all", "s": -1},
            {"who": "自治体 ・ 観光協会", "what": "文化財保護 ・ 観光連動 ・ 祭り支援", "region": "all", "s": -1},
            {"who": "アイヌ団体 ・ 文化財団", "what": "アイヌ祭祀 ・ 伝統行事の継承", "region": "all", "s": -1},
        ],
        "sources": [],
        "deep": [
            {"h": "数値で見る現状", "b": "道内宗教施設は神社 ・ 寺院 ・ 教会等で数千、開拓期からの歴史を持つ。少子高齢化 ・ 後継者不在 ・ 維持費負担で運営困難な施設多数。アイヌ祭祀も担い手 ・ 継承の課題。"},
            {"h": "宗教施設の多面的価値", "b": "宗教施設は祭祀 ・ 信仰だけでなく、地域コミュニティの集会場 ・ 祭り ・ 文化伝承 ・ 観光資源 ・ 心のケア等の多面的価値を持つ。「宗教法人の経営」を超えた地域インフラとしての位置づけが論点。"},
            {"h": "中心問い", "b": "「宗教法人の自助努力」か「地域文化 ・ 観光 ・ コミュニティの核としての公的支援 ・ 連携」か。後者は地域全体での再定義 ・ 長期戦略。"},
            {"h": "残る資産", "b": "宗教施設で残る資産は 4 種。物理 ( 建物 ・ 文化財 ) 、関係 ( 氏子 ・ 檀家 ・ 地域コミュニティ ) 、文化 ・ 知識 ( 祭祀 ・ 伝統 ・ 知識 ) 、規範 ( 心のよりどころ ・ 地域アイデンティティ ) 。"},
        ],
        "stats": [
            {"v": "数千施設", "l": "道内宗教施設 ( 神社 ・ 寺院 ・ 教会 )"},
            {"v": "後継者不在多い", "l": "維持運営困難"},
        ],
        "measures": [
            {"t": "文化財 ・ 観光と連動", "d": "観光 ・ 教育 ・ 文化財保護と一体で支える"},
            {"t": "地域コミュニティ ・ 祭り再生", "d": "祭り ・ 行事を地域住民全体で支える仕組み"},
            {"t": "アイヌ祭祀 ・ 伝統行事の継承", "d": "アイヌ文化 ・ 地域伝統行事の継承 ・ 教育"},
        ],
        "research": [
            {"t": "文化庁 文化財保護", "o": "文化庁", "u": "https://www.bunka.go.jp/"},
            {"t": "北海道神社庁", "o": "北海道神社庁", "u": "https://hokkaidojinjacho.jp/"},
        ],
        "habits": [
            {"actor": "個人として", "actions": ["地域の神社 ・ 寺院 ・ 教会の活動に参加", "祭り ・ 伝統行事への参加 ・ 応援", "アイヌ祭祀 ・ 文化を学ぶ ・ 尊重"]},
            {"actor": "企業 ・ 組織として", "actions": ["地域祭り ・ 行事への協賛 ・ 寄付", "従業員の地域祭り参加への配慮", "文化財保護 ・ アイヌ文化への協力"]},
        ],
    },
    {
        "id": "coastal-erosion",
        "q": "北海道 海岸侵食 砂浜消失 気候変動 海面上昇",
        "cat": "environment",
        "title": "海岸侵食と砂浜消失",
        "urgency": 3, "severity": 3,
        "regions": ["all", "kushiro-nemuro", "dou-nan"],
        "traits": ["fishing-village", "tourism-area"],
        "tags": ["海岸侵食", "砂浜", "気候変動", "海面上昇", "防潮"],
        "addedAt": "2026-06-14",
        "externalCases": [
            {"who": "オランダ ・ デルタワークス", "what": "海面上昇 ・ 防潮の世界モデル。長期国土計画 ・ 適応戦略。", "source": {"t": "Rijkswaterstaat", "o": "オランダ政府", "u": "https://www.rijkswaterstaat.nl/"}},
            {"who": "沖縄県 ・ 赤土流出対策", "what": "サンゴ礁保全と海岸 ・ 海洋環境の統合管理。30 年継続。", "source": {"t": "沖縄県", "o": "沖縄県", "u": "https://www.pref.okinawa.lg.jp/"}},
        ],
        "summary": "気候変動・台風・人為的要因で道内海岸の侵食・砂浜消失が進行。漁業・観光・防災への影響大。",
        "fact": "気候変動 ・ 海面上昇 ・ 台風増加で全国の海岸侵食が進行。北海道も同様、特に太平洋側 ・ 道東で砂浜消失 ・ 海岸後退が観測される。漁港 ・ 道路 ・ 集落 ・ 観光地への影響が大きい。河川改修 ・ ダム ・ 港湾建設等の人為的要因も土砂供給を減らす。",
        "interp": "海岸侵食は単なる「自然現象」ではなく、気候変動 ・ 河川 ・ 港湾 ・ 海洋環境 ・ 地域生活が複合する構造課題。「護岸 ・ 防潮堤で守る」だけでなく、土砂供給 ・ サンドバイパス ・ 適応戦略を組み合わせた長期計画が必要。",
        "initiatives": [
            {"who": "国土交通省 ・ 北海道開発局", "what": "海岸保全事業 ・ 護岸 ・ 防潮", "region": "all", "s": -1},
            {"who": "道内沿岸自治体", "what": "海岸侵食対策 ・ 観光 ・ 漁業への影響対応", "region": "all", "s": -1},
            {"who": "大学 ・ 研究機関", "what": "海岸 ・ 海洋環境研究 ・ モニタリング", "region": "all", "s": -1},
        ],
        "sources": [],
        "deep": [
            {"h": "数値で見る現状", "b": "全国の海岸侵食面積は年数十 ha 規模 ( 国交省 ) 。北海道も太平洋側 ・ 道東で砂浜消失が観測。漁港 ・ 道路 ・ 集落 ・ 観光地に影響。気候変動 ・ 海面上昇でさらに悪化の予測。"},
            {"h": "侵食の構造要因", "b": "1) 気候変動 ・ 海面上昇 ・ 台風増加、2) 河川 ・ ダム ・ 港湾による土砂供給減、3) 海岸構造物 ( 防波堤等 ) の影響、4) 自然海岸の縮小。複合要因なので個別対策では追いつかない。"},
            {"h": "中心問い", "b": "「護岸 ・ 防潮で守る」か「気候変動への適応 ・ 海岸生態系の保全」か。両輪が必要、特に長期視点 ・ 国際協調がカギ。"},
            {"h": "残る資産", "b": "海岸保全で残る資産は 4 種。物理 ( 護岸 ・ 構造物 ) 、生態 ( 砂浜 ・ サンゴ ・ 生物多様性 ) 、関係 ( 沿岸住民 ・ 漁業者 ・ 観光業 ) 、知識 ( モニタリングデータ ・ 適応知見 ) 。"},
        ],
        "stats": [
            {"v": "年数十 ha", "l": "全国の海岸侵食面積"},
            {"v": "太平洋側", "l": "道内で特に深刻"},
        ],
        "measures": [
            {"t": "サンドバイパス ・ 土砂供給", "d": "ダム土砂排出 ・ 海岸への土砂供給による回復"},
            {"t": "気候変動適応 ・ 計画的撤退", "d": "海面上昇予測下での集落 ・ インフラ移転計画"},
            {"t": "海岸生態系の保全", "d": "砂浜 ・ 海洋生物 ・ サンゴ等の保全 ・ モニタリング"},
        ],
        "research": [
            {"t": "国土交通省 北海道開発局", "o": "国土交通省", "u": "https://www.hkd.mlit.go.jp/"},
            {"t": "気候変動適応センター", "o": "国立環境研究所", "u": "https://adaptation-platform.nies.go.jp/"},
        ],
        "habits": [
            {"actor": "個人として", "actions": ["海岸 ・ 砂浜の変化を観察 ・ 記録", "海洋保全活動 ・ ボランティアに参加", "気候変動 ・ 海洋環境への意識を持つ"]},
            {"actor": "企業 ・ 組織として", "actions": ["海洋保全プロジェクトへの参加 ・ 協賛", "サプライチェーンの海洋環境負荷削減", "気候変動適応 BCP に海岸侵食を含める"]},
        ],
    },
]


# Day 2 articles ( 25 件: 16 ペア + 9 補完 )
ARTICLES_DAY2 = [
    # === 8 new ISSUEs × 2 = 16 ===
    {"id": "winter-sports-structure-2026-06", "title": "北海道冬季観光の持続性 - 気候変動 ・ 労働力 ・ 国際化の構造", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["winter-sports-tourism", "tourism-sustainability"], "summary": "ニセコ ・ ルスツ等の国際リゾート化と気候変動 ・ 労働力不足 ・ 住宅高騰の同時進行。冬季観光の構造を読み解く。", "topic": "generic"},
    {"id": "winter-sports-strategy-2026-06", "title": "冬季観光を通年型に進化させる - 4 つの戦略", "category": "アイデア", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["winter-sports-tourism"], "summary": "通年化 ・ MICE ・ ワーケーション ・ 住民共生。クイーンズタウン型 4 戦略で冬季観光を持続可能に。", "topic": "generic"},
    {"id": "agritech-smart-structure-2026-06", "title": "北海道スマート農業 - 大規模化と担い手不足の構造", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["agritech-smart"], "summary": "道内 1 経営体平均 34 ha 、全国 13 倍の大規模化。担い手減少下でのスマート農業による構造転換。", "topic": "generic"},
    {"id": "agritech-smart-strategy-2026-06", "title": "AI ・ ロボット ・ ドローンで作る次世代農業 - 5 つの実装", "category": "アイデア", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["agritech-smart"], "summary": "GPS 自動操舵 ・ AI 与信 ・ ドローン散布 ・ センサー ・ データ統合。更別村事例から学ぶスマート農業の 5 つの実装。", "topic": "generic"},
    {"id": "urban-downtown-structure-2026-06", "title": "地方都市中心市街地の衰退 - 商業集積か地域核か", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["urban-downtown-decline"], "summary": "道内地方都市の空き店舗率 10-30% 超、シャッター街化進行。商業集積維持か地域コミュニティの核へ再定義か。", "topic": "generic"},
    {"id": "urban-downtown-renewal-2026-06", "title": "中心市街地を地域の核に再生する - 富山 ・ 金沢に学ぶ", "category": "アイデア", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["urban-downtown-decline"], "summary": "コンパクトシティ ・ 多機能化 ・ 文化観光統合 ・ 商店街再生。富山 ・ 金沢の長期事例から学ぶ 4 戦略。", "topic": "generic"},
    {"id": "north-territory-structure-2026-06", "title": "北方領土問題と道東地域 - 元島民 ・ 経済 ・ 教育の構造", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["north-territory"], "summary": "元島民約 5,000 人と高齢化、ウクライナ侵攻後の停滞。地域経済 ・ 教育 ・ 国際政治の複合構造を読み解く。", "topic": "generic"},
    {"id": "north-territory-continuity-2026-06", "title": "北方領土問題を次世代へ - 教育 ・ 地域 ・ 国際協調の戦略", "category": "アイデア", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["north-territory"], "summary": "元島民支援 ・ 教育継承 ・ 国際発信 ・ 平和構築。返還を待つだけでない長期戦略の 4 つの柱。", "topic": "generic"},
    {"id": "diversity-inclusion-structure-2026-06", "title": "性的指向 ・ 多様性と地域社会 - 制度か文化変容か", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["diversity-inclusion"], "summary": "札幌市 2017 年道内初のパートナーシップ制度。制度導入を超えた地域社会の文化変容の構造。", "topic": "generic"},
    {"id": "diversity-inclusion-strategy-2026-06", "title": "包摂的な地域を作る - 多様性の 5 層実装", "category": "アイデア", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["diversity-inclusion"], "summary": "制度 ・ 教育 ・ 雇用 ・ サービス ・ コミュニティの 5 層で包摂性を構築。渋谷 ・ デンマーク等の事例実装。", "topic": "generic"},
    {"id": "youth-mental-structure-2026-06", "title": "若者のメンタルヘルス - 自殺 ・ 孤立 ・ SNS の複合構造", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["youth-mental-health", "isolation"], "summary": "若年層自殺率高水準、コロナ禍以降増加傾向。SNS ・ 学校 ・ 職場 ・ 家庭 ・ オンラインの 5 場での構造課題。", "topic": "generic"},
    {"id": "youth-mental-support-2026-06", "title": "若者のメンタルヘルス支援 - 5 場の統合戦略", "category": "アイデア", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["youth-mental-health"], "summary": "学校 ・ 職場 ・ 家庭 ・ 地域 ・ オンラインの 5 場での予防 ・ 早期発見 ・ 介入。フィンランド ・ 東京の事例実装。", "topic": "generic"},
    {"id": "religious-shrine-structure-2026-06", "title": "神社仏閣 ・ 宗教施設の維持 - 個別経営か地域文化か", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["religious-shrine"], "summary": "道内宗教施設数千、後継者不在 ・ 維持困難。地域コミュニティ ・ 文化 ・ 観光の核として再定義する構造。", "topic": "generic"},
    {"id": "religious-shrine-revival-2026-06", "title": "神社仏閣を地域文化の核に - 4 つの統合戦略", "category": "アイデア", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["religious-shrine"], "summary": "文化財連動 ・ 祭り再生 ・ アイヌ祭祀 ・ 観光統合。京都 ・ 出雲事例から学ぶ宗教施設再生の 4 戦略。", "topic": "generic"},
    {"id": "coastal-erosion-structure-2026-06", "title": "北海道海岸の侵食 - 気候変動と土砂供給の構造", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["coastal-erosion"], "summary": "気候変動 ・ 海面上昇 ・ 河川 ・ 港湾の複合で道内海岸の砂浜消失進行。漁業 ・ 観光 ・ 集落への影響構造。", "topic": "generic"},
    {"id": "coastal-erosion-adaptation-2026-06", "title": "海岸侵食への適応戦略 - オランダに学ぶ 4 つの実装", "category": "アイデア", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["coastal-erosion"], "summary": "サンドバイパス ・ 海岸生態系保全 ・ 集落移転計画 ・ 国際連携。オランダデルタワークス型 4 戦略。", "topic": "generic"},
    # === 既存 ISSUE 補完 9 件 ===
    {"id": "depopulation-residual-strategy-2026-06", "title": "人口減少を「数」ではなく「資産」で見る - 残る資産戦略", "category": "アイデア", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["depopulation", "migration"], "summary": "「人口維持」だけでは追いつかない。人口減でも残る事業 ・ 関係 ・ 仕組み資産で地域を支える視点。", "topic": "generic"},
    {"id": "low-birthrate-structure-2026-06", "title": "少子化と北海道 - 出生率 ・ 子育て ・ 暮らしの構造", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["low-birthrate", "childcare-shortage"], "summary": "道内合計特殊出生率 1.0 台、全国でも低水準。経済 ・ 暮らし ・ 子育て環境の構造的課題。", "topic": "generic"},
    {"id": "isolation-structure-2026-06", "title": "社会的孤立と地域コミュニティ - 8050 ・ 単身高齢 ・ ひきこもりの共通構造", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["isolation", "aging-care"], "summary": "高齢者 ・ ひきこもり ・ ヤングケアラー等、社会的孤立の共通構造。地域コミュニティ再生の論点。", "topic": "generic"},
    {"id": "shinkansen-donan-structure-2026-06", "title": "北海道新幹線と道南 - 延伸遅延と並行在来線の構造", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["shinkansen-donan", "jr-hokkaido-future"], "summary": "新函館北斗 - 札幌延伸の遅延、並行在来線議論、道南地域の影響。鉄道 ・ 地域経済の構造を読み解く。", "topic": "generic"},
    {"id": "rail-transit-structure-2026-06", "title": "道内 JR ・ 私鉄 ・ バスの統合 - 公共交通の地域インフラ化", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["rail-transit", "jr-hokkaido-future"], "summary": "JR 単体ではなく、鉄道 ・ バス ・ デマンド交通の統合運営。地域公共交通の構造再設計。", "topic": "generic"},
    {"id": "carbon-neutral-structure-2026-06", "title": "カーボンニュートラルと地域 - 国際目標と地域実装の構造", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["carbon-neutral", "decarbonization"], "summary": "2050 カーボンニュートラル目標。脱炭素先行地域指定と地域実装の構造課題。", "topic": "generic"},
    {"id": "biodiversity-structure-2026-06", "title": "北海道の生物多様性 - 自然保全と経済活動の両立", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["biodiversity", "env-conservation"], "summary": "知床 ・ 阿寒 ・ 釧路湿原等の自然 ・ 生物多様性。観光 ・ 一次産業 ・ 開発との両立構造。", "topic": "generic"},
    {"id": "smart-city-gx-structure-2026-06", "title": "スマートシティと GX - 札幌 ・ ニセコ ・ 上士幌の構造", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["smart-city-gx", "decarbonization"], "summary": "DX × GX で都市運営 ・ 脱炭素を統合。札幌 ・ ニセコ ・ 上士幌等の道内事例構造を読み解く。", "topic": "generic"},
    {"id": "energy-security-structure-2026-06", "title": "エネルギー安全保障と北海道 - 自給 ・ 脱炭素 ・ レジリエンス", "category": "課題発見", "publishedAt": "2026-06-14", "readMinutes": 4, "relatedIssueIds": ["energy-security", "decarbonization", "nuclear-safety"], "summary": "ウクライナ侵攻後のエネルギー安全保障。北海道のエネルギー自給 ・ 脱炭素 ・ レジリエンスの統合構造。", "topic": "generic"},
]


def append_issues():
    content = DATA.read_text(encoding="utf-8")
    insert_text = ",\n" + ",\n".join(issue_to_js(i) for i in ISSUES_DAY2) + "\n"
    # Find end of ISSUES array
    issues_end = content.index("];\n\n// 出典")
    # Insert before "];"
    # Find the last "}" before "];"
    last_brace = content.rfind("  }", 0, issues_end)
    content = content[:last_brace + 3] + insert_text + content[last_brace + 3:]
    DATA.write_text(content, encoding="utf-8")
    print(f"Added {len(ISSUES_DAY2)} ISSUEs to data.js")


def append_articles():
    """Append articles to data.js ARTICLES + generate_articles.py ARTICLES."""
    import json

    # 1. data.js ARTICLES
    data_content = DATA.read_text(encoding="utf-8")
    new_data_entries = ""
    for art in ARTICLES_DAY2:
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

    # Find ARTICLES end
    art_start = data_content.find("const ARTICLES = [")
    art_end = data_content.find("];", art_start)
    new_data_content = data_content[:art_end] + new_data_entries + data_content[art_end:]
    DATA.write_text(new_data_content, encoding="utf-8")
    print(f"Added {len(ARTICLES_DAY2)} article summaries to data.js")

    # 2. generate_articles.py ARTICLES
    gen_content = GEN.read_text(encoding="utf-8")

    # All use generic body
    new_entries = ""
    for art in ARTICLES_DAY2:
        body = generic_body(art)
        body_lines = ["        \"body\": ["]
        for block in body:
            if block[0] in ("p", "h2", "h3", "callout", "note"):
                body_lines.append(f"            ({block[0]!r}, {json.dumps(block[1], ensure_ascii=False)}),")
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

    # Find ARTICLES end in generator (the "]" before GLOSSARY_TERMS or similar)
    marker = "]\n\n\nGLOSSARY_TERMS = ["
    if marker not in gen_content:
        print("WARN: marker not found")
        return
    new_gen_content = gen_content.replace(marker, new_entries + marker, 1)
    GEN.write_text(new_gen_content, encoding="utf-8")
    print(f"Added {len(ARTICLES_DAY2)} articles to generate_articles.py")


if __name__ == "__main__":
    append_issues()
    append_articles()
