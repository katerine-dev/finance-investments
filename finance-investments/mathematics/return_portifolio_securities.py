import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

# Portfolio composed of Procter & Gamble, Microsoft, Ford, General Eletric
tickers = ['PG', 'MSFT', 'F', 'GE']
my_data = pd.DataFrame()
for t in tickers:
    my_data[t] = wb.DataReader(t, start='1995-01-01')['Adj Close']

my_data.info()

print(my_data.head())
print(my_data.tail())

# Normalization to 100

print(my_data.iloc[0])

(my_data / my_data.iloc[0] * 100).plot(figsize=(15, 6))

# The idea of this operation is to compare the behavior of the 4 stocks, as if they were starting with the same value,
# in this case 100
plt.show()

# Calculatuing the return of a portfolio of securities
returns = (my_data / my_data.shift(1)) - 1
print(returns.head())

# equal weights for each stock quotes, here it is necessary to calculate the product of the wight of each stock by
# its return
weights = np.array([0.25, 0.25, 0.25, 0.25])

annual_returns = returns.mean() * 250

print(annual_returns)

print(np.dot(annual_returns, weights))

pfolio_1 = str(round(np.dot(annual_returns, weights), 5) * 100) + '%'

print(pfolio_1)  # annual return

weights_2 = np.array([0.4, 0.4, 0.15, 0.5])

pfolio_2 = str(round(np.dot(annual_returns, weights_2), 5) * 100) + '%'

# TO COMPARE PORTFOLIO

print(pfolio_1)
print(pfolio_2)

