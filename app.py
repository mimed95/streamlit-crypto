import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen


APP_NAME="First crypto streamlit app"
st.set_page_config(
    page_title=APP_NAME,
    layout="wide",
    initial_sidebar_state="expanded",
)
# Titles and subtitles
st.title("Cryptocurrency Daily Prices | ₿")
st.header("Main Dashboard")


# To-Do: Migrate Ticker list to config
ticker_list = [
    'BTC-USD',
    'ETH-USD',
    'XRP-USD',
    "DOGE-USD"
]
ticker_image_URLS = {
    "BTC": 'https://s2.coinmarketcap.com/static/img/coins/64x64/1.png',
    "ETH": 'https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png',
    "XRP": 'https://s2.coinmarketcap.com/static/img/coins/64x64/52.png',
    "DOGE": 'https://s2.coinmarketcap.com/static/img/coins/64x64/74.png'
}
# Defining ticker variables
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Ripple = 'XRP-USD'
Doge = 'DOGE-USD'

# Access data from Yahoo Finance
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
Doge_Data = yf.Ticker(Doge)


#Fetch history data from Yahoo Finance
BTCHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")
DogeHis = Doge_Data.history(period="max")

# Fetch crypto data for the dataframe
BTC = yf.download(Bitcoin, start="2021-11-19", end="2021-11-19")
ETH = yf.download(Ethereum, start="2021-11-19", end="2021-11-19")
XRP = yf.download(Ripple, start="2021-11-19", end="2021-11-19")
DOGE = yf.download(Doge, start="2021-11-19", end="2021-11-19")

#Bitcoin
st.write("BITCOIN ($)")
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
#Display image
st.image(imageBTC)
#Display dataframe
st.table(BTC)
#Display a chart
st.bar_chart(BTCHis.Close)

#Ethereum
st.write("ETHERUM ($)")
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
#Display image
st.image(imageETH)
#Display dataframe
st.table(ETH)
#Display a chart
st.bar_chart(ETHHis.Close)

#Ripple
st.write("RIPPLE ($)")
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
#Display image
st.image(imageXRP)
#Display dataframe
st.table(XRP)
#Display a chart
st.bar_chart(XRPHis.Close)

#Bitcoin Cash
st.write("Doge ($)")
imageDoge = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/74.png'))
#Display image
st.image(imageDoge)
#Display dataframe
st.table(DOGE)
#Display a chart
st.bar_chart(DogeHis.Close)
