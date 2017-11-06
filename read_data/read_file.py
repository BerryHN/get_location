# -*- coding: utf-8 -*-
# author:BerryHN
"""

1、读取制定目录下的所有文件

"""
import os
import get_file_time
def  eachFile(filepath):
    filename=[]
    if os.path.exists(filepath)==True:
        pathDir=os.listdir(filepath)
        for allDir in pathDir:
            if allDir!=".DS_Store":
                child=os.path.join('%s%s'%(filepath,"/"+allDir))
                if os.path.isfile(child):
                    filename.append(child)
    return filename
file_name=eachFile("/Users/zhiren1111/Desktop/doctor_analysis")




for file in file_name:
    print file
