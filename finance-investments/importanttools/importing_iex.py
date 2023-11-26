import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from datetime import datetime
import os

start = datetime(2018, 1, 1)
end = datetime(2018, 12, 31)
api_key = os.environ.get('IEX_API_KEY')
PG = wb.DataReader('PG', data_source = 'iex', start=start, end=end, api_key=api_key)

print(PG)

tickers = ['PG', 'MSFT', 'T', 'F', 'GE']
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t, data_source = 'iex', start=start, api_key=api_key)['close']

print(new_data.tail())


# API (https://iexcloud.io/)

