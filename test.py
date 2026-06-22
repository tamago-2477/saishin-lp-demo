import streamlit as st

# 1. ページ設定（※必ずコードの一番最初に書きます）
st.set_page_config(page_title="さいしん・若者応援プロジェクト", layout="centered")

# 2. ロゴの表示（左上に配置）
# カラムを使って、左側だけにロゴを配置してそれっぽく見せます
col_logo, col_empty = st.columns([1, 2])
with col_logo:
    # GitHubにアップロードしたロゴ画像のファイル名と合わせます
    # ここでは "logo.png" となっています
    st.image("logo.png", use_container_width=True)

# 3. デザインの調整（CSS）
st.markdown("""
    <style>
    .main { background-color: #f9fbf9; }
    /* 追従ボタンのデザイン */
    .sticky-btn {
        position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%);
        background-color: #00A968; color: white !important; padding: 15px 30px;
        border-radius: 50px; font-weight: bold; text-decoration: none;
        z-index: 999; box-shadow: 0 4px 12px rgba(0,0,0,0.15); width: 80%; text-align: center;
        font-size: 18px;
    }
    .sticky-btn:hover { background-color: #008f58; }
    </style>
    # 追従ボタンのHTML
    <a href="https://www.saishin.co.jp/kojin/" target="_blank" class="sticky-btn">👉 スマホで口座開設（最短3分）</a>
""", unsafe_allow_html=True)