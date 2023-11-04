#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 11:46:33 2023

@author: kamalib
"""
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from datetime import timedelta


# data=pd.read_csv("/Users/kamalib/Downloads/WALMART_SALES_DATA-1.csv")
# print(data)
# store = data.groupby(['Store']).agg({'Fuel_Price':['mean','max','sum']})
# store[:5]
# store2 = data.groupby(['Store']).agg({'Unemployment':['sum']})
# plt.figure(figsize = (15,8))
# store[('Fuel_Price',  'sum')].plot()
# plt.legend()
# plt.show()   


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta


data=pd.read_csv("/Users/kamalib/Downloads/WALMART_SALES_DATA-1.csv")
print(data)


store = data.groupby(['Store']).agg({'Fuel_Price':['mean','max','sum']})
store[:5]
store2 = data.groupby(['Store']).agg({'Unemployment':['sum']})
plt.figure(figsize = (15,8))
store[('Fuel_Price',  'sum')].plot()
store2[('unemployment','sum')].plot()
plt.legend()
plt.ylabel('price')
plt.xlabel('store')
plt.show()
