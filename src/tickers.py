from dataclasses import dataclass
from typing import Optional
from urllib.request import urlopen

import pandas as pd
import streamlit as st
from PIL import Image


@dataclass
class ticker:
    name: str
    image_url: str
    start: str
    end: str

    @property
    def data(self):
        raise NotImplementedError


def display_chart(
    name: str,
    data_history: pd.DataFrame,
    image_url: str,
    ticker: str,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
):
    if start_date is None:
        start_date = data_history.index[0]
    if end_date is None:
        end_date = data_history.index[-1]
    selected_data = data_history.Close.loc[start_date:end_date]
    st.write(f"{name.upper()} ($)")
    image = Image.open(urlopen(image_url))
    #    Display image
    st.image(image)
    #    Display dataframe
    st.table(ticker)
    #    Display a chart
    st.bar_chart(selected_data)


def candlestick_chart(data, symbol):
    # see https://neuralmarkettrends.com/python-tutorials/
    pass
