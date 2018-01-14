#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 23:31:50 2018

@author: bitzilla
"""

from binance.client import Client
from minance.utils import get_historical_klines


symbol = "ETHBTC"
start = "1 Jan, 2018"
end = None
interval = Client.KLINE_INTERVAL_30MINUTE

klines = get_historical_klines(symbol, interval, start, end)
print(klines)
