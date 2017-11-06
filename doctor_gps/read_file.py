# -*- coding: utf-8 -*-
# author:BerryHN
import pandas as pd

import numpy  as np
from cal_distinct import  *

data=pd.read_csv("/Users/zhiren1111/Desktop/doctor_log_lat.csv",header=0,encoding="GB18030")
columns=data.columns
data2=data
data2.columns=["doctor_user_id","doctor_name","hospital_name","province_name","city_name","log","lat","local_log","local_lat"]

data3=data2[list(data.columns[1:len(data.columns)])]

data3.index=data2["doctor_user_id"]


for ix,row in data3.iterrows():
    log=row["log"]
    lat=row["lat"]
    local_log=row["local_log"]
    local_lat=row["local_lat"]
    distiance=get_distinct(lat,log,local_lat,local_log)
    distiance=round(distiance)
    data3.loc[ix,"distance"]=distiance


data3.to_csv("/Users/zhiren1111/Desktop/doctor_log_lat.csv",header=data3.columns,encoding="GB18030")
