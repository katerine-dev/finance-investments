import quandl
import pandas as pd
mydata_01 = quandl.get("FRED/GDP")

print(mydata_01.tail())

print(mydata_01.head())

mydata_01.to_csv("~/Documents/finance-investments/docs/csv/Data_02.csv")

mydata_02 = pd.read_csv("~/Documents/finance-investments/docs/csv/Data_02.csv")

print(mydata_02.head())

print(mydata_02.tail())

mydata_02.to_excel("~/Documents/finance-investments/docs/csv/example_excel.xlsx")

mydata_03 = pd.read_excel("~/Documents/finance-investments/docs/csv/example_excel.xlsx")

print(mydata_03)

