import yfinance as yf
import streamlit as st
from PIL import Image
import urllib3
import datetime

st.title("Cryptocurrency Daily Prices")
st.header("Main Dashboard")
# st.subheader("")

Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Ripple = 'XRP-USD'
BitcoinCash = 'BCH-USD'

BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)

BTCHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")
BCHHis = BCH_Data.history(period="max")

starts = datetime.datetime(2020,2,1)
ends = datetime.datetime(2020,2,1)
BTC = yf.download(Bitcoin, start="2022-10-18", end="2022-10-19")
ETH = yf.download(Ethereum, start="2022-10-18", end="2022-10-19")
XRP = yf.download(Ripple, start="2022-10-18", end="2022-10-19")
BCH = yf.download(BitcoinCash, start="2022-10-18", end="2022-10-19")

st.write("Bitcoin ($)")
st.image("https://s2.coinmarketcap.com/static/img/coins/64x64/1.png")
st.table(BTC)
st.bar_chart(BTCHis.Close)

st.write("Ethereum ($)")
st.image("https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png")
st.table(ETH)
st.bar_chart(ETHHis.Close)

st.write("Ripple ($)")
st.image("https://s2.coinmarketcap.com/static/img/coins/64x64/52.png")
st.table(XRP)
st.bar_chart(XRPHis.Close)

st.write("Bitcoin Cash ($)")
st.image("https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png")
st.table(BCH)
st.bar_chart(BCHHis.Close)