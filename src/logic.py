import yfinance as yf
import numpy
import src.utls as utls


def get_tickers_data():
    data = yf.download("AAPL, META", period="2d", interval="1h")
    return data
    print(data['Close', 'BTC-USD'])
    for ticker in tickers:
        data['Percentage', ticker] = data['Close', ticker].pct_change()*100
    print(data.tail(2))

def calculate_percentage(data):
    print(data.shape[1])
    for x in data['Close']:
        data['Percentage', x] = data['Close', x].pct_change()*100
    return data

def get_current_percentage(ticker_dict):
    ticker_list = utls.get_ticker_list(ticker_dict)
    s = get_tickers_data()
    print(calculate_percentage(s)['Percentage'])