# -*- coding: utf-8 -*-
# author:BerryHN
#workbook.save("/Users/zhiren1111/Desktop/csv2.xls")


import pandas  as pd
file=pd.read_excel("/Users/zhiren1111/Desktop/csv2.xls",header=None)
file.columns=["ip","lng","wegt","province","city"]

print file.columns

file.to_csv("/Users/zhiren1111/Desktop/test3.csv",index=False,encoding='GB18030')



