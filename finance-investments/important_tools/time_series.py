import pandas as pd

mydata_01 = pd.read_csv("~/Documents/finance-investments/docs/csv/Data_02.csv")

# print(mydata_01)

mydata_02 = pd.read_csv("~/Documents/finance-investments/docs/csv/Data_02.csv", index_col='Date')

# print(mydata_02)

mydata_01 = mydata_01.set_index('Date')

print(mydata_01)

# Convert a table to time series

