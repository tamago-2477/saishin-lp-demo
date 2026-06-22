import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="さいしん・若者応援プロジェクト", layout="centered")

# ==========================================
# ★新機能：ページのルーティング（振り分け）★
# URLの末尾を見て、どのページを表示するか決定します
# ==========================================
current_page = st.query_params.get("page", "home")

if current_page == "account":
    # ==========================================
    # ページ2：【口座開設ページ】のレイアウト
    # ==========================================
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.title("📱 アプリで口座開設")
    st.write("ここが「新しいページ」です！同じ test.py の中にレイアウトを書いています。")
    
    st.info("💡 実際の画面では、ここにスマホのカメラ起動ボタンや、入力フォームを配置します。")
    
    # フォームのダミー（デザインだけ）
    st.text_input("お名前 (フルネーム)")
    st.text_input("メールアドレス")
    st.button("次へ進む", type="primary")
    
    st.write("---")
    # ホームに戻るためのリンク（URLのパラメータを home にする）
    st.markdown('<a href="?page=home" target="_self" style="color: #e60012; font-weight: bold; text-decoration: none;">← トップページに戻る</a>', unsafe_allow_html=True)

else:
    # ==========================================
    # ページ1：【ホーム画面】のレイアウト（今まで作っていたもの）
    # ==========================================
    
    # タブの選択状態を管理
    if 'active_tab' not in st.session_state:
        st.session_state.active_tab = "個人のお客さま"

    # カスタムCSS
    st.markdown("""
        <style>
        .main { background-color: #f9fbf9; }
        .block-container { padding-top: 3rem; max-width: 800px; }

        .header-container { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .fake-logo { font-family: sans-serif; font-size: 26px; font-weight: bold; color: #4a4a4a; display: flex; align-items: center; gap: 10px; text-decoration: none; transition: 0.2s; }
        .fake-logo:hover { opacity: 0.7; }
        .logo-mark { background: linear-gradient(135deg, #e60012 50%, #f39800 50%); color: white; border-radius: 50%; width: 36px; height: 36px; display: flex; justify-content: center; align-items: center; font-size: 22px; font-style: italic; }
        
        .utility-menu { display: flex; align-items: center; gap: 15px; font-size: 12px; }
        .utility-link { color: #333; text-decoration: none; }
        .utility-link:hover { text-decoration: underline; }
        .utility-btn-red { background-color: #e60012; color: white !important; padding: 8px 16px; border-radius: 4px; text-decoration: none; font-weight: bold; transition: 0.2s; }
        .utility-btn-red:hover { background-color: #c1000f; }

        .custom-tab-bar { display: flex; background-color: #e60012; border-radius: 8px 8px 0 0; padding: 4px 4px 0 4px; }
        .custom-tab-bar .stButton { flex: 1; margin: 0; }
        .custom-tab-bar .stButton > button { width: 100%; height: 45px; border: none !important; border-radius: 6px 6px 0 0 !important; font-weight: bold; transition: 0s; padding: 0; }
        .custom-tab-bar .stButton > button:hover, .custom-tab-bar .stButton > button:focus, .custom-tab-bar .stButton > button:active { box-shadow: none !important; }

        .sub-menu-container { display: flex; background-color: white; border-bottom: 1px solid #ddd; border-left: 1px solid #ddd; border-right: 1px solid #ddd; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 20px; }
        .sub-item { flex: 1; text-align: center; padding: 12px 5px; font-size: 12px; font-weight: bold; color: #333; border-right: 1px solid #f0e1e1; }
        .sub-item:last-child { border-right: none; }
        .arrow { color: #f39800; font-size: 10px; margin-left: 5px; }

        .sticky-btn { position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); background-color: #e60012; color: white !important; padding: 15px 30px; border-radius: 50px; font-weight: bold; text-decoration: none; z-index: 999; box-shadow: 0 4px 12px rgba(0,0,0,0.2); width: 90%; max-width: 760px; text-align: center; font-size: 18px; transition: 0.3s; }
        .sticky-btn:hover { background-color: #c1000f; }
        </style>
    """, unsafe_allow_html=True)

    # ヘッダー描画
    st.markdown("""
        <div class="header-container">
            <a href="?page=home" target="_self" class="fake-logo">
                <div class="logo-mark">S</div>埼玉縣信用金庫
            </a>
            <div class="utility-menu">
                <a href="#" class="utility-link">お問合せ・ご意見</a>
                <a href="#" class="utility-link">よくあるご質問</a>
                <a href="?page=account" target="_self" class="utility-btn-red">口座開設</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # タブの描画
    tabs = ["個人のお客さま", "法人（個人事業主）のお客さま", "《さいしん》について", "採用のご案内"]
    css_styles = "<style>"
    for i, tab_name in enumerate(tabs):
        if st.session_state.active_tab == tab_name:
            css_styles += f".custom-tab-bar .stButton:nth-child({i+1}) > button {{ background-color: white !important; color: #333 !important; border-top: 3px solid #e60012 !important; border-bottom: none !important; }}"
        else:
            border_left = "border-left: 1px solid #ff4d4d !important;" if i > 0 else ""
            css_styles += f".custom-tab-bar .stButton:nth-child({i+1}) > button {{ background-color: transparent !important; color: white !important; {border_left} }}"
    css_styles += "</style>"
    st.markdown(css_styles, unsafe_allow_html=True)

    st.markdown('<div class="custom-tab-bar">', unsafe_allow_html=True)
    cols = st.columns(4)
    for i, tab_name in enumerate(tabs):
        with cols[i]:
            if st.button(tab_name, use_container_width=True, key=f"tab_btn_{i}"):
                st.session_state.active_tab = tab_name
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # サブメニューの表示
    if st.session_state.active_tab == "個人のお客さま":
        st.markdown('<div class="sub-menu-container"><div class="sub-item">ためる・ふやす <span class="arrow">▼</span></div><div class="sub-item">かりる <span class="arrow">▼</span></div><div class="sub-item">そなえる <span class="arrow">▼</span></div><div class="sub-item">便利に使う <span class="arrow">▼</span></div><div class="sub-item">相談・手続きする <span class="arrow">▼</span></div></div>', unsafe_allow_html=True)
    elif st.session_state.active_tab == "法人（個人事業主）のお客さま":
        st.markdown('<div class="sub-menu-container"><div class="sub-item">資金調達 <span class="arrow">▼</span></div><div class="sub-item">ビジネスサポート <span class="arrow">▼</span></div><div class="sub-item">各種サービス <span class="arrow">▼</span></div></div>', unsafe_allow_html=True)
    elif st.session_state.active_tab == "《さいしん》について":
        st.markdown