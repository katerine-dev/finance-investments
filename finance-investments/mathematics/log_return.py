import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import yfinance as yf

yf.pdr_override()

PG = wb.get_data_yahoo('PG', start='1995-01-01')

print(PG.head())
print(PG.tail())

# LOG RETURNS

PG['log_return'] = np.log(PG['Adj Close'] / PG['Adj Close'].shift(1))
print(PG['log_return'])


# PLOT
PG['log_return'].plot(figsize=(8, 5))
plt.show()

log_returns_d = PG['log_return'].mean()  # calculates the average daily rate of return

print(log_returns_d)

# Only business days, real average return

log_returns_a = PG['log_return'].mean() * 250

print(log_returns_a)  # per year

print(str(round(log_returns_a, 5) * 100) + '%')  # final percentage, a litte smaller than the simple return
