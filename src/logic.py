import yfinance as yf
import numpy
import pandas as pd
import time

import src.utls as utls



def get_tickers_data(tickers_list):
    data = yf.download(tickers_list, period="2d", interval="1h")
    print(data.tail(3))
    return data
    

def calculate_percentage(data):
    for x in data['Close']:
        data['Percentage', x] = data['Close', x].pct_change()*100
    return data

def get_current_percentage(ticker_dict):
    ticker_list = get_ticker_list(ticker_dict)
    s = get_tickers_data(ticker_list)
    s = calculate_percentage(s)
    candle_date = s.iloc[-2].name.strftime("%H:%M:%S %d.%m.%Y")
    print("Datetime: ",candle_date)

    if candle_date == ticker[0]['LastCheckTime']:
        print("1h Candle is not up yet, retrying in 60s...")
        time.sleep(60)
        return get_current_percentage(ticker_dict)
    
    for ticker in ticker_dict:
        percentage_to_dict = round(s['Percentage', ticker['Ticker']].iloc[-2], 2)
        ticker['LastChange'] = percentage_to_dict
        ticker['LastCheckTime'] = candle_date
    ticker_dict = utls.sort_dict_list_desc(ticker_dict)
    return ticker_dict



def get_ticker_list(dict_list):
    return [d['Ticker'] for d in dict_list]

