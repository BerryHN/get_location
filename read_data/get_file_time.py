# -*- coding: utf-8 -*-
# author:BerryHN

import os
import time
import os.path

def get_file_ctime(f):
    if os.path.isfile(f)==True:
        chtime=time.ctime(os.path.getctime(f))
    return chtime

def get_file_mtime(f):
    if os.path.isfile(f)==True:
        mtime=time.ctime(os.path.getmtime(f))
    return mtime



