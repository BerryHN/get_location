# -*- coding: utf-8 -*-
# author:BerryHN
# -*- coding: utf-8 -*-
# author:BerryHN
from is_lng_lat import  is_lng,is_lat
import requests
import json
import address
lng=["116.322987"]
lat=["39.983424"]

def get_province_city(lng,lat):
    url = "http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&location=" + lat + "," + lng + "&output=json&pois=1&ak=TkMNAR7XQq4YlAYqp2IDDkWwE7mknAxe"
    a = requests.get(url)
    raw_json = a.text.split("(")
    s = ""
    for i in range(len(raw_json)):

        if i == 0:
            continue
        else:
            s = s + raw_json[i]
    t = ""
    for i in range(len(s)):
        if i == len(s) - 1:
            continue
        else:
            t = t + s[i]
    address=list()
    raw_address=json.loads(t)
    if raw_address["status"] == 0:
        province=raw_address["result"]["addressComponent"]["province"]
        city=raw_address["result"]["addressComponent"]["city"]
        district=raw_address["result"]["addressComponent"]["district"]
        address.append(province)
        address.append(city)
        address.append(district)
    else:
        address=''
    address=tuple(address)
    return address

for a in lng:
    for b in lat:
        if  is_lng(a)==True and is_lat(b)==True:
            address=get_province_city(a,b)
            address=address(address[0],address[1],address[2])
            print address.getProvince()
            print address.getCity()
            print address.getDistrict()

        else:
            print ''



