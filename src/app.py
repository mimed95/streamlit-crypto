from datetime import date, timedelta

import streamlit as st
import yfinance as yf

from configuration.config import settings
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


# Defining ticker variables
Data = {
    name: yf.Ticker(ticker)
    for name, ticker in zip(settings.ticker_image_URL.keys(), settings.ticker_list)
}
# Access data from Yahoo Finance
histories = {
    name: Data[name].history(period="max") for name in settings.ticker_image_URL.keys()
}
# Fetch history data from Yahoo Finance
start = end = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")

# make today default date
downloads = {
    name: yf.download(ticker, start=start, end=end)
    for name, ticker in zip(settings.ticker_image_URL.keys(), settings.ticker_list)
}

for name, crypto in zip(settings.cryptos, settings.ticker_image_URL.keys()):
    display_chart(
        name, histories[crypto], settings.ticker_image_URL[crypto], downloads[crypto]
    )
