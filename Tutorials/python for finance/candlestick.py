#candlestick
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates 
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2012,1,1)
end = dt.datetime(2016,12,31)

df = pd.read_csv('C:/Users/Backup.AjithkumarS-PC/tlsa.csv', parse_dates=True, index_col=0)

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
plt.ylabel('Price($)')
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()
plt.xlabel('Year')
plt.ylabel('Volume(1e9)')

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)


plt.show()
