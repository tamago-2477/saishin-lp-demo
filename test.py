import streamlit as st

st.set_page_config(layout="centered")

# --- ページ切り替え ---
try:
    current_page = st.query_params.get("page", "home")
except:
    current_page = st.experimental_get_query_params().get("page", ["home"])[0]

# --- 1. ロゴと口座開設ボタン（どんなページでも常に表示） ---
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("### 埼玉縣信用金庫")
with col2:
    st.markdown('<a href="?page=account">口座開設</a>', unsafe_allow_html=True)

# --- 2. ページ別の表示 ---
if current_page == "account":
    # 口座開設ページ
    st.image("app_pr.png", use_container_width=True)
    st.markdown('<a href="?page=home">← ホームに戻る</a>', unsafe_allow_html=True)
else:
    # ホームページ（標準のタブ機能をそのまま使用）
    tab1, tab2, tab3, tab4 = st.tabs(["個人のお客さま", "法人のお客さま", "《さいしん》について", "採用のご案内"])
    
    with tab1:
        st.write("ためる・ふやす | かりる | そなえる | 便利に使う | 相談・手続き")
    with tab2:
        st.write("資金調達 | ビジネスサポート | 各種サービス")
    with tab3:
        st.write("紹介 | ブランド戦略 | 中期経営計画 | ディスクロージャー | SDGs | 施設貸出")
    with tab4:
        st.write("新卒採用 | パートタイマー採用 | キャリア採用 | 採用情報")