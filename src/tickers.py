from dataclasses import dataclass
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
    data_history: pd.Series,
    image_url: str,
    ticker: str,
    start_date: str,
    end_date: str,
):
    st.write(f"{name.upper()} ($)")
    image = Image.open(urlopen(image_url))
    #    Display image
    st.image(image)
    #    Display dataframe
    st.table(ticker)
    #    Display a chart
    st.bar_chart(data_history.Close)
