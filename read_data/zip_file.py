# -*- coding: utf-8 -*-
# author:BerryHN
"""

1、读取制定目录下的所有文件

"""
import sys
import zipfile
import os
import get_file_time




def  eachFile(filepath,targetpath):

    sep=os.sep
    if os.path.exists(filepath)==True:
        pathDir=os.listdir(filepath)
        for allDir in pathDir:
            if os.path.splitext(allDir)[1]=='.zip':
                child = os.path.join('%s%s%s' % (filepath,sep,allDir))
                file_zip=zipfile.ZipFile(child,'r')
                for file in file_zip.namelist():
                    child2 = os.path.join('%s%s%s' % (targetpath, sep, os.path.splitext(allDir)[0]))
                    file_zip.extract(file,child2)
                file_zip.close()
    return



filepath="/Users/zhiren1111/Desktop/doctor_analysis"
targetpath="/Users/zhiren1111/Desktop/doctor_analysis"
file_name=eachFile(filepath,targetpath)




