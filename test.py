import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="さいしん・若者応援プロジェクト", layout="centered")

# ==========================================
# ★安全なページ切り替え★
# ==========================================
try:
    current_page = st.query_params.get("page", "home")
except AttributeError:
    current_page = st.experimental_get_query_params().get("page", ["home"])[0]

if current_page == "account":
    # ==========================================
    # ページ2：【口座開設ページ】
    # ==========================================
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ★ここが修正ポイント（.pngに変更）★
    st.image("app_pr.png", use_container_width=True)
    
    st.write("---")
    st.markdown('<a href="?page=home" target="_self" style="display: inline-block; padding: 10px 20px; background-color: #f0f0f0; color: #333; border-radius: 5px; font-weight: bold; text-decoration: none;">← ホーム画面に戻る</a>', unsafe_allow_html=True)

else:
    # ==========================================
    # ページ1：【ホーム画面】
    # ==========================================
    # (※CSSとヘッダー描画などのコードは以前と同じです)
    
    st.markdown("""
        <style>
        .main { background-color: #f9fbf9; }
        .block-container { padding-top: 3rem; max-width: 800px; }

        .header-container { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 15px; }
        .fake-logo { font-family: sans-serif; font-size: 26px; font-weight: bold; color: #4a4a4a; display: flex; align-items: center; gap: 10px; }
        .logo-mark { background: linear-gradient(135deg, #e60012 50%, #f39800 50%); color: white; border-radius: 50%; width: 36px; height: 36px; display: flex; justify-content: center; align-items: center; font-size: 22px; font-style: italic; }
        
        .utility-menu { display: flex; align-items: center; gap: 15px; font-size: 12px; }
        .utility-link { color: #333; text-decoration: none; }
        .utility-link:hover { text-decoration: underline; }
        .utility-btn-red { background-color: #e60012; color: white !important; padding: 8px 16px; border-radius: 4px; text-decoration: none; font-weight: bold; transition: 0.2s; }
        .utility-btn-red:hover { background-color: #c1000f; }

        .stTabs [data-baseweb="tab-list"] { gap: 0; background-color: #e60012; border-radius: 5px 5px 0 0; }
        .stTabs [data-baseweb="tab"] { height: 45px; white-space: pre-wrap; background-color: #e60012; color: white; border-radius: 0; border-left: 1px solid #ff4d4d; flex: 1; justify-content: center; }
        .stTabs [data-baseweb="tab"]:first-child { border-left: none; }
        .stTabs [aria-selected="true"] { background-color: white !important; color: #333 !important; border-top: 4px solid #e60012; }
        
        .sub-menu-container { display: flex; background-color: white; border-bottom: 1px solid #ddd; border-left: 1px solid #ddd; border-right: 1px solid #ddd; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-top: -15px; margin-bottom: 20px; }
        .sub-item { flex: 1; text-align: center; padding: 12px 5px; font-size: 12px; font-weight: bold; color: #333; border-right: 1px solid #f0e1e1; }
        .sub-item:last-child { border-right: none; }
        .arrow { color: #f39800; font-size: 10px; margin-left: 5px; }

        .sticky-btn { position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); background-color: #e60012; color: white !important; padding: 15px 30px; border-radius: 50px; font-weight: bold; text-decoration: none; z-index: 999; box-shadow: 0 4px 12px rgba(0,0,0,0.2); width: 90%; max-width: 760px; text-align: center; font-size: 18px; transition: 0.3s; }
        .sticky-btn:hover { background-color: #c1000f; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="header-container">
            <div class="fake-logo"><div class="logo-mark">S</div>埼玉縣信用金庫</div>
            <div class="utility-menu">
                <a href="#" class="utility-link">お問合せ・ご意見</a>
                <a href="#" class="utility-link">よくあるご質問</a>
                <a href="?page=account" target="_self" class="utility-btn-red">口座開設</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["個人のお客さま", "法人（個人事業主）のお客さま", "《さいしん》について", "採用のご案内"])

    with tab1:
        st.markdown('<div class="sub-menu-container"><div class="sub-item">ためる・ふやす <span class="arrow">▼</span></div><div class="sub-item">かりる <span class="arrow">▼</span></div><div class="sub-item">そなえる <span class="arrow">▼</span></div><div class="sub-item">便利に使う <span class="arrow">▼</span></div><div class="sub-item">相談・手続きする <span class="arrow">▼</span></div></div>', unsafe_allow_html=True)
    with tab2:
        st.markdown('<div class="sub-menu-container"><div class="sub-item">資金調達 <span class="arrow">▼</span></div><div class="sub-item">ビジネスサポート <span class="arrow">▼</span></div><div class="sub-item">各種サービス <span class="arrow">▼</span></div></div>', unsafe_allow_html=True)
    with tab3:
        st.markdown('<div class="sub-menu-container"><div class="sub-item">《さいしん》<br>のご紹介 <span class="arrow">▼</span></div><div class="sub-item">《さいしん》<br>のブランド戦略</div><div class="sub-item">中期経営計画</div><div class="sub-item">ディスクロージャー</div><div class="sub-item">SDGs /<br>地域密着 <span class="arrow">▼</span></div><div class="sub-item">施設貸出のご案内</div></div>', unsafe_allow_html=True)
    with tab4:
        st.markdown('<div class="sub-menu-container"><div class="sub-item">新卒採用</div><div class="sub-item">パートタイマー採用</div><div class="sub-item">キャリア採用</div><div class="sub-item">キャリアリターン採用 <span class="arrow">▼</span></div><div class="sub-item">一般事業主行動計画</div></div>', unsafe_allow_html=True)

    st.markdown('<a href="?page=account" target="_self" class="sticky-btn">アプリで口座開設</a>', unsafe_allow_html=True)