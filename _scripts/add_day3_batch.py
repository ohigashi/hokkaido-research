#!/usr/bin/env python3
"""Day 3: +6 ISSUEs + 28 articles."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_scripts"))

from add_day1_issues import issue_to_js  # type: ignore
from add_day1_articles import generic_body  # type: ignore

DATA = ROOT / "data.js"
GEN = ROOT / "_scripts" / "generate_articles.py"


def make_issue(id_, title, q, cat, urgency, severity, regions, traits, tags, summary, fact, interp, ext_cases, initiatives, deep_blocks, stats, measures, research, habits):
    return {
        "id": id_, "q": q, "cat": cat, "title": title,
        "urgency": urgency, "severity": severity,
        "regions": regions, "traits": traits, "tags": tags,
        "addedAt": "2026-06-15",
        "externalCases": ext_cases,
        "summary": summary, "fact": fact, "interp": interp,
        "initiatives": initiatives, "sources": [],
        "deep": deep_blocks, "stats": stats, "measures": measures, "research": research, "habits": habits,
    }


ISSUES_DAY3 = [
    make_issue(
        "food-security", "食料安全保障と地域", "北海道 食料安全保障 輸入依存 地産地消",
        "primary", 4, 4, ["all"], ["agriculture", "fishing-village"],
        ["食料安全保障", "輸入依存", "地産地消", "災害備蓄"],
        "食料自給率 220% の北海道は国の食料安全保障の要。輸入依存・気候変動・地政学リスク下での役割。",
        "北海道は カロリーベース 220% の自給率で日本最大の食料生産基地。一方、国全体の自給率は 38% で輸入依存。ウクライナ侵攻 ・ 気候変動 ・ 国際物流リスクで食料安全保障の重要性が再認識される。北海道は国全体の食料供給の要として機能拡大の余地。",
        "食料安全保障は単なる「自給率向上」を超えて、生産 ・ 物流 ・ 備蓄 ・ 緊急対応 ・ 国際協調の総合戦略。北海道は最大の生産基地として、国全体の安全保障に貢献する長期戦略を取れる位置にある。",
        [
            {"who": "オランダ ・ 食料輸出大国", "what": "効率的農業で世界 2 位の食料輸出国。技術と政策の統合事例。", "source": {"t": "Wageningen", "o": "オランダ", "u": "https://www.wur.nl/"}},
            {"who": "スイス ・ 食料備蓄制度", "what": "国家備蓄 ・ 自給率政策の長期事例。", "source": {"t": "Federal Office", "o": "スイス", "u": "https://www.admin.ch/"}},
        ],
        [
            {"who": "農林水産省", "what": "食料 ・ 農業 ・ 農村基本計画", "region": "all", "s": -1},
            {"who": "北海道 ・ 道庁", "what": "食料供給基地としての戦略", "region": "all", "s": -1},
        ],
        [
            {"h": "数値で見る現状", "b": "北海道 カロリー自給率 220% 、生産額ベース 220%。全国平均 38% / 65%。輸入依存度高い。"},
            {"h": "リスク要因", "b": "気候変動 ・ 国際物流 ・ 地政学 ・ 為替 ・ 燃料費高騰等のリスク。輸入途絶時の影響大。"},
            {"h": "中心問い", "b": "「自給率向上」だけか、生産 ・ 物流 ・ 備蓄 ・ 国際協調を含む総合戦略か。"},
            {"h": "残る資産", "b": "農地 ・ 生産基盤 ・ 加工技術 ・ ノウハウ ・ 国際関係 ・ ブランド。"},
        ],
        [
            {"v": "220%", "l": "北海道カロリー自給率"},
            {"v": "38%", "l": "全国平均"},
        ],
        [
            {"t": "生産基盤の維持 ・ 拡大", "d": "農地保全 ・ 担い手育成 ・ 技術革新"},
            {"t": "備蓄 ・ 物流の強化", "d": "国家備蓄 ・ 緊急時対応"},
            {"t": "国際協調 ・ 輸出戦略", "d": "食料輸出での外交カード"},
        ],
        [
            {"t": "農林水産省", "o": "農林水産省", "u": "https://www.maff.go.jp/"},
            {"t": "北海道 農政部", "o": "北海道", "u": "https://www.pref.hokkaido.lg.jp/"},
        ],
        [
            {"actor": "個人として", "actions": ["道産品を意識的に購入", "食料安全保障について学ぶ", "備蓄を準備"]},
            {"actor": "企業 ・ 組織として", "actions": ["道産食材の活用拡大", "食料関連事業への投資", "サプライチェーンの安定化"]},
        ],
    ),
    make_issue(
        "wildlife-management", "野生動物管理と人との共生", "北海道 エゾシカ キタキツネ 野生動物 鳥獣害",
        "primary", 4, 3, ["all"], ["rural-mountain", "agriculture"],
        ["エゾシカ", "キタキツネ", "野生動物管理", "鳥獣害", "ハンター"],
        "ヒグマだけでなくエゾシカ・キツネ・アライグマ等、野生動物管理の総合戦略が必要。",
        "ヒグマに加え、エゾシカは推計 70 万頭以上で農林業 ・ 交通への被害大。キタキツネのエキノコックス対策も継続課題。外来種アライグマも増加。ハンター減少 ・ 野生動物の生息域拡大 ・ 気候変動等の複合課題。",
        "野生動物管理は「個別駆除」を超えて、生態系 ・ 農林業 ・ 観光 ・ 教育 ・ 人材育成の総合戦略。ヒグマ ・ エゾシカ ・ アライグマ等の種別戦略と、地域全体での共生構造が必要。",
        [
            {"who": "アメリカ ・ ナショナルパーク管理", "what": "野生動物 ・ 生態系管理の長期国際モデル。", "source": {"t": "National Park Service", "o": "アメリカ", "u": "https://www.nps.gov/"}},
            {"who": "兵庫県 ・ シカ管理", "what": "シカ個体数管理 ・ ジビエ活用の長期事例。", "source": {"t": "兵庫県", "o": "兵庫県", "u": "https://web.pref.hyogo.lg.jp/"}},
        ],
        [
            {"who": "北海道 環境生活部", "what": "野生動物管理計画", "region": "all", "s": -1},
            {"who": "道内ハンター ・ 猟友会", "what": "個体数管理 ・ 駆除", "region": "all", "s": -1},
        ],
        [
            {"h": "数値で見る現状", "b": "エゾシカ推計 70 万頭超、農林業被害年数十億円規模。ヒグマ 1.2 万頭。アライグマも増加。ハンターは高齢化 ・ 減少。"},
            {"h": "複合要因", "b": "森林管理 ・ 緩衝帯 ・ 餌付け ・ 気候変動 ・ ハンター減少 ・ 個体数増。"},
            {"h": "中心問い", "b": "「個別駆除」か「生態系全体での共生構造設計」か。"},
            {"h": "残る資産", "b": "ハンター人材 ・ モニタリングデータ ・ ジビエ流通 ・ 共生文化 ・ 観光価値。"},
        ],
        [
            {"v": "70 万頭超", "l": "エゾシカ推計"},
            {"v": "数十億円", "l": "農林業被害年額"},
        ],
        [
            {"t": "ハンター育成 ・ 通年化", "d": "若手参入 ・ 通年雇用 ・ 人材確保"},
            {"t": "ジビエ流通 ・ 観光連携", "d": "ジビエ事業化 ・ 観光価値化"},
            {"t": "生態系全体の管理", "d": "森林 ・ 緩衝帯 ・ 餌付け対策の統合"},
        ],
        [
            {"t": "環境省 野生鳥獣保護管理", "o": "環境省", "u": "https://www.env.go.jp/nature/choju/"},
            {"t": "農林水産省 鳥獣被害対策", "o": "農林水産省", "u": "https://www.maff.go.jp/j/seisan/tyozyu/"},
        ],
        [
            {"actor": "個人として", "actions": ["野生動物との安全な共生方法を学ぶ", "ジビエを意識的に消費", "ゴミ ・ 餌になるものの管理"]},
            {"actor": "企業 ・ 組織として", "actions": ["ジビエ流通 ・ 商品化への参入", "野生動物管理プロジェクトへの協賛", "ハンター育成への協力"]},
        ],
    ),
    make_issue(
        "climate-adaptation", "気候変動適応戦略", "北海道 気候変動 適応 温暖化 ゲリラ豪雨",
        "environment", 4, 4, ["all"], ["agriculture", "fishing-village", "urban"],
        ["気候変動", "適応", "温暖化", "ゲリラ豪雨", "極端気象"],
        "気候変動の影響顕在化。緩和（脱炭素）と並ぶ適応戦略を地域別・分野別に設計する必要。",
        "気候変動の影響は北海道でも顕在化。気温上昇 ・ ゲリラ豪雨 ・ 暖冬 ・ 海水温上昇 ・ 生態系変化等。緩和（脱炭素）と並ぶ「適応」戦略が国際的に重要視される。農業 ・ 漁業 ・ 観光 ・ インフラ ・ 健康 ・ 災害等の分野別 ・ 地域別対応が必要。",
        "気候変動適応は「天候の問題」を超えた地域経済 ・ 社会全体の構造課題。緩和 ( 脱炭素 ) と適応の両輪、分野別 ・ 地域別の具体的戦略、長期視点 ( 50-100 年 ) での計画が必要。",
        [
            {"who": "オランダ ・ デルタワークス", "what": "海面上昇 ・ 治水の世界モデル。長期国土計画。", "source": {"t": "Rijkswaterstaat", "o": "オランダ", "u": "https://www.rijkswaterstaat.nl/"}},
            {"who": "デンマーク ・ コペンハーゲン", "what": "豪雨適応都市計画。レジリエンス先進事例。", "source": {"t": "Copenhagen", "o": "デンマーク", "u": "https://www.kk.dk/"}},
        ],
        [
            {"who": "環境省 ・ 気候変動適応センター", "what": "国家適応計画 ・ 自治体支援", "region": "all", "s": -1},
            {"who": "北海道 ・ 道内自治体", "what": "地域気候変動適応計画", "region": "all", "s": -1},
        ],
        [
            {"h": "数値で見る現状", "b": "気温は道内で 100 年間に 1.5℃ 上昇。ゲリラ豪雨 ・ 暖冬 ・ 海水温上昇等の影響顕在化。"},
            {"h": "分野別影響", "b": "農業 ( 北上 ・ 病害 ) 、漁業 ( 魚種変化 ) 、観光 ( スキー ・ 桜 ) 、インフラ ( 豪雨 ・ 浸水 ) 、健康 ( 熱中症 ・ 感染症 ) 、生態系。"},
            {"h": "中心問い", "b": "「緩和 ( 脱炭素 ) 」だけか、「適応 ( 影響への対応 ) 」も含む両輪戦略か。"},
            {"h": "残る資産", "b": "適応インフラ ・ 知識 ・ コミュニティ ・ レジリエンスの蓄積。"},
        ],
        [
            {"v": "1.5℃", "l": "道内 100 年で気温上昇"},
            {"v": "顕在化中", "l": "ゲリラ豪雨 ・ 暖冬 ・ 海水温上昇"},
        ],
        [
            {"t": "地域適応計画策定", "d": "各自治体での適応計画 ・ 分野別対応"},
            {"t": "インフラの強靭化", "d": "豪雨 ・ 海面上昇に対応するインフラ整備"},
            {"t": "農業 ・ 漁業の品種転換", "d": "気候変動に適応する品種 ・ 技術"},
        ],
        [
            {"t": "気候変動適応センター", "o": "国立環境研究所", "u": "https://adaptation-platform.nies.go.jp/"},
            {"t": "環境省 適応策", "o": "環境省", "u": "https://www.env.go.jp/"},
        ],
        [
            {"actor": "個人として", "actions": ["気候変動の影響を学ぶ", "気候変動対策プロジェクトに参加", "省エネ ・ 適応行動を日常化"]},
            {"actor": "企業 ・ 組織として", "actions": ["BCP に気候変動リスクを含める", "事業の脱炭素 ・ 適応戦略", "気候変動関連の研究 ・ 投資"]},
        ],
    ),
    make_issue(
        "community-broadcasting", "コミュニティ FM ・ 地域放送の役割", "北海道 コミュニティ FM 地域放送 災害情報",
        "digital", 3, 3, ["all"], ["urban", "rural-mountain"],
        ["コミュニティ FM", "地域放送", "災害情報", "地域メディア"],
        "コミュニティ FM・地域放送は災害情報・地域文化の核。経営困難下での維持と公共インフラ化が論点。",
        "全国のコミュニティ FM は約 340 局、北海道にも複数存在。災害情報 ・ 地域文化 ・ コミュニティ形成の核として機能。一方、広告収入減 ・ 経営困難で閉局事例も。災害時の情報源として再評価される一方、平時の経営持続が課題。",
        "コミュニティ FM は単なる「ローカルラジオ」を超えて、災害時の情報源 ・ 地域文化の核 ・ コミュニティ形成の場としての公共インフラ価値。経営困難下で公的支援 ・ 多目的化 ・ 連携 ・ デジタル展開等の長期戦略で支える視点が必要。",
        [
            {"who": "石川県珠洲市 ・ コミュニティ FM", "what": "能登地震 ( 2024 ) で災害時情報インフラとして機能。", "source": {"t": "総務省", "o": "総務省", "u": "https://www.soumu.go.jp/"}},
            {"who": "新潟県 ・ FM ながおか", "what": "中越地震 ( 2004 ) で地域情報インフラの長期事例。", "source": {"t": "FM ながおか", "o": "新潟県", "u": "https://fmnagaoka.com/"}},
        ],
        [
            {"who": "総務省", "what": "コミュニティ FM 制度 ・ 災害対応支援", "region": "all", "s": -1},
            {"who": "道内コミュニティ FM 局", "what": "地域放送 ・ 災害情報", "region": "all", "s": -1},
        ],
        [
            {"h": "数値で見る現状", "b": "全国コミュニティ FM 約 340 局、北海道にも複数。市民放送的性格で災害時 ・ 地域コミュニティに貢献。経営は厳しい。"},
            {"h": "公共財としての価値", "b": "災害時情報 ・ 地域文化 ・ コミュニティ形成 ・ 心の支援等の多面的価値。商業ベースだけでは持続困難。"},
            {"h": "中心問い", "b": "「商業放送」として持続を求めるか、「災害インフラ ・ 公共財」として公的支援を含む長期戦略か。"},
            {"h": "残る資産", "b": "ライセンス ・ 機材 ・ 人材 ・ リスナーコミュニティ ・ 地域知識 ・ 災害対応ノウハウ。"},
        ],
        [
            {"v": "約 340 局", "l": "全国コミュニティ FM"},
            {"v": "災害時インフラ", "l": "重要価値"},
        ],
        [
            {"t": "公的支援 ・ 災害インフラ化", "d": "公的支援 ・ 災害時情報インフラとしての位置付け"},
            {"t": "デジタル展開 ・ Web ・ ポッドキャスト", "d": "リスナー拡大 ・ 新収益モデル"},
            {"t": "地域連携 ・ 多目的化", "d": "自治体 ・ NPO ・ 学校等との連携"},
        ],
        [
            {"t": "総務省 コミュニティ放送", "o": "総務省", "u": "https://www.soumu.go.jp/main_sosiki/joho_tsusin/broadcasting/"},
            {"t": "日本コミュニティ放送協会", "o": "JCBA", "u": "https://www.jcba.jp/"},
        ],
        [
            {"actor": "個人として", "actions": ["地元コミュニティ FM を聴く ・ 寄附", "災害時の情報源として活用", "地域放送への意見 ・ 番組参加"]},
            {"actor": "企業 ・ 組織として", "actions": ["コミュニティ FM への広告 ・ 協賛", "災害時の情報連携 ・ BCP に組み込む", "地域報道の支援"]},
        ],
    ),
    make_issue(
        "senior-second-career", "シニア起業 ・ セカンドキャリア", "北海道 シニア セカンドキャリア 起業 定年後",
        "industry", 3, 3, ["all"], ["urban"],
        ["シニア", "セカンドキャリア", "起業", "定年後", "高齢者雇用"],
        "定年後のシニアが地域で起業・移住・社会参加。経験・資産を地域に活かす長期戦略。",
        "全国の高齢者は約 3,600 万人、定年延長 ・ 健康寿命延伸で 60-70 代の経済社会活動への参加意欲が高まる。シニア起業 ・ セカンドキャリア ・ 移住等で地域経済 ・ コミュニティへの貢献余地。北海道は移住地として人気もあり、シニアの参入が地域活性化のチャンス。",
        "シニアの経験 ・ 資産 ・ ネットワークは地域経済の重要な資源。「定年で社会から退く」発想から「セカンドキャリアで地域貢献 ・ 起業 ・ 学び ・ 移住」へ転換することで、人口減社会の新たな活力源になる。",
        [
            {"who": "国土交通省 ・ 移住政策", "what": "都市部シニアの地方移住促進 ・ CCRC ( 生涯活躍のまち ) 構想。", "source": {"t": "国土交通省", "o": "国土交通省", "u": "https://www.mlit.go.jp/"}},
            {"who": "アメリカ ・ AARP", "what": "シニア向けの長期キャリア ・ 起業 ・ 社会参加支援。国際的なモデル。", "source": {"t": "AARP", "o": "AARP", "u": "https://www.aarp.org/"}},
        ],
        [
            {"who": "北海道 ・ 自治体", "what": "シニア起業 ・ 移住支援", "region": "all", "s": -1},
            {"who": "道内 NPO ・ 商工会", "what": "シニア起業塾 ・ メンタリング", "region": "all", "s": -1},
        ],
        [
            {"h": "数値で見る現状", "b": "全国高齢者約 3,600 万人、健康寿命 70 代後半。シニア起業 ・ セカンドキャリア意欲高まる。北海道はシニア移住先として人気。"},
            {"h": "シニアの強み", "b": "経験 ・ 専門知識 ・ 人脈 ・ 資産 ・ 時間 ・ 安定収入 ( 年金 ) 等、若年起業家にない強み。"},
            {"h": "中心問い", "b": "「定年で退く」か「セカンドキャリアで貢献 ・ 起業 ・ 学び」か、社会全体での発想転換が必要。"},
            {"h": "残る資産", "b": "シニアの経験 ・ ノウハウ ・ 人脈 ・ 起業 ・ 雇用 ・ 学びの場 ・ 地域コミュニティ。"},
        ],
        [
            {"v": "3,600 万人", "l": "全国高齢者"},
            {"v": "健康寿命 70 代後半", "l": "セカンドキャリアの時間"},
        ],
        [
            {"t": "シニア起業塾 ・ メンタリング", "d": "経験を活かした起業支援"},
            {"t": "セカンドキャリア ・ 学び直し", "d": "リスキリング ・ 副業 ・ 社会参加"},
            {"t": "CCRC ・ シニア移住", "d": "地方移住 ・ 生涯活躍のまち"},
        ],
        [
            {"t": "内閣府 高齢社会対策", "o": "内閣府", "u": "https://www8.cao.go.jp/kourei/"},
            {"t": "厚生労働省 シニア雇用", "o": "厚生労働省", "u": "https://www.mhlw.go.jp/"},
        ],
        [
            {"actor": "個人として", "actions": ["セカンドキャリア ・ 学び直しの計画", "シニア起業塾 ・ コミュニティに参加", "経験 ・ スキルを地域に活かす"]},
            {"actor": "企業 ・ 組織として", "actions": ["シニア雇用 ・ 顧問制度の導入", "シニアの経験 ・ ネットワーク活用", "シニア起業 ・ 移住支援"]},
        ],
    ),
    make_issue(
        "disaster-recovery", "災害復興と地域再生", "北海道 災害復興 胆振東部地震 復興 ブラックアウト",
        "environment", 3, 4, ["all", "dou-o"], ["urban", "rural-mountain"],
        ["災害復興", "胆振東部地震", "復興", "ブラックアウト", "BCP"],
        "胆振東部地震 ( 2018 ) ・ ブラックアウトからの復興知見。次の災害への備えと長期戦略。",
        "2018 年 9 月の胆振東部地震 ( 厚真町中心、震度 7 ) で 43 名死亡 ・ 全道ブラックアウト ・ 産業被害。復興は短期で進んだが、長期の地域再生 ・ 教訓継承 ・ 次への備えが続く。地震 ・ 津波 ・ 台風 ・ 豪雪等の複合災害リスク下、復興知見を体系化する課題。",
        "災害復興は「元に戻す」を超えて、より強靭で持続可能な地域を作る機会。胆振東部地震 ・ ブラックアウトの教訓を体系化し、次の災害 ( 千島海溝 ・ 日本海溝地震等 ) への備え ・ レジリエンス ・ 地域コミュニティ強化に活かす長期戦略。",
        [
            {"who": "東日本大震災復興", "what": "10 年以上の長期復興 ・ コミュニティ再生 ・ 教訓継承の国家事例。", "source": {"t": "復興庁", "o": "復興庁", "u": "https://www.reconstruction.go.jp/"}},
            {"who": "ニュージーランド ・ クライストチャーチ", "what": "2011 年地震からの再生 ・ レジリエンス都市の長期事例。", "source": {"t": "Christchurch City", "o": "ニュージーランド", "u": "https://www.ccc.govt.nz/"}},
        ],
        [
            {"who": "北海道 ・ 厚真町等", "what": "復興 ・ 地域再生 ・ 教訓継承", "region": "dou-o", "s": -1},
            {"who": "国 ・ 自治体", "what": "災害復興制度 ・ 復興基金", "region": "all", "s": -1},
        ],
        [
            {"h": "数値で見る現状", "b": "2018 胆振東部地震: 死者 43 名 、全道ブラックアウト ( 295 万戸 ) 、産業被害甚大。復興は短期で進んだが、長期教訓継承 ・ レジリエンス強化が続く課題。"},
            {"h": "復興の構造", "b": "短期 ( 救援 ・ 仮設住宅 ) ・ 中期 ( 復興計画 ・ 再建 ) ・ 長期 ( レジリエンス強化 ・ 教訓継承 ) の 3 段階。各段階で異なるアプローチ。"},
            {"h": "中心問い", "b": "「元に戻す」か「より強靭で持続可能な地域を作る」か、復興を機会として活かす長期視点。"},
            {"h": "残る資産", "b": "復興インフラ ・ 知識 ・ コミュニティ ・ 教訓 ・ レジリエンス文化。"},
        ],
        [
            {"v": "43 名", "l": "胆振東部地震死者"},
            {"v": "295 万戸", "l": "ブラックアウト被災戸数"},
        ],
        [
            {"t": "教訓体系化 ・ アーカイブ", "d": "復興経験 ・ 教訓を体系的に記録 ・ 継承"},
            {"t": "レジリエンス強化", "d": "次の災害への構造的備え"},
            {"t": "地域コミュニティ再生", "d": "災害後の長期コミュニティ再生 ・ 心のケア"},
        ],
        [
            {"t": "復興庁", "o": "復興庁", "u": "https://www.reconstruction.go.jp/"},
            {"t": "内閣府 防災", "o": "内閣府", "u": "https://www.bousai.go.jp/"},
        ],
        [
            {"actor": "個人として", "actions": ["災害復興の経験 ・ 教訓を学ぶ", "被災地への支援 ・ ボランティア", "自分の備え ・ BCP を強化"]},
            {"actor": "企業 ・ 組織として", "actions": ["BCP に複合災害シナリオを含める", "被災地への継続支援 ・ CSR", "従業員の防災教育"]},
        ],
    ),
]


# Day 3 articles: 12 paired + 16 アイデア for existing 課題発見-only ISSUEs
ARTICLES_DAY3 = [
    # === Day 3 new ISSUEs × 2 = 12 ===
    {"id": "food-security-structure-2026-06", "title": "北海道は日本の食料安全保障の要 - 220% 自給率の構造", "category": "課題発見", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["food-security", "food-waste-self-sufficiency"], "summary": "北海道 カロリー自給率 220% は全国 38% の要。輸入依存 ・ 気候変動 ・ 地政学リスク下での役割構造。", "topic": "generic"},
    {"id": "food-security-strategy-2026-06", "title": "北海道発の食料安全保障戦略 - 5 つの実装", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["food-security"], "summary": "生産基盤 ・ 備蓄 ・ 物流 ・ 輸出 ・ 国際協調。北海道発の食料安全保障 5 戦略。", "topic": "generic"},
    {"id": "wildlife-management-structure-2026-06", "title": "野生動物管理の総合戦略 - ヒグマ ・ シカ ・ アライグマの構造", "category": "課題発見", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["wildlife-management", "bear-conflict"], "summary": "エゾシカ 70 万頭超 ・ ヒグマ 1.2 万頭 ・ アライグマ等の複合的な野生動物管理の構造。", "topic": "generic"},
    {"id": "wildlife-management-strategy-2026-06", "title": "野生動物との共生をジビエ ・ 観光に - 4 つの活用戦略", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["wildlife-management"], "summary": "ハンター育成 ・ ジビエ流通 ・ 観光連携 ・ 生態系管理。兵庫モデルから学ぶ 4 戦略。", "topic": "generic"},
    {"id": "climate-adaptation-structure-2026-06", "title": "気候変動適応戦略 - 緩和と適応の両輪", "category": "課題発見", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["climate-adaptation"], "summary": "気温 100 年で 1.5℃ 上昇、農業 ・ 漁業 ・ 観光に影響。緩和 ( 脱炭素 ) と適応 ( 影響対応 ) の両輪戦略。", "topic": "generic"},
    {"id": "climate-adaptation-implementation-2026-06", "title": "分野別 ・ 地域別の気候変動適応 - オランダ ・ デンマーク事例", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["climate-adaptation"], "summary": "デルタワークス ・ コペンハーゲン豪雨計画 ・ 分野別適応。世界の長期事例から学ぶ実装。", "topic": "generic"},
    {"id": "community-broadcasting-structure-2026-06", "title": "コミュニティ FM の役割 - 災害インフラと地域文化", "category": "課題発見", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["community-broadcasting", "local-media"], "summary": "全国 340 局のコミュニティ FM 、能登地震で災害情報源として機能。商業放送を超えた公共インフラ価値。", "topic": "generic"},
    {"id": "community-broadcasting-renewal-2026-06", "title": "コミュニティ FM を災害時公共インフラに - 4 戦略", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["community-broadcasting"], "summary": "公的支援 ・ デジタル展開 ・ 地域連携 ・ 災害インフラ化。コミュニティ FM 持続の 4 つの実装。", "topic": "generic"},
    {"id": "senior-second-career-structure-2026-06", "title": "シニア起業 ・ セカンドキャリア - 3,600 万人の活力源", "category": "課題発見", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["senior-second-career"], "summary": "高齢者 3,600 万人、健康寿命延伸でシニアの社会経済参加が地域活性化の鍵。構造を読み解く。", "topic": "generic"},
    {"id": "senior-second-career-strategy-2026-06", "title": "シニアの経験を地域に - 起業 ・ 学び ・ 移住の 4 戦略", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["senior-second-career"], "summary": "起業塾 ・ 学び直し ・ CCRC ・ 顧問制度。AARP モデルから学ぶシニア活用 4 戦略。", "topic": "generic"},
    {"id": "disaster-recovery-structure-2026-06", "title": "胆振東部地震 ・ ブラックアウトからの復興 - 教訓と次への備え", "category": "課題発見", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["disaster-recovery", "disaster"], "summary": "2018 年震度 7 ・ 43 名死亡 ・ 全道ブラックアウト。復興と教訓継承 ・ 次の災害への備えの構造。", "topic": "generic"},
    {"id": "disaster-recovery-resilience-2026-06", "title": "復興からレジリエンスへ - 5 つの仕組みづくり", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["disaster-recovery"], "summary": "教訓体系化 ・ アーカイブ ・ 訓練 ・ コミュニティ ・ 制度。東日本 ・ クライストチャーチ事例から学ぶ実装。", "topic": "generic"},
    # === 既存 ISSUE のアイデア記事 16 ===
    {"id": "aging-care-strategy-2026-06", "title": "高齢化社会の地域包括ケア - 柏 ・ 大牟田に学ぶ 5 戦略", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["aging-care", "aging-single-household-2026-06"], "summary": "柏プロジェクト 15 年 ・ 大牟田 20 年継続事例から、地域包括ケア構築の 5 戦略を実装。", "topic": "generic"},
    {"id": "childcare-shortage-strategy-2026-06", "title": "保育不足を解決する - 流山モデルの 4 戦略", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["childcare-shortage"], "summary": "送迎保育 ・ 拡充 ・ 子育てブランディング ・ 企業連携。流山市から学ぶ保育問題解決 4 戦略。", "topic": "generic"},
    {"id": "ainu-culture-future-2026-06", "title": "アイヌ文化を未来へ - 5 つの統合戦略", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["ainu-culture"], "summary": "言語復興 ・ 教育 ・ 経済参加 ・ ブランディング ・ 国際発信。アイヌ文化と地域アイデンティティの 5 戦略。", "topic": "generic"},
    {"id": "school-consolidation-attractive-2026-06", "title": "小規模校を地域の核に - 海士町 ・ 神山町モデル", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["school-consolidation"], "summary": "島留学 ・ 地域協働カリキュラム ・ サテライト ・ コミュニティ運営。長期事例から学ぶ実装。", "topic": "generic"},
    {"id": "infra-aging-compact-2026-06", "title": "インフラ集約と居住誘導 - 富山モデルの実装", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["infra-aging"], "summary": "コンパクトシティ ・ 公共交通軸 ・ 居住誘導 ・ 多機能化。富山市 20 年事例から学ぶ実装戦略。", "topic": "generic"},
    {"id": "cost-of-living-strategy-2026-06", "title": "暮らしのコストを下げる - 道産活用と地域循環の 4 戦略", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["cost-of-living"], "summary": "省エネ住宅 ・ 道産食材 ・ 地域循環 ・ 公共交通。暮らしのコスト構造改善の 4 戦略。", "topic": "generic"},
    {"id": "forest-circulation-strategy-2026-06", "title": "森林循環を地域経済の核に - 下川モデルの 5 戦略", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["forest-circulation"], "summary": "下川 SDGs 未来都市 ・ 智頭杉 ・ ドイツ持続林業から学ぶ森林循環 5 戦略。", "topic": "generic"},
    {"id": "fisheries-climate-strategy-2026-06", "title": "気候変動下の漁業 - 4 つの適応 ・ 転換戦略", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["fisheries-climate"], "summary": "新魚種 ・ 養殖 ・ ノルウェーモデル ・ MSC 認証。気候変動下の漁業適応 4 戦略。", "topic": "generic"},
    {"id": "elderly-care-staff-strategy-2026-06", "title": "介護人材 32 万人不足の解決 - 6 つの実装", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["elderly-care-staff"], "summary": "処遇改善 ・ 外国人活用 ・ DX ・ タスクシフト ・ 地域包括 ・ 評価転換。介護人材確保 6 戦略。", "topic": "generic"},
    {"id": "reskilling-regional-2026-06", "title": "地域でリスキリング - 副業 ・ 学び直しの 4 戦略", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["reskilling"], "summary": "HICTA ・ 大学講座 ・ 副業 ・ ふるさと副業。地方でのリスキリング 4 戦略の実装。", "topic": "generic"},
    {"id": "foreign-resident-strategy-2026-06", "title": "外国人住民の生活基盤 - 大泉町 30 年に学ぶ 5 戦略", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["foreign-resident-support", "multicultural"], "summary": "言語 ・ 住宅 ・ コミュニティ ・ 子ども教育 ・ 文化変容。大泉町 30 年継続事例から 5 戦略。", "topic": "generic"},
    {"id": "new-industry-strategy-2026-06", "title": "新産業を北海道で育てる - 4 つの実装", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["new-industry"], "summary": "宇宙 ・ 半導体 ・ 食品テック ・ クリーンテック。北海道の新産業 4 領域の実装戦略。", "topic": "generic"},
    {"id": "depopulation-recover-2026-06", "title": "人口減少からの回復 - 海士町 ・ 神山町 ・ 上士幌の構造", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["depopulation"], "summary": "20 年継続事例から学ぶ人口減地域の回復構造。仕組み資産による長期戦略。", "topic": "generic"},
    {"id": "regional-medical-strategy-2026-06", "title": "地域医療を支える仕組み - 4 つの実装戦略", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["regional-medical"], "summary": "オンライン診療 ・ タスクシフト ・ 地域包括 ・ 広域連携。地域医療維持の 4 戦略。", "topic": "generic"},
    {"id": "food-waste-strategy-2026-06", "title": "サーキュラーフード北海道 - 5 つの実装", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["food-waste-self-sufficiency"], "summary": "規格外加工 ・ ロス削減 ・ 飼料化 ・ 堆肥化 ・ ブランディング。サーキュラーフード 5 戦略。", "topic": "generic"},
    {"id": "multicultural-strategy-2026-06", "title": "多文化共生の長期戦略 - 浜松 ・ 大泉モデル", "category": "アイデア", "publishedAt": "2026-06-15", "readMinutes": 4, "relatedIssueIds": ["multicultural"], "summary": "HICE 30 年 ・ 大泉町 30 年。多文化共生の長期事例から学ぶ実装戦略。", "topic": "generic"},
]


def append_issues():
    content = DATA.read_text(encoding="utf-8")
    insert_text = ",\n" + ",\n".join(issue_to_js(i) for i in ISSUES_DAY3) + "\n"
    issues_end = content.index("];\n\n// 出典")
    last_brace = content.rfind("  }", 0, issues_end)
    content = content[:last_brace + 3] + insert_text + content[last_brace + 3:]
    DATA.write_text(content, encoding="utf-8")
    print(f"Added {len(ISSUES_DAY3)} ISSUEs to data.js")


def append_articles():
    import json

    data_content = DATA.read_text(encoding="utf-8")
    new_data_entries = ""
    for art in ARTICLES_DAY3:
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

    art_start = data_content.find("const ARTICLES = [")
    art_end = data_content.find("];", art_start)
    new_data_content = data_content[:art_end] + new_data_entries + data_content[art_end:]
    DATA.write_text(new_data_content, encoding="utf-8")
    print(f"Added {len(ARTICLES_DAY3)} article summaries to data.js")

    gen_content = GEN.read_text(encoding="utf-8")
    new_entries = ""
    for art in ARTICLES_DAY3:
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

    marker = "]\n\n\nGLOSSARY_TERMS = ["
    new_gen_content = gen_content.replace(marker, new_entries + marker, 1)
    GEN.write_text(new_gen_content, encoding="utf-8")
    print(f"Added {len(ARTICLES_DAY3)} articles to generate_articles.py")


if __name__ == "__main__":
    append_issues()
    append_articles()
