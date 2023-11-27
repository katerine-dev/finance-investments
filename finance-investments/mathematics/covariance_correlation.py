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

# Covariance and correlation

# Variance
PG_var = sec_returns['PG'].var()
print(PG_var)

BEI_var = sec_returns['BEI.DE'].var()
print(BEI_var)

PG_var_a = sec_returns['PG'].var() * 250
print(PG_var_a)

BEI_var_a = sec_returns['BEI.DE'].var() * 250
print(PG_var_a)

# Covariance

cov_matriz = sec_returns.cov()  # eguals covariance
print(cov_matriz)

cov_matriz_a = sec_returns.cov() * 250
print(cov_matriz_a)

# Correlation
corr_matriz = sec_returns.corr()
print(corr_matriz)

