#!/usr/bin/env python3
"""Generate article HTML files for hokkaido-research."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ART_DIR = ROOT / "articles"

CAT_CLASS = {"課題発見": "discovery", "アイデア": "idea", "対談": "", "取材": ""}

ARTICLES = [
    {
        "id": "migration-residual-assets-2026-06",
        "title": "定着率では測れない - 移住定住で「残る資産」を見る",
        "category": "課題発見",
        "publishedAt": "2026-06-12",
        "readMinutes": 2,
        "relatedIssueIds": ["migration"],
        "summary": "「何人来たか」では地域に何が残るかを測れない。事業・関係・仕組みの 3 資産で評価する視点を提案。",
        "body": [
            ("p", "数値だけで議論される移住定住政策。しかし「何人来たか」では、地域に何が残るかを測れない。"),
            ("p", "北海道の自治体は毎年「転入超過数」「移住相談件数」を公表する。だが、数年後にその移住者が離れたとき、地域には何が残るのか。"),
            ("p", "定着率を追えば、人の流動を止めようとする発想になる。残る資産を追えば、人が変わっても回る仕組みを作る発想になる。"),
            ("h2", "3 つの資産で評価する"),
            ("p", "移住者が地域に残せるものは、大きく 3 種類に分けて考えると実践的だ。"),
            ("p", "<strong>事業資産</strong>: 起業した事業、継業した店舗、加工所。担い手が代わっても回り続けるもの。"),
            ("p", "<strong>関係資産</strong>: 移住者が外から連れてきた人脈、関係人口、企業連携。本人が離れても残る。"),
            ("p", "<strong>仕組み資産</strong>: お試し滞在の体制、移住相談の運用、地域内マッチングの仕掛け。属人化を抜いて残せる。"),
            ("p", "定着率を見ると「いま何人いるか」しか映らない。残る資産を見ると「3 年後・10 年後に何が残るか」が見える。"),
            ("h2", "評価軸を組み替える意味"),
            ("p", "評価軸が変わると、施策の優先順位が変わる。住宅手当の額より、伴走者の質。家賃補助より、起業の機会。"),
            ("p", "短期的な「来てもらう」より、長期的な「残せるものを作る」設計に向かう。"),
            ("p", "道内のいくつかの自治体はすでにこの転換を始めている。次の記事では、海士町・神山町の長期事例から具体的なヒントを読み解く。"),
        ],
    },
    {
        "id": "migration-longterm-cases-2026-06",
        "title": "17 年、15 年継続する町に共通するもの - 海士町・神山町の長期視点",
        "category": "アイデア",
        "publishedAt": "2026-06-12",
        "readMinutes": 2,
        "relatedIssueIds": ["migration"],
        "summary": "海士町と神山町に共通するのは「長期継続」と「仕組み化」。設備でなく、組織・関係・運用の積み上げ。",
        "body": [
            ("p", "全国に注目される移住成功事例の代表が、島根県海士町と徳島県神山町だ。共通するのは「17 年、15 年と継続している」こと。"),
            ("p", "短期で効く施策ではない。長期視点でしか作れない資産を作っている。"),
            ("h2", "海士町: 教育を地域の核に"),
            ("p", "人口約 2,300 人の離島、海士町。2008 年に始まった「島前高校魅力化プロジェクト」。"),
            ("p", "廃校危機にあった県立高校を、地域・行政・学校で一体運営。島外から生徒を呼ぶ「島留学」、地域協働カリキュラム、卒業生を地域人材として育てる流れ。"),
            ("p", "17 年継続することで、卒業生のネットワーク、教員の知見、地域住民の関わり方が「資産」として蓄積された。"),
            ("h2", "神山町: サテライトオフィスとつなぐ公社"),
            ("p", "人口約 4,800 人の山間部、神山町。2010 年代初頭から「神山町は緑のシリコンバレー」と言われ始めた。"),
            ("p", "IT 企業 16 社以上のサテライトオフィス進出。2023 年には「神山まるごと高専」開校。NPO 法人グリーンバレー、神山つなぐ公社等が、地域と外をつなぐハブとして機能している。"),
            ("p", "15 年継続することで、「神山に来る」という選択肢自体が外部の若手にとって自然になった。"),
            ("h2", "共通項: 仕組みを残す"),
            ("p", "両者とも、特定の個人の情熱に頼らない。組織として、仕組みとして、関係として、長期に残るものを設計している。"),
            ("p", "道内自治体が真似るとき、設備よりも合意形成と運営体制を真似るべきだ。設備は数年で陳腐化するが、仕組みは 20 年効く。"),
        ],
    },
    {
        "id": "furusato-nozei-asset-question-2026-06",
        "title": "ふるさと納税は地方財源か、それとも関係資産か",
        "category": "課題発見",
        "publishedAt": "2026-06-12",
        "readMinutes": 2,
        "relatedIssueIds": ["furusato-nozei"],
        "summary": "ふるさと納税を短期収入として扱うか、長期の関係資産として扱うか。評価軸の選択が施策を分ける。",
        "body": [
            ("p", "ふるさと納税の全国市場規模は 2023 年度に約 1.1 兆円。北海道は紋別市、根室市など毎年 100 億円超の自治体を多く抱え、地方財源として大きな存在になった。"),
            ("p", "しかし、制度改正が起きるたび、自治体は戦略変更を迫られる。2019 年の規制強化、2023 年の経費 50% ルール、そして今後の見直し可能性。"),
            ("p", "ふるさと納税は、地方自治体にとって「短期的な現金収入」なのか、それとも「長期的な関係資産」なのか。"),
            ("h2", "現金収入として見れば"),
            ("p", "寄附金額が地域の財源になる、というシンプルな構造。返礼品競争で寄附を集める、中間業者に手数料を払う、残った分を一般財源に組み込む。"),
            ("p", "メリットは即効性。デメリットは制度依存。改正一つで自治体財政が揺らぐ脆弱性を抱える。"),
            ("h2", "関係資産として見れば"),
            ("p", "寄附者は単に「お得な買い物をした人」ではなく、地域に関心を持った人々。その関心を継続的な関係に育てれば、関係人口、観光客、リピーター、移住検討者にもなりうる。"),
            ("h2", "評価軸を変える"),
            ("p", "「今年いくら集まったか」より、「3 年前の寄附者で今も関係が続いているのは何人か」「寄附者からどれだけのリピーターが生まれたか」を測る。"),
            ("p", "短期目標と長期戦略は両立できる。短期で財源を確保しながら、長期で関係資産を育てる設計。寄附者リストを CRM として運用するか、データを箱の中で眠らせるかは、自治体の判断次第だ。"),
            ("p", "次の記事では、関係人口化への具体的な 4 つの転換を読み解く。"),
        ],
    },
    {
        "id": "furusato-nozei-transition-2026-06",
        "title": "寄附から関係人口へ - ふるさと納税の 4 つの転換",
        "category": "アイデア",
        "publishedAt": "2026-06-12",
        "readMinutes": 2,
        "relatedIssueIds": ["furusato-nozei"],
        "summary": "短期収入から長期関係資産への移行に必要な 4 つの具体的なステップを整理。",
        "body": [
            ("p", "ふるさと納税を「短期収入」から「長期の関係資産」に転換するための、4 つの具体的なステップ。"),
            ("h2", "1. お礼状から物語へ"),
            ("p", "返礼品送付で関係を終わらせない。寄附者ごとに、自治体の取り組みや成果を伝える物語を継続的に届ける。"),
            ("p", "商品の背景にいる生産者の話、地域の取り組みの進捗、寄附がどう使われたかの可視化。これらは寄附者を「お買い物客」から「ファン」に変える可能性を持つ。"),
            ("h2", "2. 単発寄附から継続寄附へ"),
            ("p", "ふるさと納税の多くは年 1 回の単発。だが、年 2 回、3 回と継続する寄附者を育てれば関係は深まる。"),
            ("p", "ふるなび、ふるさとチョイス等のポータルでは「定期便」やリピート機能が拡大中。継続率を KPI に加える自治体が増えている。"),
            ("h2", "3. ガバメントクラウドファンディング ( GCF ) の活用"),
            ("p", "返礼品競争を離れ、課題解決型寄附で寄附者に「投資先」感覚を持ってもらう。"),
            ("p", "脱炭素、教育、福祉、防災等の具体プロジェクトに紐づける。寄附者は「結果を見たい」と思うので、進捗報告が自然と関係を継続させる。"),
            ("h2", "4. 寄附者を訪問者に変える"),
            ("p", "寄附者向けの現地体験、ふるさと納税限定の地域訪問プログラム。返礼品 + 体験の組み合わせは、関係人口化の最も強い経路。"),
            ("p", "ふるさと納税の本質的価値は、自治体と寄附者の関係を可視化する仕組みを持っていること。制度改正リスクを減らすのは、寄附額の最大化より、関係の蓄積だ。"),
        ],
    },
    {
        "id": "vacant-houses-perspective-2026-06",
        "title": "空き家を負担から資源に - 視点転換が変える施策",
        "category": "課題発見",
        "publishedAt": "2026-06-12",
        "readMinutes": 2,
        "relatedIssueIds": ["vacant-houses"],
        "summary": "「いかに減らすか」から「誰が、何のために使うか」へ。視点転換で空き家施策の全体像が変わる。",
        "body": [
            ("p", "北海道の空き家は約 38 万戸 ( 2023 年住宅・土地統計調査 ) 。10 年で約 1.4 倍に増えた。"),
            ("p", "多くの自治体は空き家を「負担」として扱う。固定資産税の優遇措置撤回、解体補助、特定空家対策。問題は「いかに減らすか」。"),
            ("p", "しかし、人口減少が止まらない以上、空き家を負担として扱う発想だけでは追いつかない。"),
            ("h2", "負担から資源への転換"),
            ("p", "視点を変える。空き家は「人がいない場所」ではなく「使える場所」。誰が、何のために使うか。それを設計するのが施策の本質。"),
            ("h2", "移住者向けの拠点"),
            ("p", "長期不在の住宅は、適切な改修で移住者の住まいになる。空き家バンク、リフォーム補助、家賃補助。すでに多くの自治体が取り組む典型例。"),
            ("h2", "起業のスペース"),
            ("p", "サテライトオフィス、コワーキングスペース、加工所、ゲストハウス。空き家は「住む」だけでなく「働く」「営む」場所にもなる。"),
            ("h2", "地域コミュニティの場"),
            ("p", "カフェ、子ども食堂、シェアスペース。地域住民が集まる場として再生する事例も多い。"),
            ("h2", "3 つの視点をつなぐ"),
            ("p", "成功する空き家施策は、移住・起業・コミュニティの 3 つを統合的に扱う。"),
            ("p", "「住む人を探す」「使う事業を探す」「集まる活動を支える」を別々の窓口でなく、空き家を中心にひとつの戦略として組み立てる。"),
            ("p", "20 年単位で見れば、空き家は地域の再生のための土地と建物の在庫だ。"),
            ("p", "次の記事では、25 年継続する尾道市の事例から、長期的な空き家再生の仕組みを読み解く。"),
        ],
    },
    {
        "id": "vacant-houses-onomichi-2026-06",
        "title": "25 年の継続が作る空き家再生 - 尾道に学ぶ仕組み",
        "category": "アイデア",
        "publishedAt": "2026-06-12",
        "readMinutes": 2,
        "relatedIssueIds": ["vacant-houses"],
        "summary": "尾道空き家再生プロジェクト 20 年。設備でも補助金でもなく、組織・関わり方・循環を残した。",
        "body": [
            ("p", "広島県尾道市。坂の街として知られる人口約 13 万人の地方都市。"),
            ("p", "ここで 2007 年から始まった NPO 法人「尾道空き家再生プロジェクト」は、空き家対策の代表的な長期事例として全国に知られる。"),
            ("p", "20 年近く継続することで、何が積み上がったのか。"),
            ("h2", "始まりは個人の問題意識"),
            ("p", "代表理事の豊田雅子氏は、自宅近くで朽ちていく古民家を見て「もったいない」と感じたことから始めた。"),
            ("p", "行政の施策でも、補助金事業でもない。一人の問題意識を、地域の運動に育てた。"),
            ("h2", "少額からの参加"),
            ("p", "会員制度を作り、市民が「サポート会員」「修繕会員」として関わる仕組みを整備。"),
            ("p", "専門家でなくても、空き家再生に参加できる。これが市民の関わり方を広げ、「地域の課題は地域で解決する」感覚を育てた。"),
            ("h2", "移住者の循環"),
            ("p", "再生した空き家は、移住者・若手起業家・アーティストに貸し出される。"),
            ("p", "入居者が次の物件の再生に関わる。出ていく人も「尾道に関わる関係人口」になる。循環構造が長期に維持される。"),
            ("h2", "学ぶべきこと"),
            ("p", "設備でも補助金でもない。継続する組織・関わる仕組み・循環する関係。"),
            ("p", "これらは 1 - 2 年では作れない。20 年の継続が、「尾道で家を借りる」「尾道に関わる」という選択肢を、外部の人にとって自然なものにした。"),
            ("p", "道内の自治体が空き家対策を進めるとき、即効性のある施策と並行して、20 年以上続けられる組織と仕組みを設計することが、長期的な成果を分ける。"),
        ],
    },
]


def render_body(blocks):
    parts = []
    for tag, text in blocks:
        if tag == "h2":
            parts.append(f"<h2>{text}</h2>")
        elif tag == "p":
            parts.append(f"<p>{text}</p>")
    return "\n".join(parts)


def format_date_jp(iso_date):
    y, m, d = iso_date.split("-")
    return f"{y} 年 {int(m)} 月 {int(d)} 日"


# JS that runs in each article to populate related sections from data.js
RELATED_JS = """
<script src="/data.js"></script>
<script>
(function(){
  var ARTICLE_ID = "__ARTICLE_ID__";
  var RELATED_IDS = __RELATED_IDS__;

  function esc(s){ return String(s||"").replace(/[<>&"]/g, function(c){
    return {"<":"&lt;",">":"&gt;","&":"&amp;",'"':"&quot;"}[c];
  });}

  // 1. 関連する課題
  var issuesEl = document.getElementById("rel-issues");
  if(issuesEl && typeof ISSUES !== "undefined"){
    var matches = ISSUES.filter(function(i){ return RELATED_IDS.indexOf(i.id) >= 0; });
    if(matches.length){
      issuesEl.innerHTML = matches.map(function(i){
        var cat = (typeof CATEGORIES !== "undefined" && CATEGORIES[i.cat]) ? CATEGORIES[i.cat].label : "";
        return '<a class="rel-card" href="/?issue=' + i.id + '">' +
          '<div class="rel-card-meta">' + esc(cat) + '</div>' +
          '<div class="rel-card-title">' + esc(i.title) + '</div>' +
          '<div class="rel-card-sum">' + esc(i.summary||"") + '</div>' +
          '</a>';
      }).join("");
    }
  }

  // 2. 関連する取り組み (initiatives in matched issues)
  var initEl = document.getElementById("rel-initiatives");
  if(initEl && typeof ISSUES !== "undefined"){
    var inits = [];
    ISSUES.forEach(function(i){
      if(RELATED_IDS.indexOf(i.id) < 0) return;
      (i.initiatives||[]).forEach(function(it){ inits.push(it); });
    });
    inits = inits.slice(0, 5);
    if(inits.length){
      initEl.innerHTML = inits.map(function(it){
        return '<div class="rel-init">' +
          '<div class="rel-init-where">' + esc(it.where||"") + '</div>' +
          '<div class="rel-init-name">' + esc(it.name||"") + '</div>' +
          '<div class="rel-init-desc">' + esc(it.desc||it.summary||"") + '</div>' +
          '</div>';
      }).join("");
    } else {
      initEl.parentElement.style.display = "none";
    }
  }

  // 3. 関連するデータ (stats)
  var statsEl = document.getElementById("rel-stats");
  if(statsEl && typeof ISSUES !== "undefined"){
    var stats = [];
    ISSUES.forEach(function(i){
      if(RELATED_IDS.indexOf(i.id) < 0) return;
      (i.stats||[]).forEach(function(s){ stats.push(s); });
    });
    stats = stats.slice(0, 4);
    if(stats.length){
      statsEl.innerHTML = stats.map(function(s){
        var v = s.value || s.v || "";
        var l = s.label || s.k || "";
        return '<div class="rel-stat">' +
          '<div class="rel-stat-v">' + esc(v) + '</div>' +
          '<div class="rel-stat-l">' + esc(l) + '</div>' +
          '</div>';
      }).join("");
    } else {
      statsEl.parentElement.style.display = "none";
    }
  }

  // 4. 他の関連記事
  var artEl = document.getElementById("rel-articles");
  if(artEl && typeof ARTICLES !== "undefined"){
    var others = ARTICLES.filter(function(a){
      if(a.id === ARTICLE_ID) return false;
      return (a.relatedIssues||[]).some(function(x){ return RELATED_IDS.indexOf(x) >= 0; });
    }).sort(function(a,b){
      return (b.publishedAt||"").localeCompare(a.publishedAt||"");
    });
    if(others.length){
      artEl.innerHTML = others.map(function(a){
        var catCls = a.category === "課題発見" ? "discovery" : (a.category === "アイデア" ? "idea" : "");
        return '<a class="rel-art" href="/articles/' + a.id + '.html">' +
          '<span class="rel-art-cat ' + catCls + '">' + esc(a.category) + '</span>' +
          '<div class="rel-art-title">' + esc(a.title) + '</div>' +
          '<div class="rel-art-meta">' + esc(a.publishedAt) + ' ・ ' + (a.readMinutes||2) + ' 分</div>' +
          '</a>';
      }).join("");
    } else {
      artEl.parentElement.style.display = "none";
    }
  }
})();
</script>
"""


TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}｜北海道・地域課題リサーチ</title>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" href="/favicon.svg">
<meta name="description" content="{summary}">
<meta property="og:title" content="{title}｜北海道・地域課題リサーチ">
<meta property="og:description" content="{summary}">
<meta property="og:type" content="article">
<meta property="og:url" content="https://hokkaido-research.lrg.jp/articles/{id}.html">
<meta property="og:image" content="https://hokkaido-research.lrg.jp/og-image.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/articles/_article_styles.css">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-3FN8N9DLPP"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-3FN8N9DLPP');
</script>
</head>
<body>
<div class="article-wrap">
<a class="back-link" href="/">← トップへ戻る</a>

<header class="article-head">
<div class="article-meta-row">
<span class="article-cat {cat_class}">{category}</span>
<span class="article-date">{date_jp}</span>
<span class="article-time">{minutes} 分で読める</span>
</div>
<h1 class="article-title">{title}</h1>
<p class="article-summary">{summary}</p>
<div class="article-author">hokkaido-research 編集部</div>
</header>

<article class="body">
{body_html}
</article>

<section class="rel-section">
  <h3 class="rel-h">関連する課題</h3>
  <div id="rel-issues" class="rel-issues"></div>
</section>

<section class="rel-section">
  <h3 class="rel-h">関連する取り組み</h3>
  <div id="rel-initiatives" class="rel-initiatives"></div>
</section>

<section class="rel-section">
  <h3 class="rel-h">関連するデータ</h3>
  <div id="rel-stats" class="rel-stats"></div>
</section>

<section class="rel-section">
  <h3 class="rel-h">他の関連記事</h3>
  <div id="rel-articles" class="rel-articles"></div>
</section>

<a class="back-cta" href="/">← 記事一覧 ・ トップへ戻る</a>

<footer>
<p>運営: Largo 株式会社 ( <a href="https://lrg.jp" target="_blank" rel="noopener">lrg.jp</a> )</p>
<p>お問い合わせ ・ 提携 ・ 連携: <a href="https://x.com/h_ohigashi" target="_blank" rel="noopener">運営者 ( X )</a></p>
<p><a href="/terms.html">利用規約</a> ・ <a href="/privacy.html">プライバシーポリシー</a></p>
</footer>
</div>
{related_js}
</body>
</html>
"""


