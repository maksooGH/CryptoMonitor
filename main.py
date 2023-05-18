import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
#print(plt.style.available)
plt.style.use('seaborn-v0_8-bright')


import yfinance as yf



apple= yf.Ticker("aapl")

# show actions (dividends, splits)
aapl_historical = apple.history(period="5d", interval="1m")
print(type(apple.news))

for y in apple.news:
    print(y)
#for key, value in stockinfo.items():    
#    print(f"{key}: {value}")