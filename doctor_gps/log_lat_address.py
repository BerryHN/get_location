# -*- coding: utf-8 -*-
# author:BerryHN
import requests
import json

lng="116.322987"
lat="39.983424"


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
    address=tuple(address)
    return address



a=get_province_city(lng,lat)
print a[0]
print a[1]
print a[2]