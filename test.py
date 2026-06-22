import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="さいしん・若者応援プロジェクト", layout="centered")

# 2. ヘッダー部分（ロゴとメニュー）
col_logo, col_empty = st.columns([1, 1.5]) # ロゴが少し大きめに見えるように比率を微調整
with col_logo:
    st.image("logo.png", use_container_width=True)

st.image("menu.png", use_container_width=True)

# 3. デザインの調整（CSS）
st.markdown("""
    <style>
    /* 全体の背景色と、上の余白を少し詰める */
    .main { background-color: #f9fbf9; }
    .block-container { padding-top: 2rem; max-width: 760px; }

    /* 追従ボタンのデザイン */
    .sticky-btn {
        position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%);
        background-color: #00A968; color: white !important; padding: 15px 30px;
        border-radius: 50px; font-weight: bold; text-decoration: none;
        z-index: 999; box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        
        /* ここを修正：画像が入っている枠の幅（最大760px）にピッタリ合わせる */
        width: 90%; max-width: 760px; 
        
        text-align: center;
        font-size: 18px;
    }
    .sticky-btn:hover { background-color: #008f58; }
    </style>
    <a href="https://www.saishin.co.jp/kojin/" target="_blank" class="sticky-btn">👉 スマホで口座開設（最短3分）</a>
""", unsafe_allow_html=True)