def main():
    ART_DIR.mkdir(exist_ok=True)
    import json as _json

    for a in ARTICLES:
        body_html = render_body(a["body"])
        related_js = (
            RELATED_JS
            .replace("__ARTICLE_ID__", a["id"])
            .replace("__RELATED_IDS__", _json.dumps(a["relatedIssueIds"]))
        )
        html = TEMPLATE.format(
            title=a["title"],
            summary=a["summary"],
            id=a["id"],
            cat_class=CAT_CLASS.get(a["category"], ""),
            category=a["category"],
            date_jp=format_date_jp(a["publishedAt"]),
            minutes=a["readMinutes"],
            body_html=body_html,
            related_js=related_js,
        )
        out = ART_DIR / f"{a['id']}.html"
        out.write_text(html, encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")

    # ARTICLES JS snippet for data.js
    js_lines = ["const ARTICLES = ["]
    for a in ARTICLES:
        js_lines.append("  {")
        js_lines.append(f'    id: "{a["id"]}",')
        js_lines.append(f'    title: "{a["title"]}",')
        js_lines.append(f'    category: "{a["category"]}",')
        js_lines.append(f'    publishedAt: "{a["publishedAt"]}",')
        js_lines.append(f'    readMinutes: {a["readMinutes"]},')
        related_arr = ", ".join(f'"{r}"' for r in a["relatedIssueIds"])
        js_lines.append(f'    relatedIssues: [{related_arr}],')
        js_lines.append(f'    summary: "{a["summary"]}",')
        js_lines.append("  },")
    js_lines.append("];")
    (ROOT / "_articles_data_snippet.js").write_text("\n".join(js_lines), encoding="utf-8")
    print("\nARTICLES snippet written to _articles_data_snippet.js")


if __name__ == "__main__":
    main()
