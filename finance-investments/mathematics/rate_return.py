from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import yfinance as yf

yf.pdr_override()

PG = wb.get_data_yahoo('PG', start='1995-01-01')

print(PG.head())
print(PG.tail())


PG['simple_return'] = (PG['Adj Close']/PG['Adj Close'].shift(1)) - 1
print(PG['simple_return'])  # daily closing percentage

# PLOT
PG['simple_return'].plot(figsize=(8, 5))
plt.show()

avg_returns_d = PG['simple_return'].mean()  # calculates the average daily rate of return

print(avg_returns_d)

# Only business days, real average return

avg_returns_a = PG['simple_return'].mean() * 250

print(avg_returns_a)  # per year

print(str(round(avg_returns_a, 5) * 100) + '%')  # final percentage
