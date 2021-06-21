from typing import List, Union
import pandas_datareader as pdr

import matplotlib.pyplot as plt

def rsi(symbol :str ,name :str, date :str) -> None :
    """
    Calculates and visualises the Relative Stock Index on a Stock of the company.

    Parameters:
        symbol(str) : Symbol of the company from  https://in.finance.yahoo.com/
        name(str) : Name of the company
        date(str) : start date of historical data in the format (YYYY,M,D)
    Returns:
        Return type: void  
    Example:
        rsi('GOOG','Google','2020,01,01')     

    """
    ticker : str = pdr.get_data_yahoo(symbol, date)
    delta : List[float]  = ticker['Close'].diff()
    up : int   = delta.clip(lower=0)
    down : int = -1*delta.clip(upper=0)
    ema_up : Union[bool,float]= up.ewm(com=13, adjust=False).mean()
    ema_down : Union[bool,float] = down.ewm(com=13, adjust=False).mean()
    rs : float = ema_up/ema_down
    ticker['RSI'] = 100 - (100/(1 + rs))
    ticker : list = ticker.iloc[14:]
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
#rsi('GOOG','Google','2020,01,01')
