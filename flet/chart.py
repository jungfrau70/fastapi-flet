import requests
import pandas as pd
import plotly.express as px
from flet.plotly_chart import PlotlyChart

# Function to fetch data from the backend
def fetch_data():
    ohlc_response = requests.get("http://127.0.0.1:8000/ohlc")
    ema20_response = requests.get("http://127.0.0.1:8000/ema?period=20")
    ema50_response = requests.get("http://127.0.0.1:8000/ema?period=50")
    ema100_response = requests.get("http://127.0.0.1:8000/ema?period=100")
    ema200_response = requests.get("http://127.0.0.1:8000/ema?period=200")

    ohlc_data = ohlc_response.json()["data"]
    ema20 = ema20_response.json()
    ema50 = ema50_response.json()
    ema100 = ema100_response.json()
    ema200 = ema200_response.json()

    return ohlc_data, ema20, ema50, ema100, ema200

# Function to create chart
def create_chart():
    ohlc_data, ema20, ema50, ema100, ema200 = fetch_data()
    df = pd.DataFrame(ohlc_data)
    fig = px.line(df, x="timestamp", y="close")
    return fig
