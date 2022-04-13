# Crypto Ticker Dashboard in Streamlit

A streamlit dashboard for cryptocurrencies. This is a work in progress.
As of now it only fetches BTC, ETH, XRP and DOGE prices to display.

## To-Do:

 - [X] Configuration management for tickers with dynaconf
- dynamic display of tickers
    - [ ] adding/removing cryptos
    - [ ] change price to display to Open, Close, Min, Max
    - [ ] change period to display
    - [ ] add some basic Moving average indicators into the chart


## Quick Start
- Install the dependecies
``pip install -r requirements.txt``
- To display the ticker dashboard run
``streamlit run src/app.py`` and open http://localhost:8501/ in your browser
