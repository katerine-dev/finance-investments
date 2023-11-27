import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

# Portfolio composed of Procter & Gamble, Microsoft, Ford, General Eletric
tickers = ['PG', 'BEI.DE']
sec_data = pd.DataFrame()
for t in tickers:
    sec_data[t] = wb.DataReader(t, start='2007-01-01')['Adj Close']

print(sec_data.tail())

sec_returns = np.log(sec_data / sec_data.shift(1))
print(sec_returns)

# MEAN - P&G
print(sec_returns['PG'].mean())

print(sec_returns['PG'].mean() * 250)  # only business days

# STANDARD DEVIATION = P&G
print(sec_returns['PG'].std())

print(sec_returns['PG'].std() * 250 ** 0.5)  # only business days and scalar potencial to 0.5

# MEAN - Beiersdorf

print(sec_returns['BEI.DE'].mean())

print(sec_returns['BEI.DE'].mean() * 250)  # only business day

# STANDARD DEVIATION - Beiersdorf

print(sec_returns['BEI.DE'].std())

print(sec_returns['BEI.DE'].std() * 250 ** 0.5)  # only business days and scalar potencial to 0.5

print("******** results ********")
print(sec_returns['PG'].mean() * 250)
print(sec_returns['BEI.DE'].mean() * 250)


# print(sec_returns['PG', 'BEI.DE'].mean() * 250) ---- need to put in array
# Array (mean)
print(sec_returns[['PG', 'BEI.DE']].mean() * 250)
# Array (volatility)
print(sec_returns[['PG', 'BEI.DE']].std() * 250 ** 0.5)



