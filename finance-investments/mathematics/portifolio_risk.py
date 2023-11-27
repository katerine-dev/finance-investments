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

# Calculating Diversifiable and Non-Diversifiable Risk of a Portfolio

print(weights[0])
print(weights[1])

# diversifiable risk = portfolio variance - weighted annual variance
# Diversifiable Risk

PG_var_a = sec_returns[['PG']].var() * 250
print(PG_var_a)

BEI_var_a = sec_returns[['BEI.DE']].var() * 250
print(BEI_var_a)

dr = pfolio_var - (weights[0] ** 2 * PG_var_a) - (weights[1] ** 2 * BEI_var_a)

print(dr)

#print(float(PG_var_a))

# Correct

PG_var_a = sec_returns['PG'].var() * 250
print(PG_var_a)

BEI_var_a = sec_returns['BEI.DE'].var() * 250
print(BEI_var_a)

dr = pfolio_var - (weights[0] ** 2 * PG_var_a) - (weights[1] ** 2 * BEI_var_a)

print(dr)

print(str(round(dr*100, 3)) + '%')

# Non-diversifiable risk
n_dr_1 = pfolio_var - dr
print(n_dr_1)

n_dr_2 = (weights[0] ** 2 * PG_var_a) - (weights[1] ** 2 * BEI_var_a)
print(n_dr_2)

n_dr_2 == n_dr_1
