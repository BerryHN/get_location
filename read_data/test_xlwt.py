# -*- coding: utf-8 -*-
# author:BerryHN

import xlwt

workbook=xlwt.Workbook()

sheet1=workbook.add_sheet("sheet1",cell_overwrite_ok=True)
sheet2=workbook.add_sheet("sheet2",cell_overwrite_ok=True)
sheet1.write(0,0,"this should overwrite1")
sheet1.write(0,1,"aaaaaaaa")
sheet2.write(0,0,"this should overwrite2")
sheet2.write(1,2,"bbbbbbbb")
sheet2.write(2,3,u"曹晓光")

workbook.save("/Users/zhiren1111/Desktop/test2.xls")