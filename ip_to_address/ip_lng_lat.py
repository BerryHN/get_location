# -*- coding: utf-8 -*-
# author:BerryHN
'''
    调用百度API -- 解析ip所在的省和市，以及城市中心
'''

import requests
import sys, urllib, urllib2
from is_ip import  is_ip
ip=["223.104.187.124","123.157.216.202","113.122.226.248.161"]
def get_address(ip):
    ip_new=is_ip(ip)
    if ip_new:
        import json
        url = "http://api.map.baidu.com/location/ip?ip=" + ip_new + "&ak=TkMNAR7XQq4YlAYqp2IDDkWwE7mknAxe&coor=gcj02"
        a=requests.get(url)
        lng=list()
        json=json.loads(a.text)
        if json["status"]==0:
            log=json["content"]["point"]["x"]
            lat=json["content"]["point"]["y"]
            province=json["content"]["address_detail"]["province"]
            city=json["content"]["address_detail"]["city"]
            lng.append(log)
            lng.append(lat)
            lng.append(province)
            lng.append(city)
        address=tuple(lng)
        print address
        return address
    else:
        return "","","",""
for i in ip:
    t=get_address(i)
    for j in t:
        print j







