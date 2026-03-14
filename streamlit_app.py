import streamlit as st

st.title("股票分析系統")

stock = st.text_input("輸入股票代碼")

if stock:
    st.write("股票代碼:", stock)
