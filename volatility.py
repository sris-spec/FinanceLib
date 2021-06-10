import numpy as np
import pandas_datareader as pdr
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
def volatility(symbol):
    start = dt.datetime(2020, 1, 1)
    data = pdr.get_data_yahoo(symbol, start)
    data.head()
    high_low = data['High'] - data['Low']
    high_cp = np.abs(data['High'] - data['Close'].shift())
    low_cp = np.abs(data['Low'] - data['Close'].shift())
    df = pd.concat([high_low, high_cp, low_cp], axis=1)
    true_range = np.max(df, axis=1)
    average_true_range = true_range.rolling(14).mean()
    average_true_range
    true_range.rolling(14).sum()/14
    
    fig, ax = plt.subplots()
    average_true_range.plot(ax=ax)
    ax2 = data['Close'].plot(ax=ax, secondary_y=True, alpha=.3)
    ax.set_ylabel("ATR")
    ax2.set_ylabel("Price")
symbol=input()# Sample input: GOOG
v=volatility(symbol)