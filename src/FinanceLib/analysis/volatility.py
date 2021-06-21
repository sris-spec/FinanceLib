from typing import List, Union
import numpy as np
import pandas_datareader as pdr

import pandas as pd
import matplotlib.pyplot as plt
def volatility(symbol :str, date :str) ->None:
    """
    Measures and visualizes the Volatility of a Stock by calculating the Average True Range(ATR)
    Parameters:
        symbol(str) : Symbol of the company from  https://in.finance.yahoo.com/
        date(str) : start date of historical data in the format (YYYY,M,D)        
    Returns:
        Return type: void
    Example:
        volatility('GOOG','2020,01,01')    

    """
    
    data : str = pdr.get_data_yahoo(symbol,date)
    data.head()
    high_low : Union[int,float]= data['High'] - data['Low']
    high_cp : List[float] = np.abs(data['High'] - data['Close'].shift())
    low_cp : List[float]= np.abs(data['Low'] - data['Close'].shift())
    df : List[str] = pd.concat([high_low, high_cp, low_cp], axis=1)
    true_range : float= np.max(df, axis=1)
    average_true_range : float= true_range.rolling(14).mean()
    average_true_range
    true_range.rolling(14).sum()/14
    
    fig, ax = plt.subplots()
    average_true_range.plot(ax=ax)
    ax2 : Union[bool,float]= data['Close'].plot(ax=ax, secondary_y=True, alpha=.3)
    ax.set_ylabel("ATR")
    ax2.set_ylabel("Price")
    plt.show()
#volatility('GOOG','2020,01,01')
