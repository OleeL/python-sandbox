import requests
import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Output, Input
import plotly.graph_objs as go

def fetch_binance_ohlcv(symbol="BTCUSDT", interval="1m", limit=100):
    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        data = resp.json()
        columns = [
            "Timestamp", "Open", "High", "Low", "Close", "Volume", "CloseTime",
            "QuoteAssetVolume", "NumberOfTrades", "TakerBuyBase", "TakerBuyQuote", "Ignore"
        ]
        df = pd.DataFrame(data, columns=columns)
        df["Date"] = pd.to_datetime(df["Timestamp"], unit="ms")
        for col in ["Open", "High", "Low", "Close", "Volume"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        return df
    else:
        return None

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Live BTC/USDT Binance Candlestick (1min)"),
    dcc.Graph(id="live-candles"),
    dcc.Interval(id="interval", interval=60*1000, n_intervals=0)
])

@app.callback(
    Output("live-candles", "figure"),
    [Input("interval", "n_intervals")]
)
def update_chart(n):
    df = fetch_binance_ohlcv()
    if df is not None and not df.empty:
        fig = go.Figure(data=[go.Candlestick(
            x=df["Date"], open=df["Open"], high=df["High"],
            low=df["Low"], close=df["Close"],
            increasing_line_color='green', decreasing_line_color='red'
        )])
        fig.update_layout(
            xaxis_rangeslider_visible=False,
            yaxis_title="Price (USDT)",
            xaxis_title="Date"
        )
        return fig
    return {}

if __name__ == "__main__":
    app.run(debug=True)
