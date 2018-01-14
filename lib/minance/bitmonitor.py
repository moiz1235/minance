#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 11:03:47 2018

@author: bitzilla
This module is for functions/classes for looking into the crypto market
and getting data on select instruments.
"""
from __future__ import print_function
import os
from configobj import ConfigObj
from binance.client import Client
from binance.helpers import date_to_milliseconds, interval_to_milliseconds
from utils import get_historical_klines

class BitMonitor(object):
    """
    Class for monitoring the crypto market
    """
    config = ConfigObj(os.path.join(os.getenv("HOME"), "python", "config.ini"))

    def __init__(self):
        self.api_key = self.config["API_KEY"]
        self.api_secret = self.config["API_SECRET"]
