import pandas as pd
import matplotlib.pyplot as plt
import datetime
import time
plt.style.use('seaborn-v0_8-bright')
import yfinance as yf
import numpy


Stocks = [
    {"ticker":"BTC-USD"},
    {"ticker":"ETH-USD"},
    {"ticker":"AAPL"},
    {"ticker":"TSLA"},
    {"ticker":"META"},
]

def wait_for_next_round_hour():
    current_time = datetime.datetime.now()
    next_hour = current_time.replace(minute=0, second=0, microsecond=0) + datetime.timedelta(hours=1)+ datetime.timedelta(seconds=10) 
    time_to_wait = round((next_hour - current_time).total_seconds(), 0)
    print(f'Waiting {time_to_wait} seconds for next hour candles...')
    time.sleep(time_to_wait)
    # Optional: Print a message once the waiting is over
    print("Next hour candles has arrived!")

def get_last_price(ticker):
    t= yf.Ticker(ticker)
    prices = t.history(period="2d", interval="1h")
    prices['Percentage'] = prices['Close'].pct_change()*100
    pricelog = prices.iloc[-2]
    #print(calculate_change)
    return numpy.round(pricelog['Percentage'], 2), numpy.round(pricelog['Close'], 2)


def get_tickers_data(tickers):
    data = yf.download(tickers, period="2d", interval="1h",prepost = False)
    data= data.drop(['Volume', 'Adj Close', 'High','Low', 'Open'], axis=1)
    print(data['Close', 'BTC-USD'])
    for ticker in tickers:
        data['Percentage', ticker] = data['Close', ticker].pct_change()*100
    print(data.tail(2))


def sort_dict_list_by_change(dict_list):
    sorted_list = sorted(dict_list, key=lambda x: x['change'], reverse=True)
    return sorted_list

def get_ticker_list(dict_list):
    return [d['ticker'] for d in dict_list]


def main():
    global Stocks
    print(get_tickers_data(get_ticker_list(Stocks)))
    return
    while True:
        
        
        for stock in Stocks:
            change, last = get_last_price(stock['ticker'])
            stock['change'] = change
            stock['last'] = last
        Stocks = sort_dict_list_by_change(Stocks)
        print(Stocks)


if __name__ == '__main__':
    main()
