import yfinance as yf
import numpy
import src.utls as utls
import pandas as pd


def get_tickers_data(tickers_list):
    data = yf.download(tickers_list, period="2d", interval="1h")
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
    for ticker in ticker_dict:
        percentage_to_dict = round(s['Percentage', ticker['Ticker']].iloc[-2], 2)
        ticker['LastChange'] = percentage_to_dict
        ticker['LastCheckTime'] = candle_date
    ticker_dict = sort_dict_list_by_change(ticker_dict)
    return ticker_dict

def sort_dict_list_by_change(dict_list):
    sorted_list = sorted(dict_list, key=lambda x: x['LastChange'], reverse=True)
    return sorted_list

def get_ticker_list(dict_list):
    return [d['Ticker'] for d in dict_list]