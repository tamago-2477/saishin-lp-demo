import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="さいしん・若者応援プロジェクト", layout="centered")

# 2. ヘッダー部分（ロゴとメニュー）
col_logo, col_empty = st.columns([1, 1.5]) 
with col_logo:
    # GitHubにアップロードしたロゴ画像のファイル名
    st.image("logo.png", use_container_width=True)

# GitHubにアップロードしたメニュー画像のファイル名
st.image("menu.png", use_container_width=True)

# 3. デザインの調整（CSS）
st.markdown("""
    <style>
    /* 全体の背景色と、上の余白を調整 */
    .main { background-color: #f9fbf9; }
    .block-container { padding-top: 4rem; max-width: 760px; }

    /* 追従ボタンのデザイン */
    .sticky-btn {
        position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%);
        
        /* --- 修正点：背景色を赤に、文字色を白に明示的に設定 --- */
        background-color: #e60012; /* 鮮やかな赤 */
        color: white !important; /* 文字色は白 */
        
        padding: 15px 30px;
        border-radius: 50px; /* 角丸 */
        font-weight: bold;
        text-decoration: none;
        z-index: 999;
        
        /* --- 修正点：影の設定を、白地に見える黒い影に変更 --- */
        box-shadow: 0 4px 12px rgba(0,0,0,0.15); /* 黒い影 */
        
        /* 画像枠に合わせた幅（維持） */
        width: 90%; max-width: 760px; 
        
        text-align: center;
        font-size: 18px;
    }
    
    /* --- 修正点：ホバー時の背景色も暗い赤に変更 --- */
    .sticky-btn:hover { background-color: #c1000f; } /* ホバー時は暗い赤 */
    
    </style>
    
    /* --- 修正点：文字を短くシンプルに「スマホで口座開設」に変更 --- */
    <a href="https://www.saishin.co.jp/kojin/" target="_blank" class="sticky-btn">スマホで口座開設</a>
""", unsafe_allow_html=True)