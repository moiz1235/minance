import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2012,1,1)
end = dt.datetime(2016,12,31)

df = pd.read_csv('aapl.csv', parse_dates=True, index_col=0)
#print(df.head())

#df.plot()
#print(df[['Open','High']].head())
df['Adj Close'].plot()
plt.show()