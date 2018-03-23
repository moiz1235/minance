import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2012,1,1)
end = dt.datetime(2016,12,31)

df = pd.read_csv('C:/Users/Backup.AjithkumarS-PC/tlsa.csv', parse_dates=True, index_col=0)

df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
#df.dropna(inplace=True)
print(df.head())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
plt.xlabel('Year')
plt.ylabel('Price($)')
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1) # shareax allows zoom to perform on both subplots
plt.xlabel('Year')
plt.ylabel('Volume(1e8)')

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()
