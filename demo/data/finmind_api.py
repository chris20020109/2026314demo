import requests
import pandas as pd

API_TOKEN = "你的FinMindToken"

def get_stock_price(stock_id, start="2024-01-01"):

    url = "https://api.finmindtrade.com/api/v4/data"

    params = {
        "dataset": "TaiwanStockPrice",
        "data_id": stock_id,
        "start_date": start,
        "token": API_TOKEN
    }

    res = requests.get(url, params=params)
    data = res.json()["data"]

    df = pd.DataFrame(data)

    return df
def get_eps(stock_id):

    url = "https://api.finmindtrade.com/api/v4/data"

    params = {
        "dataset": "TaiwanStockFinancialStatements",
        "data_id": stock_id,
        "token": API_TOKEN
    }

    res = requests.get(url, params=params)
    data = res.json()["data"]

    df = pd.DataFrame(data)

    eps = df[df["type"] == "EPS"]

    return eps
