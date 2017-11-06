# -*- coding: utf-8 -*-
# author:BerryHN
import csv
csvfile=file("/Users/zhiren1111/Desktop/test2.csv","wb")
writer=csv.writer(csvfile,dialect='excel')
writer.writerow(['id','url','keywords'])
data=[
    ('1','http://www.xiaoheiseo.com','小黑')
    ,
    ('1','http://www.baidu.com/','百度'),
    ('3','http://www.jd.com/','京东')
    ]
writer.writerows(data)
csvfile.close()
