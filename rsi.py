import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt

def rsi(symbol,name):
    ticker = pdr.get_data_yahoo(symbol, dt.datetime(2019,1,1), dt.datetime.now())
    delta = ticker['Close'].diff()
    up = delta.clip(lower=0)
    down = -1*delta.clip(upper=0)
    ema_up = up.ewm(com=13, adjust=False).mean()
    ema_down = down.ewm(com=13, adjust=False).mean()
    rs = ema_up/ema_down
    ticker['RSI'] = 100 - (100/(1 + rs))
    ticker = ticker.iloc[14:]
    print(ticker)
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.get_xaxis().set_visible(False)
    fig.suptitle(name)
    ticker['Close'].plot(ax=ax1)
    ax1.set_ylabel('Price ($)')
    ticker['RSI'].plot(ax=ax2)
    ax2.set_ylim(0,100)
    ax2.axhline(30, color='r', linestyle='--')
    ax2.axhline(70, color='r', linestyle='--')
    ax2.set_ylabel('RSI')
    plt.show()
symbol=input()
name=input()
r=rsi(symbol,name)