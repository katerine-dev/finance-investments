import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import yfinance as yf

ser = pd.Series(np.random.random(5), name="Column 01")

print(ser)

print(ser[2])

yf.pdr_override()

PG = wb.get_data_yahoo('PG', start='1995-1-1')
# PG is the ticker
print(PG)

print(PG.info())  # information from datatable
print(PG.head())  # first lines
print(PG.tail())  # last lines
print(PG.head(20))
print(PG.head(20))

# Companies: Procter & Gamble, Microsoft, AT&T, Ford, General Eletric
tickers = ['PG', 'MSFT', 'T', 'F', 'GE']
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t, start='1995-1-1')['Adj Close']  # 'Adj close' (adjusted closure, name column)
print(new_data.tail())
