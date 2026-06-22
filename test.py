import streamlit as st

st.set_page_config(page_title="さいしん・若者応援プロジェクト", layout="centered")

# CSSは必要最小限に絞りました
st.markdown("""
    <style>
    .block-container { padding-top: 1rem !important; }
    .header-box { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
    .logo { font-size: 24px; font-weight: bold; color: #333; display: flex; align-items: center; gap: 10px; }
    .stTabs [data-baseweb="tab-list"] { background-color: #e60012; }
    .stTabs [data-baseweb="tab"] { color: white; flex: 1; }
    .stTabs [aria-selected="true"] { background-color: white !important; color: #333 !important; }
    .sub-menu { display: flex; background: white; border: 1px solid #ddd; }
    .sub-item { flex: 1; text-align: center; padding: 10px; font-size: 12px; border-right: 1px solid #eee; }
    </style>
""", unsafe_allow_html=True)

# ページ切り替え
try:
    current_page = st.query_params.get("page", "home")
except:
    current_page = st.experimental_get_query_params().get("page", ["home"])[0]

# --- 全ページ共通ヘッダー ---
st.markdown('''
    <div class="header-box">
        <div class="logo">埼玉縣信用金庫</div>
        <div><a href="?page=account">口座開設</a></div>
    </div>
''', unsafe_allow_html=True)

if current_page == "account":
    st.image("app_pr.png", use_container_width=True)
    st.markdown('<a href="?page=home">← ホームへ戻る</a>', unsafe_allow_html=True)
else:
    # メニューをヘッダーの下に明確に配置
    tab1, tab2, tab3, tab4 = st.tabs(["個人のお客さま", "法人のお客さま", "《さいしん》について", "採用のご案内"])
    
    with tab1:
        st.markdown('<div class="sub-menu"><div class="sub-item">ためる・ふやす</div><div class="sub-item">かりる</div><div class="sub-item">そなえる</div><div class="sub-item">便利に使う</div><div class="sub-item">相談・手続き</div></div>', unsafe_allow_html=True)
    with tab2:
        st.markdown('<div class="sub-menu"><div class="sub-item">資金調達</div><div class="sub-item">ビジネスサポート</div><div class="sub-item">各種サービス</div></div>', unsafe_allow_html=True)
    # ... 他タブも同様に記載