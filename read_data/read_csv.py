# -*- coding: utf-8 -*-
# author:BerryHN
from collections import namedtuple
import  csv



with open("/Users/zhiren1111/Desktop/csv.csv","rU")  as f:
    f_csv=csv.reader(f,dialect=csv.excel_tab)
    f2 = open("/Users/zhiren1111/Desktop/test2.csv", "wb")
    writer = csv.writer(f2)
    headers=next(f_csv)
    headers=namedtuple("Row",headers)
    for line in f_csv:
        print line
        writer.writerow(line)





with open("/Users/zhiren1111/Desktop/test.csv","rU")  as f:
    f_csv=csv.DictReader(f,dialect=csv.excel_tab)





