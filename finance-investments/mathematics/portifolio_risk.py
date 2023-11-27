import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import yfinance as yf

yf.pdr_override()

# Portfolio composed of Procter & Gamble, Microsoft, Ford, General Eletric
tickers = ['PG', 'BEI.DE']
sec_data = pd.DataFrame()
for t in tickers:
    sec_data[t] = wb.DataReader(t, start='2007-01-01')['Adj Close']

print(sec_data.tail())

sec_returns = np.log(sec_data / sec_data.shift(1))
print(sec_returns)

# Calculating Portifolio Risk

# Equal weighthing scheme:
weights = np.array([0.5, 0.5])

print(weights)

# Portfolio Variance:
pfolio_var = np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))

print(pfolio_var)

# Portifolio Volatily
pfolio_vol = (np.dot (weights.T, np.dot(sec_returns.cov() * 250, weights))) **0.5
print(str(round(pfolio_vol, 5) * 100) + '%')

