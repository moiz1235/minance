All the imports required for the tutorial

import bs4 as bs # For html scraping

import pickle # For session save and restore

import requests # For Web query

import datetime as dt # For date and time

import os # For system operations

import pandas as pd # For data manipulation

import pandas_datareader.data as web # For getting stock data

import matplotlib.pyplot as plt # For visualization

from matplotlib import style # Plotting styles

import numpy as np
 
from collections import Counter # For spread calcluation

from sklearn import svm, cross_validation, neighbors

from sklearn.ensemble import VotingClassifier, RandomForestClassifier

Order of tutorial

1.  Save_apple_to_csv.py
2.  plot_from_csv.py
3.  moving_average.py
4.  candlestick.py
5.  get_tickers_from_web.py
6.  save_stock_info_of_selected_tickers.py
7.  compile_all_tickers.py
8.  correlation.py
9.  process_data_for_ml_labels.py
10. buy_sell_hold_labels.py
11. extract_features.py
12. ml.py (Final showdown)
