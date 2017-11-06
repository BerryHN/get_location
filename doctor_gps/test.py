# -*- coding: utf-8 -*-
# author:BerryHN
import pandas as pd

import numpy  as np
from cal_distinct import  *

data=pd.read_csv("/Users/zhiren1111/Desktop/doctor_log_lat.csv",header=0,encoding="GB18030")

print data.shape[1]