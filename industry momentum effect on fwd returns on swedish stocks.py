# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:04:51 2021

@author: richa
"""



import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import math
from datetime import date

#get prices from yahoo finance

tday = date.today()
tday_str = tday.strftime("%Y-%m-%d")
#=============================================================================
# =============================================================================
se_str = 'EVO.ST KIND-SDB.ST KAMBI.ST BETS-B.ST LEO.ST'
intl_str ='LVS FLTR.L EVO.ST MGM CZR ENT.L WYNN CHDN PENN BYD SGMS'

gaming_hist = yf.download(intl_str + ' ' +  se_str, start='2015-01-01', end=tday_str)

# =============================================================================
#=============================================================================
# 
# hist = yf.download('ALIG.ST CCC.ST BALCO.ST BERG-B.ST'
#                    ' COIC.ST HLDX.S LIAB.ST MTRS.ST NCC-B.ST'
#                    ' NMAN.ST SYSR.ST', start='2015-01-01', end=tday_str)

close_prices_gaming = gaming_hist["Adj Close"]#.dropna(how='all').fillna(0)


#calculate daily returns
ret_daily_gaming = close_prices_gaming.pct_change()


#calculate 20 day returns
ret_20d_gaming = close_prices_gaming.pct_change(20)

gaming_ret_intl = pd.concat([ret_daily_gaming['LVS'], ret_daily_gaming['FLTR.L'], ret_daily_gaming['EVO.ST']],axis= 1)
gaming_ret_se = pd.concat([ret_daily_gaming['EVO.ST'], ret_daily_gaming['KIND-SDB.ST'], ret_daily_gaming['KAMBI.ST']],axis= 1)

gaming_20d_intl = pd.concat([ret_20d_gaming['LVS'], ret_20d_gaming['FLTR.L'], ret_20d_gaming['EVO.ST']],axis= 1)
gaming_20d_se = pd.concat([ret_20d_gaming['EVO.ST'], ret_20d_gaming['KIND-SDB.ST'], ret_20d_gaming['KAMBI.ST']],axis= 1)


pos_ind = gaming_20d_intl.mean(axis=1) > 0 

pd.concat(pos_ind

long_returns_daily = np.multiply(gaming_ret_se,pos_ind.shift(2))


cum_ret =(1 + long_returns_daily.mean()).cumprod()