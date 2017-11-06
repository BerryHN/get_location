# -*- coding: utf-8 -*-
# author:BerryHN
import re
def is_lng(lng):
    import re
    lng=lng.strip()
    pattern=re.compile(r'[0-9]*\.*[0-9]+$')
    group=re.findall(pattern,lng)
    if not group:
        return False
    return abs(float(lng))<=180

def is_lat(lng):
    import re
    lng=lng.strip()
    pattern=re.compile(r'[0-9]*\.*[0-9]+$')
    group=re.findall(pattern,lng)
    if not group:
        return False
    return abs(float(lng))<=90
