import streamlit as st

# 1. ページ設定（これを最初に書く）
st.set_page_config(page_title="さいしん・若者応援プロジェクト", layout="centered")

# 2. デザインの調整（CSS）
st.markdown("""
    <style>
    .main { background-color: #f9fbf9; }
    .stButton>button { background-color: #00A968; color: white; border-radius: 25px; height: 3em; width: 100%; font-weight: bold; }
    .sticky-btn {
        position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%);
        background-color: #00A968; color: white !important; padding: 15px 30px;
        border-radius: 50px; font-weight: bold; text-decoration: none;
        z-index: 999; box-shadow: 0 4px 12px rgba(0,0,0,0.15); width: 80%; text-align: center;
    }
    </style>
    <a href="#" class="sticky-btn">今すぐスマホで口座開設</a>
""", unsafe_allow_html=True)

# 3. コンテンツ
st.title("埼玉縣信用金庫 × Z世代")
st.write("### 銀行を、もっと自由に。もっと身近に。")

st.info("💡 **マーケティング班の提案:** 15時以降も集まれるコミュニティ施設から、このページへ誘導します。")

st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=1000", caption="若者が主役の新しい銀行のカタチ")

st.success("✅ **楽天・みずほ銀行の強みを導入:** 迷わせない1カラム設計 ＆ どこでも申し込める追従ボタン")

# ステップ表示
col1, col2, col3 = st.columns(3)
col1.metric("Step 1", "本人確認")
col2.metric("Step 2", "情報入力")
col3.metric("Step 3", "完了！")