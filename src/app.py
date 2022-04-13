import streamlit as st
import yfinance as yf

from config import settings
from tickers import display_chart

APP_NAME = "First crypto streamlit app"
st.set_page_config(
    page_title=APP_NAME,
    layout="wide",
    initial_sidebar_state="expanded",
)
# Titles and subtitles
st.title("Cryptocurrency Daily Prices | ₿")
st.header("Main Dashboard")

# To-Do: Migrate Ticker list to config
names = ["Bitcoin", "Ethereum", "Ripple", "Doge"]
ticker_list = ["BTC-USD", "ETH-USD", "XRP-USD", "DOGE-USD"]
ticker_image_URLS = {
    "BTC": "https://s2.coinmarketcap.com/static/img/coins/64x64/1.png",
    "ETH": "https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png",
    "XRP": "https://s2.coinmarketcap.com/static/img/coins/64x64/52.png",
    "DOGE": "https://s2.coinmarketcap.com/static/img/coins/64x64/74.png",
}
# Defining ticker variables
Data = {
    name: yf.Ticker(ticker)
    for name, ticker in zip(ticker_image_URLS.keys(), ticker_list)
}
# Access data from Yahoo Finance
histories = {
    name: Data[name].history(period="max") for name in ticker_image_URLS.keys()
}
# Fetch history data from Yahoo Finance
start = end = "2021-11-19"
downloads = {
    name: yf.download(ticker, start=start, end=end)
    for name, ticker in zip(ticker_image_URLS.keys(), ticker_list)
}

for name, crypto in zip(settings.names, ticker_image_URLS.keys()):
    display_chart(
        name,
        histories[crypto],
        ticker_image_URLS[crypto],
        downloads[crypto],
        start,
        end,
    )
