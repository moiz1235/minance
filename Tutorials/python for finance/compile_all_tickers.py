#compile all
import bs4 as bs
import pickle 
import requests
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web

def save_sp500_tickers():
	resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
	soup = bs.BeautifulSoup(resp.text, 'lxml')
	table = soup.find('table', {'class':'wikitable sortable'})
	tickers= []
	for row in table.findAll('tr')[1:]:
		ticker = row.findAll('td')[0].text
		tickers.append(ticker)
	with open("sp500tickers.pickle", "wb") as f:
		pickle.dump(tickers, f)
	print(tickers)
	return tickers
	
#save_sp500_tickers()

def get_date_from_yahoo(releaod_sp500=False):
	if(releaod_sp500):
		tickers = save_sp500_tickers()
	else:
		with open("sp500tickers.pickle", "rb") as f:
			tickers = pickle.load(f)
	
	if not os.path.exists('stock_dfs'):
		os.makedirs('stock_dfs')
	
	start = dt.datetime(2015, 1 , 1)
	end = dt.datetime(2017, 12, 31)
	
	for ticker in tickers: #use the same number from save_stock_info_of_selected_tickers.py
		if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
			df = web.DataReader(ticker, 'yahoo', start, end)
			df.to_csv('stock_dfs/{}.csv'.format(ticker))
		else:
			print('Already have {}'.format(ticker))
	
		print(ticker)
			
#get_date_from_yahoo()

def compile_data():
	with open('sp500tickers.pickle', 'rb') as f:
		tickers = pickle.load(f)
	
	main_df = pd.DataFrame()

	for count, ticker in enumerate(tickers): #use the same number get_date_from_yahoo
		df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
		df.set_index('Date', inplace=True)
		
		df.rename(columns = {'Adj Close': ticker}, inplace=True)
		df.drop(['Open','High','Low','Close','Volume'], 1, inplace=True)
		
		if main_df.empty:
			main_df = df
		else:
			main_df = main_df.join(df, how='outer')
			
		if count%5 ==0:
			print(count)
			
	print(main_df.head())
	main_df.to_csv('sp500_joined_closes.csv')
	
compile_data()