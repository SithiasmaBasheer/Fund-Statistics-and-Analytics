# Import libraries
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

# Set styple for ploting
style.use('ggplot')

# Output file name
file_name = r'C:\StockAnalytics.csv'

# Assign Start and End date for stocks
start = dt.datetime(2017, 1, 1)
end = dt.datetime.now()

# Using web.DataReader from Pandas_datareader , call stocks API
df = web.DataReader('^DJI', 'stooq', start, end)

# write data to csv
df.to_csv(file_name, sep=';', encoding='utf-8')
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)

print(df.head())

# using matplotlib , plot graph from df
df.plot()
plt.show()

df['Volume'].plot()
plt.show()