import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="さいしん・若者応援プロジェクト", layout="centered")

# 2. カスタムCSS
st.markdown("""
    <style>
    .main { background-color: #f9fbf9; }
    .block-container { padding-top: 3rem; max-width: 800px; }

    /* --- ロゴとユーティリティメニューの配置 --- */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
    .fake-logo {
        font-family: sans-serif;
        font-size: 26px;
        font-weight: bold;
        color: #4a4a4a;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .logo-mark {
        background: linear-gradient(135deg, #e60012 50%, #f39800 50%);
        color: white;
        border-radius: 50%;
        width: 36px;
        height: 36px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 22px;
        font-style: italic;
    }
    .utility-menu {
        display: flex;
        align-items: center;
        gap: 15px;
        font-size: 12px;
    }
    .utility-link { color: #333; text-decoration: none; }
    .utility-link:hover { text-decoration: underline; }
    .utility-btn-red {
        background-color: #e60012;
        color: white !important;
        padding: 8px 16px;
        border-radius: 4px;
        text-decoration: none;
        font-weight: bold;
    }

    /* --- Streamlitのタブを「さいしん風」にカスタマイズ --- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        background-color: #e60012; /* タブ全体の背景を赤に */
        border-radius: 5px 5px 0 0;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        white-space: pre-wrap;
        background-color: #e60012;
        color: white; /* 非アクティブ時の文字色 */
        border-radius: 0;
        border-left: 1px solid #ff4d4d;
        flex: 1; /* 等分配置 */
    }
    .stTabs [data-baseweb="tab"]:first-child { border-left: none; }
    /* 選択されているタブのデザイン */
    .stTabs [aria-selected="true"] {
        background-color: white !important;
        color: #333 !important;
        border-top: 4px solid #e60012;
    }
    
    /* --- サブメニュー（タブの中身）のデザイン --- */
    .sub-menu-container {
        display: flex;
        background-color: white;
        border-bottom: 1px solid #ddd;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-top: -15px; /* Streamlit特有の隙間を埋める */
        margin-bottom: 20px;
    }
    .sub-item {
        flex: 1;
        text-align: center;
        padding: 12px 5px;
        font-size: 12px;
        font-weight: bold;
        color: #333;
        border-right: 1px solid #f0e1e1;
    }
    .sub-item:last-child { border-right: none; }
    .arrow { color: #f39800; font-size: 10px; margin-left: 5px; }

    /* --- 追従ボタン --- */
    .sticky-btn {
        position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%);
        background-color: #e60012; color: white !important; padding: 15px 30px;
        border-radius: 50px; font-weight: bold; text-decoration: none;
        z-index: 999; box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        width: 90%; max-width: 760px; text-align: center; font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. ヘッダー描画（ロゴと右上のメニュー）
st.markdown("""
    <div class="header-container">
        <div class="fake-logo"><div class="logo-mark">S</div>埼玉縣信用金庫</div>
        <div class="utility-menu">
            <a href="#" class="utility-link">お問合せ・ご意見</a>
            <a href="#" class="utility-link">よくあるご質問</a>
            <a href="#" class="utility-btn-red">口座開設</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. メインタブの作成
tab1, tab2, tab3, tab4 = st.tabs([
    "個人のお客さま", 
    "法人（個人事業主）のお客さま", 
    "《さいしん》について", 
    "採用のご案内"
])

# 5. 各タブの中身（サブメニュー）
with tab1:
    st.markdown("""
        <div class="sub-menu-container">
            <div class="sub-item">ためる・ふやす <span class="arrow">▼</span></div>
            <div class="sub-item">かりる <span class="arrow">▼</span></div>
            <div class="sub-item">そなえる <span class="arrow">▼</span></div>
            <div class="sub-item">便利に使う <span class="arrow">▼</span></div>
            <div class="sub-item">相談・手続きする <span class="arrow">▼</span></div>
        </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
        <div class="sub-menu-container">
            <div class="sub-item">資金調達 <span class="arrow">▼</span></div>
            <div class="sub-item">ビジネスサポート <span class="arrow">▼</span></div>
            <div class="sub-item">各種サービス <span class="arrow">▼</span></div>
        </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
        <div class="sub-menu-container">
            <div class="sub-item">《さいしん》<br>のご紹介 <span class="arrow">▼</span></div>
            <div class="sub-item">《さいしん》<br>のブランド戦略</div>
            <div class="sub-item">中期経営計画</div>
            <div class="sub-item">ディスクロージャー</div>
            <div class="sub-item">SDGs /<br>地域密着 <span class="arrow">▼</span></div>
            <div class="sub-item">施設貸出のご案内</div>
        </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown("""
        <div class="sub-menu-container">
            <div class="sub-item">新卒採用</div>
            <div class="sub-item">パートタイマー採用</div>
            <div class="sub-item">キャリア採用</div>
            <div class="sub-item">キャリアリターン採用 <span class="arrow">▼</span></div>
            <div class="sub-item">一般事業主行動計画</div>
        </div>
    """, unsafe_allow_html=True)


# 6. アプリ誘導ボタン
st.markdown('<a href="https://www.saishin.co.jp/kojin/" target="_blank" class="sticky-btn">アプリで口座開設</a>', unsafe_allow_html=True)