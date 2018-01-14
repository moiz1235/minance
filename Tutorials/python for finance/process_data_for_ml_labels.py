#ML percent_change
import bs4 as bs
import pickle 
import requests
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

def process_data_for_labels(ticker):
	hm_days= 7
	df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
	tickers= df.columns.values.tolist()
	df.fillna(0,inplace=True)
	
	for i in range(1, hm_days+1):
		df['{}_{}d'.format(ticker, i)]= (df[ticker].shift(-i) - df[ticker])/(df[ticker])
		
	df.fillna(0, inplace=True)
	return tickers, df
	
process_data_for_labels('MMM')