import streamlit as st

st.set_page_config(layout="centered")

# CSSは「背景色」と「ボタンの配置」だけに限定しました
st.markdown("""
    <style>
    .stApp { background-color: #f9fbf9; }
    .footer-btn { position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); width: 90%; z-index: 100; }
    </style>
""", unsafe_allow_html=True)

# ページ切り替え
try:
    current_page = st.query_params.get("page", "home")
except:
    current_page = st.experimental_get_query_params().get("page", ["home"])[0]

# --- ヘッダー（ロゴマーク再現） ---
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown("### <span style='background:linear-gradient(135deg, #e60012, #f39800); color:white; padding:5px 10px; border-radius:50%;'>S</span>", unsafe_allow_html=True)
with col2:
    st.markdown("### 埼玉縣信用金庫")

# --- コンテンツ部分 ---
if current_page == "account":
    st.image("app_pr.png", use_container_width=True)
    st.markdown('<a href="?page=home">← ホームに戻る</a>', unsafe_allow_html=True)
else:
    tab1, tab2, tab3, tab4 = st.tabs(["個人のお客さま", "法人のお客さま", "《さいしん》について", "採用のご案内"])
    with tab1:
        st.write("ためる・ふやす | かりる | そなえる | 便利に使う | 相談・手続き")
    # ... 他のタブ ...
    
    # --- ずっと下に表示するボタン ---
    st.markdown("""
        <div class="footer-btn">
            <a href="?page=account" target="_self" style="display:block; background:#e60012; color:white; text-align:center; padding:15px; border-radius:30px; text-decoration:none; font-weight:bold;">
                アプリで口座開設
            </a>
        </div>
    """, unsafe_allow_html=True)