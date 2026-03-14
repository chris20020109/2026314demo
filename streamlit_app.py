import streamlit as st
from data import finmind_api

get_stock_price = finmind_api.get_stock_price
get_eps = finmind_api.get_eps

st.title("台股分析系統")

stock = st.text_input("股票代碼", "2330")

if st.button("抓資料"):

    price = get_stock_price(stock)

    st.write("最近股價")

    st.dataframe(price.tail())

    eps = get_eps(stock)

    st.write("EPS")

    st.dataframe(eps.tail())
