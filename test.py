import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="さいしん・若者応援プロジェクト", layout="centered")

# 2. 画像を使わず、すべてHTMLとCSSで描画する
st.markdown("""
    <style>
    /* 全体の背景色と上の余白 */
    .main { background-color: #f9fbf9; }
    .block-container { padding-top: 4.5rem; max-width: 800px; }

    /* --- 0. ヘッダー全体（ロゴと右側のメニューを横並びにする枠） --- */
    .header-container {
        display: flex;
        justify-content: space-between; /* 左右に離して配置 */
        align-items: center; /* 縦の真ん中で揃える */
        margin-bottom: 15px;
        flex-wrap: wrap; /* 画面が狭い時に重ならないよう折り返す設定 */
        gap: 15px;
    }

    /* --- 1. ロゴ部分のデザイン --- */
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

    /* --- 1.5. 右上のユーティリティメニュー --- */
    .utility-menu {
        display: flex;
        align-items: center;
        gap: 15px;
        font-size: 12px;
    }
    .utility-link {
        color: #333;
        text-decoration: none;
    }
    .utility-link:hover {
        text-decoration: underline;
    }
    .utility-btn-red {
        background-color: #e60012;
        color: white !important;
        padding: 8px 16px;
        border-radius: 4px;
        text-decoration: none;
        font-weight: bold;
        transition: 0.2s;
    }
    .utility-btn-red:hover {
        background-color: #c1000f;
    }

    /* --- 2. メニューバー（赤）のデザイン --- */
    .fake-menu-top {
        display: flex;
        background-color: #e60012;
        color: white;
        font-size: 12px;
        font-weight: bold;
        text-align: center;
        border-radius: 5px 5px 0 0;
        overflow: hidden;
    }
    .fake-menu-tab-active, .fake-menu-tab {
        flex: 1; 
        display: flex;
        align-items: center; 
        justify-content: center; 
        padding: 12px 5px; 
    }
    .fake-menu-tab-active {
        background-color: white;
        color: #333;
        border-top: 4px solid #e60012;
    }
    .fake-menu-tab {
        border-left: 1px solid #ff4d4d;
    }

    /* --- 3. サブメニュー（白）のデザイン --- */
    .fake-menu-bottom {
        display: flex;
        background-color: white;
        color: #333;
        font-size: 11px;
        font-weight: bold;
        text-align: center;
        border-bottom: 1px solid #ddd;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .fake-menu-sub {
        flex: 1; 
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 10px 2px;
        border-right: 1px solid #f0e1e1;
    }
    .fake-menu-sub:last-child {
        border-right: none; 
    }
    .arrow { color: #f39800; font-size: 9px; margin-left: 3px; }

    /* --- 4. 追従ボタン（赤）のデザイン --- */
    .sticky-btn {
        position: fixed; 
        bottom: 20px; 
        left: 50%; 
        transform: translateX(-50%);
        background-color: #e60012; 
        color: white !important; 
        padding: 15px 30px;
        border-radius: 50px; 
        font-weight: bold; 
        text-decoration: none;
        z-index: 999; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        width: 90%; 
        max-width: 760px; 
        text-align: center;
        font-size: 18px;
        transition: 0.3s;
    }
    .sticky-btn:hover { background-color: #c1000f; }
    </style>

    <div class="header-container">
        <div class="fake-logo">
            <div class="logo-mark">S</div>
            埼玉縣信用金庫
        </div>
        <div class="utility-menu">
            <a href="#" class="utility-link">お問合せ・ご意見</a>
            <a href="#" class="utility-link">よくあるご質問</a>
            <a href="#" class="utility-btn-red">口座開設</a>
        </div>
    </div>

    <div class="fake-menu-top">
        <div class="fake-menu-tab-active">個人のお客さま</div>
        <div class="fake-menu-tab">法人（個人事業主）のお客さま</div>
        <div class="fake-menu-tab">《さいしん》について</div>
        <div class="fake-menu-tab">採用のご案内</div>
    </div>
    <div class="fake-menu-bottom">
        <div class="fake-menu-sub">ためる・ふやす <span class="arrow">▼</span></div>
        <div class="fake-menu-sub">かりる <span class="arrow">▼</span></div>
        <div class="fake-menu-sub">そなえる <span class="arrow">▼</span></div>
        <div class="fake-menu-sub">便利に使う <span class="arrow">▼</span></div>
        <div class="fake-menu-sub">相談・手続きする <span class="arrow">▼</span></div>
    </div>

    <a href="https://www.saishin.co.jp/kojin/" target="_blank" class="sticky-btn">スマホで口座開設</a>
""", unsafe_allow_html=True)