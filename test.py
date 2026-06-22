import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="さいしん・若者応援プロジェクト", layout="centered")

# 2. タブの選択状態を管理する（セッションステート）
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "個人のお客さま"

# 3. カスタムCSS
st.markdown("""
    <style>
    /* 全体の背景色と上の余白 */
    .main { background-color: #f9fbf9; }
    .block-container { padding-top: 3rem; max-width: 800px; }

    /* --- ロゴとユーティリティメニューの配置 --- */
    .header-container {
        display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;
    }
    .fake-logo {
        font-family: sans-serif; font-size: 26px; font-weight: bold; color: #4a4a4a; display: flex; align-items: center; gap: 10px;
    }
    .logo-mark {
        background: linear-gradient(135deg, #e60012 50%, #f39800 50%); color: white; border-radius: 50%; width: 36px; height: 36px; display: flex; justify-content: center; align-items: center; font-size: 22px; font-style: italic;
    }
    .utility-menu { display: flex; align-items: center; gap: 15px; font-size: 12px; }
    .utility-link { color: #333; text-decoration: none; }
    .utility-link:hover { text-decoration: underline; }
    .utility-btn-red {
        background-color: #e60012; color: white !important; padding: 8px 16px; border-radius: 4px; text-decoration: none; font-weight: bold;
    }

    /* --- 自作タブバー（ボタンの親要素） --- */
    .custom-tab-bar {
        display: flex;
        background-color: #e60012; /* 全体の背景を赤に */
        border-radius: 8px 8px 0 0; /* ★ここで全体の上の角を丸くする★ */
        padding: 4px 4px 0 4px; /* ★上と左右に赤い余白を作る★ */
    }
    
    /* Streamlitの標準ボタンを透明にして、枠の大きさに合わせる */
    .custom-tab-bar .stButton { flex: 1; margin: 0; }
    .custom-tab-bar .stButton > button {
        width: 100%;
        height: 45px;
        border: none !important;
        border-radius: 6px 6px 0 0 !important; /* ★白くなったタブの上の角を丸くする★ */
        font-weight: bold;
        transition: 0s;
        padding: 0;
    }
    /* Streamlitボタンのホバー時の色変化を消す */
    .custom-tab-bar .stButton > button:hover, 
    .custom-tab-bar .stButton > button:focus, 
    .custom-tab-bar .stButton > button:active {
        box-shadow: none !important;
    }

    /* --- サブメニュー（タブの中身）のデザイン --- */
    .sub-menu-container {
        display: flex;
        background-color: white;
        border-bottom: 1px solid #ddd;
        border-left: 1px solid #ddd;
        border-right: 1px solid #ddd;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .sub-item {
        flex: 1; text-align: center; padding: 12px 5px; font-size: 12px; font-weight: bold; color: #333; border-right: 1px solid #f0e1e1;
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

# 4. ヘッダー描画
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

# 5. タブの描画（ボタンを横並びにして色を動的に変える）
tabs = ["個人のお客さま", "法人（個人事業主）のお客さま", "《さいしん》について", "採用のご案内"]

# 動的にCSSを生成して、選択されたタブだけ白く、他を赤くする
css_styles = "<style>"
for i, tab_name in enumerate(tabs):
    if st.session_state.active_tab == tab_name:
        # アクティブなタブ（白背景、黒文字、上に赤い細線）
        css_styles += f".custom-tab-bar .stButton:nth-child({i+1}) > button {{ background-color: white !important; color: #333 !important; border-top: 3px solid #e60012 !important; border-bottom: none !important; }}"
    else:
        # 非アクティブなタブ（赤背景、白文字、左に薄い赤の区切り線）
        border_left = "border-left: 1px solid #ff4d4d !important;" if i > 0 else ""
        css_styles += f".custom-tab-bar .stButton:nth-child({i+1}) > button {{ background-color: transparent !important; color: white !important; {border_left} }}"
css_styles += "</style>"
st.markdown(css_styles, unsafe_allow_html=True)

# タブバーのコンテナ
st.markdown('<div class="custom-tab-bar">', unsafe_allow_html=True)
cols = st.columns(4)
for i, tab_name in enumerate(tabs):
    with cols[i]:
        # ボタンが押されたら、session_stateを更新して再描画
        if st.button(tab_name, use_container_width=True, key=f"tab_btn_{i}"):
            st.session_state.active_tab = tab_name
            st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# 6. 選択されたタブに応じたサブメニューの表示
if st.session_state.active_tab == "個人のお客さま":
    st.markdown("""
        <div class="sub-menu-container">
            <div class="sub-item">ためる・ふやす <span class="arrow">▼</span></div>
            <div class="sub-item">かりる <span class="arrow">▼</span></div>
            <div class="sub-item">そなえる <span class="arrow">▼</span></div>
            <div class="sub-item">便利に使う <span class="arrow">▼</span></div>
            <div class="sub-item">相談・手続きする <span class="arrow">▼</span></div>
        </div>
    """, unsafe_allow_html=True)
elif st.session_state.active_tab == "法人（個人事業主）のお客さま":
    st.markdown("""
        <div class="sub-menu-container">
            <div class="sub-item">資金調達 <span class="arrow">▼</span></div>
            <div class="sub-item">ビジネスサポート <span class="arrow">▼</span></div>
            <div class="sub-item">各種サービス <span class="arrow">▼</span></div>
        </div>
    """, unsafe_allow_html=True)
elif st.session_state.active_tab == "《さいしん》について":
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
elif st.session_state.active_tab == "採用のご案内":
    st.markdown("""
        <div class="sub-menu-container">
            <div class="sub-item">新卒採用</div>
            <div class="sub-item">パートタイマー採用</div>
            <div class="sub-item">キャリア採用</div>
            <div class="sub-item">キャリアリターン採用 <span class="arrow">▼</span></div>
            <div class="sub-item">一般事業主行動計画</div>
        </div>
    """, unsafe_allow_html=True)

# 7. アプリ誘導ボタン
st.markdown('<a href="https://www.saishin.co.jp/kojin/" target="_blank" class="sticky-btn">アプリで口座開設</a>', unsafe_allow_html=True)