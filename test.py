import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="さいしん・若者応援プロジェクト", layout="centered")

# 2. CSS定義
st.markdown("""
    <style>
    .main { background-color: #f9fbf9; }
    .block-container { padding-top: 2rem; max-width: 800px; }
    
    /* --- ヘッダー・メニュー部分（固定表示） --- */
    .header-container { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
    .fake-logo { font-family: sans-serif; font-size: 26px; font-weight: bold; color: #4a4a4a; display: flex; align-items: center; gap: 10px; text-decoration: none; transition: 0.2s; }
    .fake-logo:hover { opacity: 0.7; }
    .logo-mark { background: linear-gradient(135deg, #e60012 50%, #f39800 50%); color: white; border-radius: 50%; width: 36px; height: 36px; display: flex; justify-content: center; align-items: center; font-size: 22px; font-style: italic; }
    .utility-menu { display: flex; align-items: center; gap: 15px; font-size: 12px; }
    .utility-link { color: #333; text-decoration: none; }
    .utility-btn-red { background-color: #e60012; color: white !important; padding: 8px 16px; border-radius: 4px; text-decoration: none; font-weight: bold; }

    .stTabs [data-baseweb="tab-list"] { gap: 0; background-color: #e60012; border-radius: 5px 5px 0 0; }
    .stTabs [data-baseweb="tab"] { height: 45px; background-color: #e60012; color: white; border-radius: 0; border-left: 1px solid #ff4d4d; flex: 1; }
    .stTabs [aria-selected="true"] { background-color: white !important; color: #333 !important; border-top: 4px solid #e60012; }
    
    .sub-menu-container { display: flex; background-color: white; border: 1px solid #ddd; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-top: -15px; margin-bottom: 20px; }
    .sub-item { flex: 1; text-align: center; padding: 12px 5px; font-size: 12px; font-weight: bold; color: #333; border-right: 1px solid #f0e1e1; }
    .sub-item:last-child { border-right: none; }
    
    .sticky-btn { position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); background-color: #e60012; color: white !important; padding: 15px 30px; border-radius: 50px; font-weight: bold; text-decoration: none; z-index: 999; box-shadow: 0 4px 12px rgba(0,0,0,0.2); width: 90%; max-width: 760px; text-align: center; font-size: 18px; }
    </style>
""", unsafe_allow_html=True)

# 3. ページの状態管理
if 'active_tab' not in st.session_state: st.session_state.active_tab = "個人のお客さま"
try:
    current_page = st.query_params.get("page", "home")
except:
    current_page = st.experimental_get_query_params().get("page", ["home"])[0]

# --- 共通ヘッダー（常に表示） ---
st.markdown(f'''
    <div class="header-container">
        <a href="?page=home" target="_self" class="fake-logo"><div class="logo-mark">S</div>埼玉縣信用金庫</a>
        <div class="utility-menu">
            <a href="#" class="utility-link">お問合せ・ご意見</a>
            <a href="#" class="utility-link">よくあるご質問</a>
            <a href="?page=account" target="_self" class="utility-btn-red">口座開設</a>
        </div>
    </div>
''', unsafe_allow_html=True)

# --- ページコンテンツの振り分け ---
if current_page == "account":
    st.image("app_pr.png", use_container_width=True)
    st.write("---")
    st.markdown('<a href="?page=home" target="_self">← ホームに戻る</a>', unsafe_allow_html=True)
else:
    # 共通メニュー（ホーム画面時のみ表示）
    tab1, tab2, tab3, tab4 = st.tabs(["個人のお客さま", "法人（個人事業主）のお客さま", "《さいしん》について", "採用のご案内"])
    
    # ※各タブの中身（サブメニュー）の表示処理は以前と同じなので省略
    # ... (前回のコードの "tab1〜tab4" の中身をここに入れてください) ...

    # 追従ボタン
    st.markdown('<a href="?page=account" target="_self" class="sticky-btn">アプリで口座開設</a>', unsafe_allow_html=True)