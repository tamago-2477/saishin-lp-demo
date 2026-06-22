import streamlit as st

# 1. ページ設定（※必ずコードの一番最初に書きます）
st.set_page_config(page_title="さいしん・若者応援プロジェクト", layout="centered")

# 2. ロゴの表示（左上に配置）
# カラムを使って、左側だけにロゴを配置してそれっぽく見せます
col_logo, col_empty = st.columns([1, 2])
with col_logo:
    # 先ほどアップロードした画像ファイル名と合わせます
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
    <a href="https://www.saishin.co.jp/kojin/" target="_blank" class="sticky-btn">👉 スマホで口座開設（最短3分）</a>
""", unsafe_allow_html=True)

# 4. メインコンテンツ
st.write("---") # 区切り線
st.title("埼玉縣信用金庫 × Z世代")
st.write("### 銀行を、もっと自由に。もっと身近に。")

st.info("💡 **マーケティング班の提案:** 15時以降も集まれるコミュニティ施設から、このページへ誘導します。")

# イメージ画像（URLで直接読み込み）
st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=1000", caption="若者が主役の新しい銀行のカタチ")

st.success("✅ **楽天・みずほ銀行の強みを導入:** 迷わせない1カラム設計 ＆ どこでも申し込める追従ボタン")

st.write("---")
st.subheader("📱 口座開設はカンタン3ステップ")

# ステップ表示
col1, col2, col3 = st.columns(3)
col1.metric("Step 1", "本人確認")
col2.metric("Step 2", "情報入力")
col3.metric("Step 3", "完了！")

# 追従ボタンのスクロール確認用の余白
for _ in range(10):
    st.write("")
st.write("※下にスクロールしても、緑色のボタンが追従します。")