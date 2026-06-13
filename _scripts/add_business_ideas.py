#!/usr/bin/env python3
"""5 つの主要 ISSUE に businessIdeas フィールドを追加するスクリプト。

対象: elderly-care-staff / fisheries-climate / low-birthrate / rail-transit / energy-security
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data.js"

IDEAS = {
    "elderly-care-staff": [
        {
            "title": "広域介護シェアプラットフォーム",
            "target": "道内中小介護事業者 ・ 自治体",
            "revenueModel": "月額 SaaS + 派遣手数料",
            "mechanism": "複数市町村のヘルパー ・ 看護師を 1 つのシフト管理 ・ 移動 ・ 報酬システムで広域シェア。 道北 ・ オホーツク等の人材不足地域へ道央から週次派遣。",
            "combo": "JR北海道 / 道北バス + 自動運転バス + ICT 見守りデバイス",
        },
        {
            "title": "外国人介護人材一気通貫支援サービス",
            "target": "ベトナム ・ フィリピン ・ インドネシア介護人材 + 道内事業者",
            "revenueModel": "成功報酬 + 住宅 ・ 日本語学習サブスク",
            "mechanism": "雇用契約 ・ ビザ ・ 住宅 ・ 日本語 ・ 生活支援 ・ コミュニティ参加を 1 社で提供。 道内自治体 ・ 大学 ・ 不動産と連携し人材リテンションを確保。",
            "combo": "ふるさと納税 ( 企業版 ) + 道内多文化共生センター",
        },
    ],
    "fisheries-climate": [
        {
            "title": "道内陸上養殖ブランド統合ハブ",
            "target": "道内陸上養殖事業者 ・ 投資家",
            "revenueModel": "ブランドライセンス + 共同販売手数料",
            "mechanism": "上士幌 ・ 苫小牧 ・ 八雲等で進む陸上サーモン ・ サバ ・ チョウザメを「北海道陸上養殖」統一ブランドで束ね、 出荷 ・ EC ・ B2B 営業を共同化。",
            "combo": "北海道経済産業局 + 北電再エネ PPA + EC 産地直販",
        },
        {
            "title": "北海道ブリ ・ 新魚種ブランディングサブスク",
            "target": "首都圏 ・ 海外の高所得層 ・ 飲食店",
            "revenueModel": "月額定期便 + 季節限定プレミアム",
            "mechanism": "気候変動で増えた新魚種を月額定期便で出荷。 漁港ごとの顔の見える生産者ストーリーと組み合わせて、 量ではなく単価で勝負。",
            "combo": "ふるさと納税返礼 + SNS 産地ライブ",
        },
    ],
    "low-birthrate": [
        {
            "title": "道内子育てインフラスコア + 移住エージェント",
            "target": "道外子育て世代 ・ 自治体 ・ 不動産会社",
            "revenueModel": "成約手数料 + 自治体 SaaS",
            "mechanism": "道内 179 市町村の子育て支援 ・ 学校 ・ 保育 ・ 医療 ・ 物価 ・ 通勤性 を統合スコア化。 道外世帯にマッチング + 物件 + 移住手続を一気通貫サポート。",
            "combo": "ふるさと納税 + 自治体補助金 + JR / 航空アライアンス",
        },
        {
            "title": "保育士コミュニティ + 道内自治体送客 SaaS",
            "target": "保育士 ・ 学童指導員 ・ 道内自治体",
            "revenueModel": "月額 SaaS + 採用成功報酬",
            "mechanism": "全国の保育士向けコミュニティを運営し、 道内子育て先進自治体への移住 ・ 転職を支援。 住宅 + キャリアパスをセット提案。",
            "combo": "自治体住宅手当 + 北海道大学 ・ 教育大の養成課程",
        },
    ],
    "rail-transit": [
        {
            "title": "道内 MaaS スーパーアプリ",
            "target": "観光客 ・ 通勤者 ・ 自治体 ・ 観光関連事業者",
            "revenueModel": "サブスク + 加盟手数料 + 広告",
            "mechanism": "JR ・ バス ・ 第三セクター ・ タクシー ・ ライドシェア ・ レンタカー ・ シェアサイクルを 1 つのアプリで横断検索 ・ 予約 ・ 決済。",
            "combo": "ふるさと納税 + 観光 DMO + JR / 道内航空",
        },
        {
            "title": "過疎地域デマンドモビリティ SaaS",
            "target": "道内過疎自治体 ・ 高齢者向け事業者",
            "revenueModel": "自治体 SaaS + ライドシェア手数料",
            "mechanism": "予約型デマンド交通 ・ ライドシェア ・ 自動運転バスを 1 つのプラットフォームで運営。 高齢者 ・ 観光客 ・ 通学 ・ 物流の混載で運行効率を上げる。",
            "combo": "JR 北海道 + 道内バス事業者 + 地域おこし協力隊",
        },
    ],
    "energy-security": [
        {
            "title": "道内自治体マイクログリッド SaaS + 運営代行",
            "target": "道内市町村 ・ JA ・ 漁協 ・ 商工会",
            "revenueModel": "月額 SaaS + 運営代行手数料 + 売電収入分配",
            "mechanism": "上士幌型マイクログリッドを 30-50 自治体に横展開。 バイオガス ・ PV ・ 蓄電池 ・ EV 充電を統合制御。",
            "combo": "環境省脱炭素先行地域 + 北電 + 道内大学",
        },
        {
            "title": "ラピダス需要対応 PPA + 蓄電池ファンド",
            "target": "半導体 ・ データセンター事業者 ・ 機関投資家",
            "revenueModel": "PPA 売電 + ファンド運用",
            "mechanism": "ラピダス + データセンター + 半導体集積向けに長期 PPA を組み、 再エネ + 蓄電池 + 需給シフトでベースロード供給。 道内余剰再エネを需要側に直接届ける。",
            "combo": "千歳市 + 道庁ゼロカーボン推進局 + JBIC ・ DBJ",
        },
    ],
}


def ideas_js(items):
    """Python dict list を JS 配列 ( 4 space indent ) として整形。"""
    lines = ["    businessIdeas: ["]
    for it in items:
        lines.append("      {")
        for k in ("title", "target", "revenueModel", "mechanism", "combo"):
            v = it.get(k, "").replace('"', '\\"')
            lines.append(f'        {k}: "{v}",')
        lines.append("      },")
    lines.append("    ],")
    return "\n".join(lines)


content = DATA.read_text(encoding="utf-8")

for issue_id, items in IDEAS.items():
    pattern = re.compile(
        r'(id:\s*"' + re.escape(issue_id) + r'"[\s\S]+?habits:\s*\[\s*[\s\S]*?\]\s*,?)',
        re.DOTALL,
    )
    m = pattern.search(content)
    if not m:
        print(f"× {issue_id} not found")
        continue
    block = m.group(1)
    if "businessIdeas" in block:
        print(f"⚠ {issue_id} already has businessIdeas")
        continue
    # block の末尾 ( habits: [ ... ] , または habits: [ ... ] ) の後ろに追加
    new_block = block.rstrip().rstrip(",") + ",\n" + ideas_js(items)
    content = content[: m.start()] + new_block + content[m.end():]
    print(f"✓ {issue_id} に {len(items)} 件追加")

DATA.write_text(content, encoding="utf-8")
print("done")
