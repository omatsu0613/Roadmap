import streamlit as st
import plotly.graph_objects as go
import math

# ─── ページ設定 ───────────────────────────────────────────────
st.set_page_config(
    page_title="キャリア相談シミュレーター",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── カスタムCSS ──────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=Shippori+Mincho:wght@400;600;700&display=swap');

/* ベースリセット */
html, body, [class*="css"] {
    font-family: 'Noto Sans JP', sans-serif;
    color: #1a1a2e;
}

/* 背景 */
.stApp {
    background: linear-gradient(135deg, #f8f6f0 0%, #fdf9f3 50%, #f5f0e8 100%);
    min-height: 100vh;
}

/* ヘッダー */
.main-header {
    background: linear-gradient(135deg, #1a1a2e 0%, #2d2d4e 100%);
    color: white;
    padding: 2.5rem 3rem;
    border-radius: 16px;
    margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(26, 26, 46, 0.2);
}
.main-header h1 {
    font-family: 'Shippori Mincho', serif;
    font-size: 2.2rem;
    font-weight: 700;
    margin: 0;
    letter-spacing: 0.05em;
    color: #f5e6c8;
}
.main-header p {
    margin: 0.5rem 0 0 0;
    color: #c9b99a;
    font-size: 0.9rem;
    font-weight: 300;
    letter-spacing: 0.08em;
}

/* セクションカード */
.section-card {
    background: white;
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 2px 16px rgba(26, 26, 46, 0.06);
    border: 1px solid rgba(26, 26, 46, 0.06);
}

/* セクションタイトル */
.section-title {
    font-family: 'Shippori Mincho', serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #1a1a2e;
    border-left: 4px solid #c9923c;
    padding-left: 1rem;
    margin-bottom: 1.5rem;
    letter-spacing: 0.03em;
}

/* セクション番号バッジ */
.section-badge {
    display: inline-block;
    background: #1a1a2e;
    color: #f5e6c8;
    border-radius: 50%;
    width: 28px;
    height: 28px;
    line-height: 28px;
    text-align: center;
    font-size: 0.8rem;
    font-weight: 700;
    margin-right: 0.6rem;
    vertical-align: middle;
}

/* divider */
.custom-divider {
    height: 2px;
    background: linear-gradient(90deg, #c9923c, transparent);
    margin: 2rem 0;
    border: none;
}

/* グラフカード */
.graph-card {
    background: white;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 4px 24px rgba(26, 26, 46, 0.08);
    border: 1px solid rgba(201, 146, 60, 0.2);
}

/* 設計図ボタン */
.stButton > button {
    background: linear-gradient(135deg, #1a1a2e 0%, #2d2d4e 100%) !important;
    color: #f5e6c8 !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 1rem 3rem !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    font-family: 'Noto Sans JP', sans-serif !important;
    letter-spacing: 0.06em !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
    box-shadow: 0 4px 20px rgba(26, 26, 46, 0.25) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(26, 26, 46, 0.35) !important;
}

/* アウトプットカード */
.output-card {
    background: linear-gradient(135deg, #1a1a2e 0%, #2d2d4e 100%);
    border-radius: 16px;
    padding: 2.5rem;
    color: white;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 32px rgba(26, 26, 46, 0.2);
}
.output-card h3 {
    font-family: 'Shippori Mincho', serif;
    color: #f5e6c8;
    font-size: 1.3rem;
    border-bottom: 1px solid rgba(245, 230, 200, 0.3);
    padding-bottom: 0.8rem;
    margin-bottom: 1.2rem;
}
.output-card p, .output-card li {
    color: #d4c4a8;
    line-height: 1.9;
    font-size: 0.95rem;
}
.output-card ul {
    padding-left: 1.5rem;
}
.highlight-gold {
    color: #f5e6c8;
    font-weight: 600;
}

/* ロードマップ */
.roadmap-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    border-left: 4px solid #c9923c;
    margin-bottom: 1rem;
    box-shadow: 0 2px 12px rgba(26, 26, 46, 0.06);
}
.roadmap-card h4 {
    font-family: 'Shippori Mincho', serif;
    color: #1a1a2e;
    font-size: 1.05rem;
    margin-bottom: 0.8rem;
}
.roadmap-card p, .roadmap-card li {
    color: #444;
    font-size: 0.9rem;
    line-height: 1.8;
}

/* チェックボックスグループ */
.checkbox-group {
    background: #fafaf8;
    border-radius: 10px;
    padding: 1rem 1.5rem;
    border: 1px solid #e8e4dc;
}

/* テキストエリア */
.stTextArea textarea {
    border-radius: 10px !important;
    border: 1px solid #ddd8ce !important;
    font-family: 'Noto Sans JP', sans-serif !important;
    font-size: 0.9rem !important;
    background: #fafaf8 !important;
}
.stTextInput input, .stSelectbox, .stNumberInput input {
    border-radius: 10px !important;
    border: 1px solid #ddd8ce !important;
    background: #fafaf8 !important;
}

/* スライダー */
.stSlider .stMarkdown {
    font-size: 0.85rem;
}

/* サブヘッダー */
.sub-label {
    font-size: 0.85rem;
    color: #888;
    margin-bottom: 0.3rem;
    letter-spacing: 0.02em;
}

/* info box */
.info-box {
    background: #fef9f0;
    border: 1px solid #f0d9a8;
    border-radius: 10px;
    padding: 1rem 1.5rem;
    margin-bottom: 1rem;
    font-size: 0.88rem;
    color: #7a5c2a;
}

/* priority badge */
.priority-badge {
    display: inline-block;
    background: #c9923c;
    color: white;
    border-radius: 20px;
    padding: 0.2rem 0.8rem;
    font-size: 0.8rem;
    font-weight: 700;
    margin-bottom: 0.8rem;
}

/* フッター */
.footer-note {
    text-align: center;
    color: #aaa;
    font-size: 0.8rem;
    padding: 2rem 0;
    letter-spacing: 0.05em;
}

/* Streamlit要素の調整 */
[data-testid="stExpander"] {
    border-radius: 10px !important;
    border: 1px solid #ddd8ce !important;
    background: white !important;
}
label[data-baseweb="checkbox"] span {
    font-size: 0.92rem;
}
.stRadio label {
    font-size: 0.92rem;
}
</style>
""", unsafe_allow_html=True)

# ─── ヘッダー ─────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>✦ 個別キャリア相談シミュレーター</h1>
    <p>CAREER DESIGN SIMULATOR ｜ ヒアリングシート & 収益シミュレーション</p>
</div>
""", unsafe_allow_html=True)

# ─── セクション1：基本プロフィール ────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title"><span class="section-badge">1</span>基本プロフィール</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    name = st.text_input("お名前", placeholder="例：山田 花子")
    age = st.number_input("年齢", min_value=18, max_value=80, value=35, step=1)
    gender = st.radio("性別", ["女性", "男性", "その他・回答しない"], horizontal=True)

with col2:
    income = st.number_input("現在の年収（万円）", min_value=0, max_value=5000, value=300, step=10)
    household_income = st.number_input("現在の世帯年収（万円）", min_value=0, max_value=10000, value=500, step=10)
    marital_status = st.radio("婚姻状況", ["未婚", "既婚"], horizontal=True)

with col3:
    has_children = st.radio("お子様の有無", ["なし", "あり"], horizontal=True)
    num_children = 0
    if has_children == "あり":
        num_children = st.number_input("お子様の人数", min_value=1, max_value=10, value=1, step=1)
    region = st.text_input("お住まいの地域", placeholder="例：東京都、大阪府")
    occupation = st.text_input("現在の職業", placeholder="例：医療事務、営業職")

st.markdown('</div>', unsafe_allow_html=True)

# ─── セクション2：経験の棚卸し ────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title"><span class="section-badge">2</span>経験の棚卸し</div>', unsafe_allow_html=True)

st.markdown('<div class="info-box">💬 ヒアリングしながら入力してください。職種・年数・担当業務など、思い出せる範囲でOKです。</div>', unsafe_allow_html=True)

career_history = st.text_area(
    "これまでの経歴",
    height=120,
    placeholder="例：医療事務を7年（レセプト業務・患者対応）、その後クリニック受付を3年（新人教育も担当）、直近3年は経理事務として請求管理を担当",
)

side_job_history = st.text_area(
    "副業歴",
    height=100,
    placeholder="例：5年前にブログアフィリエイトをスタート。トレンド記事中心でGoogleアドセンス収益。最高月収1万円、合計30記事以上投稿",
)

col1, col2 = st.columns(2)
with col1:
    has_blog = st.radio("ブログはお持ちですか？", ["なし", "あり（運用中）", "あり（休止中）"], horizontal=True)
    blog_years = st.selectbox("ブログ運用歴", ["なし", "1年未満", "1〜2年", "2〜3年", "3〜5年", "5年以上"])

with col2:
    current_revenue = st.number_input("現在の副業収益（月額・円）", min_value=0, max_value=10000000, value=0, step=1000)
    target_revenue = st.number_input("目標金額（月額・円）", min_value=0, max_value=10000000, value=100000, step=1000)
    best_result = st.text_input("過去の副業最高実績", placeholder="例：月収3万円、案件10件受注など")

st.markdown("**その他副業歴（複数選択可）**")
side_jobs_options = [
    "ライティング・ブログ", "Canvaデザイン", "SNS運用代行", "動画編集",
    "ハンドメイド販売", "フリマ・転売", "データ入力", "アンケートモニター",
    "家庭教師・講師", "コーチング・コンサル", "その他"
]
cols = st.columns(4)
selected_side_jobs = []
for i, job in enumerate(side_jobs_options):
    with cols[i % 4]:
        if st.checkbox(job, key=f"sj_{i}"):
            selected_side_jobs.append(job)

st.markdown('</div>', unsafe_allow_html=True)

# ─── セクション3：現在地と作業条件 ───────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title"><span class="section-badge">3</span>現在地と作業条件</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    daily_hours = st.select_slider(
        "1日に確保できる平均作業時間",
        options=[0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0],
        value=1.5,
        format_func=lambda x: f"{x}時間"
    )
    holiday_hours = st.select_slider(
        "休日に確保しやすい時間",
        options=[0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0],
        value=3.0,
        format_func=lambda x: f"{x}時間"
    )

with col2:
    holiday_style = st.text_input("休日の主な過ごし方", placeholder="例：子どもと外出、家でのんびり、趣味の時間")
    savings = st.number_input("現在の貯金額（万円）", min_value=0, max_value=100000, value=100, step=10)

hobbies = st.text_area(
    "趣味・特技・少しでも興味があること",
    height=80,
    placeholder="例：料理、旅行、読書、SNS閲覧、整理整頓が得意、人に教えるのが好き など"
)

st.markdown('</div>', unsafe_allow_html=True)

# ─── セクション4：申し込み理由・今後の目標 ──────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title"><span class="section-badge">4</span>申し込み理由・今後の目標</div>', unsafe_allow_html=True)

st.markdown("**4-1 個別相談に申し込んだ理由（複数選択可）**")
reasons_options = [
    "独学の試行錯誤を終わらせたい",
    "自分の経験がどんな仕事に変わるのか知りたい",
    "３ヶ月以内に収益の土台を作りたい",
    "書くだけではなく設計・整理・改善側に回りたい",
    "将来の収入不安に備えたい",
    "自分1人で判断し続けるやり方を終わらせたい",
    "自分に合うテーマや方向性を明確にしたい",
    "AI×Canva×ライティングを実務で使える形にしたい",
    "企業案件で型を学びながら自分の資産にもつなげたい",
    "体力勝負ではない働き方に切り替えたい",
    "家事・育児・仕事と両立できる別レールを作りたい",
    "個別に設計されたロードマップで進みたい",
]
cols = st.columns(2)
selected_reasons = []
for i, r in enumerate(reasons_options):
    with cols[i % 2]:
        if st.checkbox(r, key=f"reason_{i}"):
            selected_reasons.append(r)

st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

st.markdown("**4-2 今後の目標（複数選択可）**")
goals_options = [
    "半年以内に月３〜5万円の副収入の土台を作りたい",
    "会社以外の収入源を持ちたい",
    "自分のブログやSNSも資産化したい",
    "将来的にフリーランスや独立も視野に入れたい",
    "親の介護や将来の生活不安に備えたい",
    "1年以内に月10万円以上を安定して目指したい",
    "在宅でも続けやすい働き方を作りたい",
    "自分の経験を価値に変えられる働き方に移行したい",
    "子育てや家庭と両立しながら積み上げたい",
    "今の仕事を続けながら次のレールを準備したい",
]
cols = st.columns(2)
selected_goals = []
for i, g in enumerate(goals_options):
    with cols[i % 2]:
        if st.checkbox(g, key=f"goal_{i}"):
            selected_goals.append(g)

st.markdown('</div>', unsafe_allow_html=True)

# ─── セクション5：収益シミュレーター ─────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title"><span class="section-badge">5</span>収益シミュレーター</div>', unsafe_allow_html=True)

def calc_income(hours: float) -> tuple[int, int]:
    """作業時間から現実ライン・理想ラインを計算"""
    # 基準点: 0.5h→14000/17000, 1h→28000/33000, 4h→189000/223000
    # 非線形モデル（収穫逓増→逓減を考慮）
    if hours <= 0:
        return 0, 0
    # べき乗モデルでフィット
    real = int(28000 * (hours ** 1.05))
    ideal = int(33000 * (hours ** 1.05))
    # 0.5h補正
    if hours == 0.5:
        real, ideal = 14000, 17000
    return real, ideal

hours_range = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
real_values = []
ideal_values = []
for h in hours_range:
    r, i = calc_income(h)
    real_values.append(r)
    ideal_values.append(i)

# 手動補正で精度を上げる
preset = {
    0.5: (14000, 17000),
    1.0: (28000, 33000),
    1.5: (42000, 50000),
    2.0: (62000, 73000),
    2.5: (85000, 100000),
    3.0: (112000, 133000),
    3.5: (148000, 175000),
    4.0: (189000, 223000),
    4.5: (235000, 278000),
    5.0: (285000, 336000),
}
real_values = [preset[h][0] for h in hours_range]
ideal_values = [preset[h][1] for h in hours_range]

hour_labels = [f"{h}時間" for h in hours_range]

# 目標金額ライン
target = target_revenue if target_revenue > 0 else None

fig = go.Figure()

# 理想ライン
fig.add_trace(go.Scatter(
    x=hour_labels, y=ideal_values,
    mode='lines+markers',
    name='理想ライン',
    line=dict(color='#c9923c', width=3, dash='dot'),
    marker=dict(size=8, color='#c9923c', symbol='diamond'),
    fill='tonexty',
    fillcolor='rgba(201,146,60,0.08)',
    hovertemplate='<b>理想ライン</b><br>作業時間: %{x}<br>月収: ¥%{y:,}<extra></extra>'
))

# 現実ライン
fig.add_trace(go.Scatter(
    x=hour_labels, y=real_values,
    mode='lines+markers',
    name='現実ライン',
    line=dict(color='#2d2d4e', width=3),
    marker=dict(size=8, color='#2d2d4e'),
    hovertemplate='<b>現実ライン</b><br>作業時間: %{x}<br>月収: ¥%{y:,}<extra></extra>'
))

# 現在の作業時間マーカー
current_idx = hours_range.index(daily_hours)
fig.add_trace(go.Scatter(
    x=[hour_labels[current_idx]],
    y=[real_values[current_idx]],
    mode='markers',
    name=f'現在の設定（{daily_hours}時間）',
    marker=dict(size=16, color='#e85555', symbol='star', line=dict(color='white', width=2)),
    hovertemplate=f'<b>現在の設定</b><br>作業時間: {daily_hours}時間<br>現実ライン: ¥{real_values[current_idx]:,}<extra></extra>'
))

# 目標金額ライン
if target and target > 0:
    fig.add_hline(
        y=target,
        line=dict(color='#e85555', width=2, dash='dash'),
        annotation_text=f"  目標: ¥{target:,}",
        annotation_position="right",
        annotation_font=dict(color='#e85555', size=12)
    )

fig.update_layout(
    title=dict(
        text="1日の作業時間と月収シミュレーション",
        font=dict(family='Noto Sans JP', size=18, color='#1a1a2e'),
        x=0.02
    ),
    xaxis=dict(
        title="1日の作業時間",
        gridcolor='#f0ece4',
        tickfont=dict(family='Noto Sans JP', size=12)
    ),
    yaxis=dict(
        title="月収（円）",
        gridcolor='#f0ece4',
        tickformat='¥,.0f',
        tickfont=dict(family='Noto Sans JP', size=12)
    ),
    plot_bgcolor='white',
    paper_bgcolor='white',
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1,
        font=dict(family='Noto Sans JP', size=12)
    ),
    hovermode='x unified',
    margin=dict(l=20, r=80, t=60, b=40),
    height=420
)

st.plotly_chart(fig, use_container_width=True)

# シミュレーション結果サマリー
real_cur, ideal_cur = preset[daily_hours]
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        f"現実ライン（{daily_hours}時間/日）",
        f"¥{real_cur:,}",
        help="継続的に取り組んだ場合の現実的な月収目安"
    )
with col2:
    st.metric(
        f"理想ライン（{daily_hours}時間/日）",
        f"¥{ideal_cur:,}",
        help="スキルアップと効率化が進んだ場合の月収目安"
    )
with col3:
    if target_revenue > 0:
        diff = target_revenue - real_cur
        st.metric(
            "目標金額まであと",
            f"¥{abs(diff):,}",
            delta=f"{'あと' if diff > 0 else '達成余裕'} ¥{abs(diff):,}",
            delta_color="inverse" if diff > 0 else "normal"
        )
    else:
        st.metric("目標金額", "未設定")

st.markdown('</div>', unsafe_allow_html=True)

# ─── 設計図生成ボタン ──────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)

generate = st.button("✦ 個別専用キャリア設計図を作成する", use_container_width=True)

if generate:
    real_yr1 = real_cur
    ideal_yr1 = ideal_cur
    name_display = name if name else "あなた"
    occupation_display = occupation if occupation else "会社員"

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="text-align:center; padding: 1.5rem 0;">
        <div style="font-family:'Shippori Mincho',serif; font-size:1.8rem; color:#1a1a2e; letter-spacing:0.1em;">
            ✦ {name_display}さんの個別キャリア設計図
        </div>
        <div style="color:#c9923c; font-size:0.9rem; margin-top:0.5rem; letter-spacing:0.12em;">
            PERSONAL CAREER DESIGN PLAN
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ① ライフスタイル
    hobby_text = hobbies if hobbies else "趣味や家族との時間"
    children_text = f"お子様{num_children}人との" if has_children == "あり" and num_children > 0 else ""

    st.markdown(f"""
    <div class="output-card">
        <h3>① ライフスタイル ─ 副業をした場合の生活イメージ</h3>
        <p>
            副業をはじめると聞くと、<span class="highlight-gold">「今の生活が変わってしまうのでは」</span>と感じる方も多いです。<br><br>
            でも、{name_display}さんの場合は違います。<br><br>
            1日<span class="highlight-gold">{daily_hours}時間</span>という、生活の中の小さなすき間から始まります。
            {children_text}時間、{hobby_text}、大切にしている日々のリズム──その土台は、一切崩しません。<br><br>
            平日の夜、少しだけ画面に向かう時間を作る。休日に{holiday_hours}時間だけ集中する。それだけで、
            半年後には月<span class="highlight-gold">¥{real_yr1:,}〜{ideal_yr1:,}</span>という、
            ランチ数十回分・サブスク数本分・小さな旅行費用に相当する「別の収入」が動き始めます。<br><br>
            大切なのは、<span class="highlight-gold">一気に変えようとしないこと</span>。
            いまの生活をそのまま持ちながら、隣に小さな収入の畑を育てていくイメージです。
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ② 成功する人のルート
    yr1_real_display = f"{real_yr1 * 10 // 10000 * 10000:,}"
    yr1_ideal_display = f"{ideal_yr1 // 10000 * 10000 + 10000:,}"

    st.markdown(f"""
    <div class="output-card">
        <h3>② 成功する人のルート</h3>
        <p>
            まずは<span class="highlight-gold">企業ニーズに近い仕事で型を覚えます</span>。<br>
            次にフィードバックを受け、その型を自分のクライアントワークやブログ・SNSへ移す順番が合っています。<br><br>
            大切なのは、{name_display}さんが積み上げてきた経験──{occupation_display}としての知識や視点──を、
            <span class="highlight-gold">企業が使いやすい形として理解し、変換すること</span>です。<br><br>
            1日<span class="highlight-gold">{daily_hours}時間</span>の作業でも、
            1年目は<span class="highlight-gold">月¥{real_yr1:,}前後〜¥{ideal_yr1:,}前後</span>が
            現実ラインとして見えやすく、その後は「作業を受ける人」から
            <span class="highlight-gold">「改善を提案できる人」</span>へ寄せていくと、伸び方が安定します。
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ③ このまま何も行わなかった場合
    st.markdown(f"""
    <div class="output-card">
        <h3>③ このまま何も行わなかった場合</h3>
        <p><span class="highlight-gold">1. 何も変えないまま、時間だけが過ぎるパターン</span></p>
        <p>
            いまの『{occupation_display}』だけで毎日が回る状態が続くと、経験は増えても、
            それが副収入や資産に変わらないまま終わりやすいです。<br>
            とくに1日<span class="highlight-gold">{daily_hours}時間</span>を確保できるのに動かない状態が続くと、
            1年後も「不安はあったのに何も変わっていない」に戻りやすいです。
        </p>
        <br>
        <p><span class="highlight-gold">2. 少し動くが、自己流で遠回りするパターン</span></p>
        <p>
            型も順番も持たずに始めると、頑張っているつもりでも、収益に繋がらない作業だけが増えやすいです。<br>
            調べる・投稿する・作るを繰り返しても、<span class="highlight-gold">企業ニーズに合う形へ変換できないまま</span>だと、
            時間だけが先に消えていきます。
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ④ 高単価な価値に変わる具体的な作業内容
    st.markdown("""
    <div class="output-card">
        <h3>④ あなたの経験が高単価な価値に変わる具体的な作業内容</h3>
        
        <div style="margin-bottom:1.5rem;">
            <div class="priority-badge">優先順位１</div>
            <p><span class="highlight-gold">実務ライティングの仕事</span></p>
            <p>
                「書くだけ」では弱いですが、<span class="highlight-gold">構成・導線・見せ方まで入ると</span>、
                単なる執筆よりも企業成果に近い仕事になります。
            </p>
            <p><span class="highlight-gold">向きやすい案件：</span></p>
            <ul>
                <li>記事の見出し構成を作る</li>
                <li>リライトで読みやすさと導線を改善する</li>
                <li>ブログ・SNS・資料で使い回せるコンテンツ骨子を作る</li>
            </ul>
            <p><span class="highlight-gold">初心者が最初にやる作業：</span></p>
            <ul>
                <li>AIで構成案を作り、人が検索意図や伝える順番を整える</li>
                <li>1記事を「本文」「図解」「SNS要約」に分解して再利用する</li>
                <li>記事サンプルと改善前後の比較をポートフォリオ化する</li>
            </ul>
        </div>
        
        <div>
            <div class="priority-badge">優先順位２</div>
            <p><span class="highlight-gold">文章を図解・スライド・見せ方に変える仕事</span></p>
            <p>
                「作る」だけでなく「<span class="highlight-gold">伝わる形に直す</span>」ところまで入れるので、
                単純なデザイン外注より価値を出しやすいです。
            </p>
            <p><span class="highlight-gold">向きやすい案件：</span></p>
            <ul>
                <li>長い説明文を1枚図解に直す</li>
                <li>ブログ記事や営業資料をスライド形式に整える</li>
                <li>サービス案内や比較表を、初見でも理解できる見た目に変える</li>
            </ul>
            <p><span class="highlight-gold">初心者が最初にやる作業：</span></p>
            <ul>
                <li>AIで下書きを作り、要点だけを抜いたラフを作る</li>
                <li>Canvaで1テーマ1枚の図解サンプルを2本作る</li>
                <li>文章だけの説明を「見た瞬間に伝わる形」へ置き換える練習をする</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 90日ロードマップ
    st.markdown(f"""
    <div style="font-family:'Shippori Mincho',serif; font-size:1.3rem; color:#1a1a2e;
                border-left:4px solid #c9923c; padding-left:1rem; margin:2rem 0 1.5rem 0;">
        90日ロードマップ
    </div>
    """, unsafe_allow_html=True)

    roadmap_data = [
        {
            "title": "1ヶ月目｜現在地の把握と、最初の型づくり",
            "body": f"""平日夜の{min(daily_hours, 2.0)}〜{min(daily_hours + 0.5, 2.0)}時間を軸に、休日で整える前提で進めます。<br><br>
            <b>この月にやること</b><br>
            ・現在地の把握と、どの経験を価値に変えるかの整理<br>
            ・受注するための基本準備（プロフィール、肩書き、簡単な自己紹介）<br>
            ・AIで下書きを作り、Canvaや文章で見やすく整える型を1つ作る<br>
            ・最初のサンプルを1〜2個作る<br>
            ・案件応募の流れを知り、どこに出すかを決める<br><br>
            <b>この月のゴール</b><br>
            「何をやる人か」が一言で言える状態と、見せられるサンプルが最低1本ある状態を作ります。""",
        },
        {
            "title": "2ヶ月目｜小さく受注しながら、実務の型に慣れる",
            "body": """まずは小さな案件、模擬案件、または知人向けのサンプル対応で「最後まで出す経験」を作ります。<br><br>
            <b>この月にやること</b><br>
            ・お仕事の並行受注、または模擬案件で納品経験を増やす<br>
            ・コンテンツ制作の慣れを作り、Canva操作や修正対応に慣れる<br>
            ・継続受注につながるよう、成果物の見せ方を整える<br>
            ・ポートフォリオを作り、提案時に見せられる状態にする<br><br>
            <b>この月のゴール</b><br>
            「作れる」ではなく「<b>納品できる</b>」に変わること。ここで実務の流れを体で覚えます。""",
        },
        {
            "title": "3ヶ月目｜継続受注と、単価を上げる提案に進む",
            "body": """<b>この月にやること</b><br>
            ・継続受注を狙い、単発作業から抜ける提案を入れる<br>
            ・価値単価を上げるために、整理だけでなく改善提案まで含める<br>
            ・デザインや見せ方の幅を広げ、対応可能コンテンツを増やす<br>
            ・記事・図解・資料・導線改善など、関連する納品パターンを1つ増やす<br><br>
            <b>この月のゴール</b><br>
            「作業者」ではなく、<b>「整えて成果につなげる人」</b>として見てもらう段階に入ります。""",
        },
        {
            "title": "90日以降｜企業案件の型を、自分の資産にも移す",
            "body": """最初は企業案件側で型を覚え、その後に自分のブログやSNSの立ち上げへ進みます。<br><br>
            <b>この先の伸ばし方</b><br>
            ・企業案件で使った構成・導線・見せ方を、自分の発信にも流用する<br>
            ・自分の強みが刺さるテーマを固定し、発信の軸をぶらさない<br>
            ・自腹で手探りするのではなく、実務で学んだ型を自分資産へ移す""",
        },
    ]

    for rm in roadmap_data:
        st.markdown(f"""
        <div class="roadmap-card">
            <h4>✦ {rm["title"]}</h4>
            <p>{rm["body"]}</p>
        </div>
        """, unsafe_allow_html=True)

    # まとめカード
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #c9923c 0%, #e5a84d 100%);
                border-radius:16px; padding:2rem 2.5rem; margin-top:2rem;
                box-shadow:0 8px 32px rgba(201,146,60,0.3);">
        <div style="font-family:'Shippori Mincho',serif; font-size:1.2rem; color:white; margin-bottom:1rem;">
            ✦ {name_display}さんへのメッセージ
        </div>
        <p style="color:rgba(255,255,255,0.9); line-height:1.9; font-size:0.95rem;">
            1日{daily_hours}時間という時間を、「小さすぎる」と感じているかもしれません。<br>
            でもその積み重ねが、1年後には<b style="color:white;">月¥{real_yr1:,}〜¥{ideal_yr1:,}</b>という現実になります。<br><br>
            大切なのは、完璧な準備ではなく、<b style="color:white;">型を持って動き出すこと</b>。<br>
            {name_display}さんのこれまでの経験は、すでに価値に変わる素材を持っています。
            あとは、それを企業が使える形に変換する順番と方法を知るだけです。
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="footer-note">✦ このキャリア設計図は個別相談の内容をもとに生成されています ✦</div>', unsafe_allow_html=True)
