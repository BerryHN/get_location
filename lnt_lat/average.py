# -*- coding: utf-8 -*-
# author:BerryHN

import pandas as pd

import numpy  as np

data=pd.read_csv("/Users/zhiren1111/Desktop/lng.csv",header=None,encoding="GB18030")

data.columns=["user_id","ip","lng","lat","province","city"]
data2=data[list(data.columns[1:len(data.columns)])]

data2.index=data["user_id"].values

#print data2

lng=data2[["lng","lat"]].groupby(data2.index)
data3=lng.mean()
#print data3


new_data=pd.merge(data2,data3,how="inner",left_index=True,right_index=True)
print new_data.head