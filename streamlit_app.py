import streamlit as st

uploaded_files = st.file_uploader(
    "Upload images", accept_multiple_files="directory", type=["jpg", "png", "jpeg"]
)
for uploaded_file in uploaded_files:
    st.image(uploaded_file)
st.subheader("操作")
col1, col2, col3 = st.columns(3)

with col1:
    st.button("儲存")

with col2:
    st.button("查看打卡紀錄")

with col3:
    st.button("生成/下載 NFT")
    st.title("Web3打卡Demo")

# 說明
st.write("請上傳圖片，並按下儲存，系統會自動打卡（需登入 Metamask）。")

# 檔案上傳
uploaded_files = st.file_uploader(
    "Upload images", accept_multiple_files="directory", type=["jpg", "png", "jpeg"]
)
for uploaded_file in uploaded_files:
    st.image(uploaded_file)
    
# 按鈕
st.subheader("操作")
col1, col2, col3 = st.columns(3)

with col1:
    st.button("儲存")

with col2:
    st.button("查看打卡紀錄")

with col3:
    st.button("生成/下載 NFT")
