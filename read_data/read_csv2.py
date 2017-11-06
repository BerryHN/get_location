# -*- coding: utf-8 -*-
# author:BerryHN
from collections import namedtuple
import  csv

import pandas as pd
from ip_to_address.ip_lng_lat import  get_address
import xlwt

import datetime
starttime=datetime.datetime.now()
workbook=xlwt.Workbook()

sheet1=workbook.add_sheet("sheet1",cell_overwrite_ok=True)
sheet2=workbook.add_sheet("sheet2",cell_overwrite_ok=True)
data =pd.read_csv("/Users/zhiren1111/Desktop/csv2.csv",header=1,encoding="GB18030",sep=",")
columns=data.columns

rnums= len(data)
cnums= len(columns)
ips=data[["zip"]].values

list=[u"曹晓光",u"临安"]
x="\n".join(list)
for i in range(rnums):
    a=get_address(ips[i][0])
    sheet1.write(i, 0, ips[i][0])
    for j in range(1,len(a)+1):
        sheet1.write(i, j, a[j-1])
    sheet1.write(10,2,x)




workbook.save("/Users/zhiren1111/Desktop/csv2.xls")

















