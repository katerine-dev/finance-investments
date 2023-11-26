import pandas as pd
from pandas_datareader import data as wb
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

# Indices S&P500, NASDAQ, DAX, Financial Times Stock Exchange
tickers = ['^GSPC', '^IXIC', '^GDAXI', '^FTSE']
ind_data = pd.DataFrame()
for t in tickers:
    ind_data[t] = wb.DataReader(t, start='1995-01-01')['Adj Close']

print(ind_data.head())
print(ind_data.tail())

(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()

# simples return
ind_returns = (ind_data / ind_data.shift(1)) - 1

print(ind_returns.tail())

# annual return
annual_ind_returns = ind_returns.mean() * 250
print(annual_ind_returns)

# Indices Procter & Gamble S&P500, Dow Jones
tickers = ['PG', '^GSPC', '^DJI']
data_2 = pd.DataFrame()
for t in tickers:
    data_2[t] = wb.DataReader(t, start='1995-01-01')['Adj Close']

print(data_2.tail())

(data_2 / data_2.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()

