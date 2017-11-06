# -*- coding: utf-8 -*-
# author:BerryHN

import xlrd
data=xlrd.open_workbook("/Users/zhiren1111/Desktop/test.xls")
table=data.sheets()[0]
nrows=table.nrows
for i in range(nrows):
    if i==0:
        continue
    print table.row_values(i)[:13]