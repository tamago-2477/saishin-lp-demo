import streamlit as st

st.set_page_config(page_title="さいしん・若者応援プロジェクト", layout="centered")

# CSS修正：高さを固定して見切れを防ぐ
st.markdown("""
    <style>
    .main { background-color: #f9fbf9; }
    .block-container { padding-top: 1rem !important; max-width: 800px; }
    
    /* サイト全体の上部固定エリア（ロゴ＋メニュー） */
    .top-section { height: 160px; } 
    
    .header-container { display: flex; justify-content: space-between; align-items: center; padding-bottom: 10px; }
    .fake-logo { font-family: sans-serif; font-size: 26px; font-weight: bold; color: #4a4a4a !important; display: flex; align-items: center; gap: 10px; text-decoration: none; }
    .logo-mark { background: linear-gradient(135deg, #e60012 50%, #f39800 50%); color: white; border-radius: 50%; width: 36px; height: 36px; display: flex; justify-content: center; align-items: center; font-size: 22px; font-style: italic; }
    
    .utility-menu { display: flex; align-items: center; gap: 15px; font-size: 12px; }
    .utility-btn-red { background-color: #e60012; color: white !important; padding: 8px 16px; border-radius: 4px; text-decoration: none; font-weight: bold; }

    /* メニュータブのデザイン */
    .stTabs [data-baseweb="tab-list"] { background-color: #e60012; border-radius: 5px 5px 0 0; }
    .stTabs [data-baseweb="tab"] { height: 45px; color: white; border-left: 1px solid #ff4d4d; flex: 1; }
    .stTabs [aria-selected="true"] { background-color: white !important; color: #333 !important; border-top: 4px solid #e60012; }
    
    .sub-menu-container { display: flex; background-color: white; border: 1px solid #ddd; margin-top: -15px; }
    .sub-item { flex: 1; text-align: center; padding: 10px 2px; font-size: 11px; font-weight: bold; color: #333; border-right: 1px solid #f0e1e1; }
    .arrow { color: #f39800; font-size: 9px; }
    </style>
""", unsafe_allow_html=True)

# ページ切り替え管理
try:
    current_page = st.query_params.get("page", "home")
except:
    current_page = st.experimental_get_query_params().get("page", ["home"])[0]

# --- 常に表示するヘッダーエリア ---
st.markdown('''
    <div class="top-section">
        <div class="header-container">
            <a href="?page=home" target="_self" class="fake-logo"><div class="logo-mark">S</div>埼玉縣信用金庫</a>
            <div class="utility-menu">
                <span>お問合せ・ご意見</span> <span>よくあるご質問</span>
                <a href="?page=account" target="_self" class="utility-btn-red">口座開設</a>
            </div>
        </div>
''', unsafe_allow_html=True)

if current_page == "account":
    st.markdown('</div>', unsafe_allow_html=True) # top-sectionを閉じる
    st.image("app_pr.png", use_container_width=True)
    st.markdown('<a href="?page=home" target="_self">← ホームへ戻る</a>', unsafe_allow_html=True)
else:
    # メニューをtop-sectionの中に配置
    tab1, tab2, tab3, tab4 = st.tabs(["個人のお客さま", "法人（個人事業主）のお客さま", "《さいしん》について", "採用のご案内"])
    st.markdown('</div>', unsafe_allow_html=True) # top-sectionを閉じる

    with tab1:
        st.markdown('<div class="sub-menu-container"><div class="sub-item">ためる・ふやす<span class="arrow">▼</span></div><div class="sub-item">かりる<span class="arrow">▼</span></div><div class="sub-item">そなえる<span class="arrow">▼</span></div><div class="sub-item">便利に使う<span class="arrow">▼</span></div><div class="sub-item">相談・手続きする<span class="arrow">▼</span></div></div>', unsafe_allow_html=True)
    with tab2:
        st.markdown('<div class="sub-menu-container"><div class="sub-item">資金調達<span class="arrow">▼</span></div><div class="sub-item">ビジネスサポート<span class="arrow">▼</span></div><div class="sub-item">各種サービス<span class="arrow">▼</span></div></div>', unsafe_allow_html=True)
    # ... (他タブも同様) ...