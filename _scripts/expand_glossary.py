#!/usr/bin/env python3
"""Expand glossary.html with ~35 more terms and update GLOSSARY_TERMS in generator."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY = ROOT / "glossary.html"
GEN = ROOT / "_scripts" / "generate_articles.py"

# New terms organized by category
# Each: (slug, term, reading, definition)
NEW_TERMS = {
    "編集 ・ 概念フレーム": [
        ("central-question", "中心問い", "ちゅうしんとい", "課題の本質を 1 つの問いに集約し、議論や施策の判断軸にする編集手法。例: 「移住政策は人を固定することか、人を通じて資産を残すことか」。当サイトの記事 ・ ISSUE で重視。"),
        ("3-stage-journey", "3 段ジャーニー", "さんだんじゃーにー", "「課題を知る → アイデアを得る → 行動に移す」のユーザー体験フレーム。当サイトの設計軸。"),
        ("legacy-asset-framework", "残る資産フレーム", "のこるしさんふれーむ", "「事業資産 ・ 関係資産 ・ 仕組み資産 ・ 規範資産」の 4 分類で施策の長期効果を評価する考え方。"),
    ],
    "移住 ・ 関係人口 ・ 暮らし": [
        ("dual-residence", "二地域居住", "にちいききょじゅう", "都市と地方の両方に拠点を持って暮らす働き方 ・ ライフスタイル。関係人口の主要形態の 1 つ。"),
        ("furusato-return", "ふるさと回帰", "ふるさとかいき", "都市住民が地方に移住 ・ 関わる動き。認定 NPO 法人ふるさと回帰支援センターが推進。"),
        ("residential-induction", "居住誘導区域", "きょじゅうゆうどうくいき", "都市計画法に基づき、人口減少下でも生活サービスや公共交通を維持するため居住を誘導する区域。コンパクトシティの基盤。"),
        ("immigration-counter", "移住相談窓口", "いじゅうそうだんまどぐち", "自治体や民間が運営する移住希望者向け相談 ・ マッチング機能。"),
        ("ainu-iturn", "島留学 ・ 地域留学", "しまりゅうがく ・ ちいきりゅうがく", "島根県海士町等が始めた、地域外の生徒を高校に受け入れる留学プログラム。教育魅力化と移住の入口。"),
    ],
    "産業 ・ 起業 ・ 雇用": [
        ("six-industrialization", "6 次産業化", "ろくじさんぎょうか", "1 次 ( 生産 ) + 2 次 ( 加工 ) + 3 次 ( 販売 ・ サービス ) を統合する地域産業モデル。1 + 2 + 3 = 6。"),
        ("business-succession", "事業承継", "じぎょうしょうけい", "中小企業 ・ 一次産業者の経営を次世代に引き継ぐこと。親族継承 ・ 第三者継承等の方法がある。黒字廃業の防止が論点。"),
        ("vc", "VC ( ベンチャーキャピタル )", "ぶいしー", "高成長スタートアップに投資する投資ファンド。地方スタートアップ生態系の重要なプレイヤー。"),
        ("accelerator", "アクセラレーター", "あくせられーたー", "短期集中型でスタートアップを育成する民間 ・ 公的プログラム。資金 ・ メンタリング ・ ネットワークを提供。"),
        ("u-i-j-detail", "U ターン ・ I ターン ・ J ターン", "ゆーたーん ・ あいたーん ・ じぇーたーん", "U= 出身地に戻る、I= 縁のない地方へ移住、J= 出身地近郊に移住。移住政策で使われる分類。"),
        ("kakeagi", "新規就農", "しんきしゅうのう", "農業を新たに始めること。親元就農 ・ 雇用就農 ・ 独立就農の 3 種類があり、全国新規就農相談センターが支援。"),
    ],
    "観光 ・ 地域経済": [
        ("overtourism", "オーバーツーリズム", "おーばーつーりずむ", "観光客が過剰に集中することで地域住民の生活 ・ 環境 ・ 文化に負荷をかける現象。ニセコ ・ 京都等で顕在化。"),
        ("mice", "MICE", "まいす", "Meeting ・ Incentive travel ・ Convention ・ Exhibition の頭文字。ビジネス目的の観光 ・ 国際会議の総称。"),
        ("local-brand", "地域ブランド", "ちいきぶらんど", "産品 ・ 産地 ・ 自治体のブランド化。プレミアム価格化 ・ ロイヤルティ獲得を目指す。"),
        ("workation", "ワーケーション", "わーけーしょん", "Work + Vacation 。リゾート ・ 観光地で仕事を続ける働き方。コロナ後に拡大、地方創生の機会。"),
    ],
    "教育 ・ 子育て": [
        ("school-attractive", "教育魅力化", "きょういくみりょくか", "地域 ・ 学校 ・ 行政の連携で公立校 ( 特に高校 ) の魅力を高める取り組み。海士町の島前高校が先行事例。"),
        ("free-school", "フリースクール", "ふりーすくーる", "不登校 ・ 学校外学習を支援する民間学習施設。教育機会確保法 ( 2017 ) で位置づけ向上中。"),
        ("learning-support", "学習支援", "がくしゅうしえん", "経済的困難 ・ 発達特性等で学習機会の少ない子ども ・ 若者向けの無料 ・ 低価格の学習プログラム。"),
        ("nursery-shortage", "待機児童", "たいきじどう", "認可保育所の利用希望が満たされない子ども。各市町村が把握 ・ 公表する。「潜在待機児童」を含めるとさらに多い。"),
    ],
    "医療 ・ 福祉": [
        ("medical-region", "無医地区", "むいちく", "医療機関のない山間部 ・ 過疎地。北海道に約 137 ヶ所存在。"),
        ("8050-problem", "8050 問題", "はちまるごーまるもんだい", "80 代の親と 50 代のひきこもりの子の同居 ・ 親亡き後の生活困窮リスク。"),
        ("dementia-supporter", "認知症サポーター", "にんちしょうさぽーたー", "認知症の人 ・ 家族を地域で見守るためのボランティア。養成講座を受講して取得。"),
        ("home-care", "在宅医療 ・ 訪問介護", "ざいたくいりょう ・ ほうもんかいご", "病院 ・ 施設ではなく、患者の自宅で行う医療 ・ 介護。地域包括ケアの中核。"),
    ],
    "環境 ・ エネルギー": [
        ("renewable-energy", "再生可能エネルギー", "さいせいかのうえねるぎー", "風力 ・ 太陽光 ・ バイオマス ・ 地熱等、自然由来で枯渇しないエネルギー。北海道はポテンシャル全国一。"),
        ("grid-constraint", "系統制約", "けいとうせいやく", "発電された電力が送電網の容量不足で送れない状況。北海道では本州との連系線が細い問題。"),
        ("circular-economy", "サーキュラーエコノミー", "さーきゅらーえこのみー", "廃棄を出さず、資源を循環させる経済モデル。脱炭素 ・ 資源効率化と並ぶ国際潮流。"),
        ("blackout", "ブラックアウト", "ぶらっくあうと", "電力系統全体の崩壊による広域停電。2018 年 9 月の北海道胆振東部地震で全道停電を経験。"),
    ],
    "デジタル ・ サイバー": [
        ("ransomware", "ランサムウェア", "らんさむうぇあ", "システムを暗号化し身代金を要求するサイバー攻撃。地方自治体 ・ 中小企業 ・ 医療機関を狙う事例増加。"),
        ("soc", "SOC ( セキュリティオペレーションセンター )", "えすおーしー", "サイバー攻撃を 24 時間監視 ・ 検知 ・ 対応する専門組織。共同 SOC が地方の有効な対策。"),
        ("zero-trust", "ゼロトラスト", "ぜろとらすと", "「すべての通信 ・ ユーザーを信頼しない」前提のセキュリティモデル。クラウド ・ リモート時代の主流。"),
        ("smart-city", "スマートシティ", "すまーとしてぃ", "IoT ・ AI ・ ビッグデータを活用した都市運営。脱炭素 ・ 効率 ・ 暮らしやすさを統合的に向上。"),
        ("open-data", "オープンデータ", "おーぷんでーた", "公開された行政 ・ 公共データ。誰でも利用 ・ 加工 ・ 再配布可能。シビックテック ・ 地域 DX の基盤。"),
    ],
    "災害 ・ 防災": [
        ("resilience", "レジリエンス", "れじりえんす", "災害 ・ ショックからの回復力 ・ 適応力。インフラ多重化 ・ コミュニティ ・ BCP 等の総合的な能力。"),
        ("self-help-mutual-public", "自助 ・ 共助 ・ 公助", "じじょ ・ きょうじょ ・ こうじょ", "防災 ・ 福祉の 3 段階。自助 ( 自分 ) ・ 共助 ( 地域 ) ・ 公助 ( 行政 ) の役割分担。"),
        ("evacuation-plan", "避難計画", "ひなんけいかく", "災害時の避難経路 ・ 場所 ・ 物資等の事前計画。自治体策定だが家庭 ・ 企業も独自の計画が必要。"),
    ],
    "アイヌ ・ 多文化": [
        ("upopoy", "ウポポイ", "うぽぽい", "国立アイヌ民族博物館 + 国立民族共生公園。白老町に 2020 年開設、アイヌ文化発信の中核。"),
        ("inclusive-design", "ユニバーサルデザイン", "ゆにばーさるでざいん", "障害 ・ 年齢 ・ 性別 ・ 言語に関わらず利用できる商品 ・ サービス ・ 環境の設計。インクルーシブの基盤。"),
        ("easy-japanese", "やさしい日本語", "やさしいにほんご", "簡単な語彙 ・ 文法で書く日本語。外国人住民 ・ 障害者等の情報アクセスを支える。"),
    ],
}


def render_term(slug: str, term: str, reading: str, definition: str) -> str:
    return f'''<div class="glossary-item" id="term-{slug}">
<div class="glossary-term">{term}<span class="glossary-reading">{reading}</span></div>
<div class="glossary-def">{definition}</div>
</div>'''


def render_category(cat_name: str, terms: list) -> str:
    items = "\n".join(render_term(*t) for t in terms)
    return f'''<section class="glossary-cat">
<h2 class="glossary-cat-title">{cat_name}</h2>
<div class="glossary-list">
{items}
</div>
</section>'''


def main():
    content = GLOSSARY.read_text(encoding="utf-8")

    # Build new sections
    new_sections = "\n\n".join(render_category(cat, terms) for cat, terms in NEW_TERMS.items())

    # Insert before the "<div class=\"back-links back-links-bottom\">" near the end
    marker = '<div class="back-links back-links-bottom">'
    if marker not in content:
        print("ERROR: marker not found")
        return
    new_content = content.replace(marker, new_sections + "\n\n" + marker, 1)
    GLOSSARY.write_text(new_content, encoding="utf-8")

    total = sum(len(t) for t in NEW_TERMS.values())
    print(f"Added {total} new terms across {len(NEW_TERMS)} categories")

    # Update GLOSSARY_TERMS in generate_articles.py
    gen_content = GEN.read_text(encoding="utf-8")

    # Build new TERMS list ( longest first for proper replacement )
    all_terms = []
    for cat_terms in NEW_TERMS.values():
        for slug, term, _, _ in cat_terms:
            # Use first term part as key (some terms have alternatives like "U ターン ・ I ターン ・ J ターン")
            simple_term = term.split(" (")[0].split("（")[0]
            all_terms.append((simple_term, slug))

    # Sort by length descending
    all_terms.sort(key=lambda x: -len(x[0]))

    # Find GLOSSARY_TERMS in script and append
    pattern = re.compile(r'(GLOSSARY_TERMS = \[\n)((?:\s+\(.+\n)+)(\])', re.DOTALL)
    m = pattern.search(gen_content)
    if not m:
        print("ERROR: GLOSSARY_TERMS pattern not found")
        return

    existing_lines = m.group(2)
    new_entries = "\n".join(f'    ({term!r}, {slug!r}),' for term, slug in all_terms)
    new_block = m.group(1) + existing_lines + "    # --- expanded glossary ---\n" + new_entries + "\n" + m.group(3)

    new_gen_content = gen_content.replace(m.group(0), new_block)
    GEN.write_text(new_gen_content, encoding="utf-8")
    print(f"Updated GLOSSARY_TERMS with {len(all_terms)} new entries")


if __name__ == "__main__":
    main()
