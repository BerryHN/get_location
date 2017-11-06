# -*- coding: utf-8 -*-
# author:BerryHN
# encoding:utf-8
import base64
import urllib
import urllib2

'''
人脸对比
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v2/match"

f = open('/Users/zhiren1111/Desktop/cao.jpg', 'rb')
# 参数images：图像base64编码
img1 = base64.b64encode(f.read())
# 二进制方式打开图文件
f = open('/Users/zhiren1111/Desktop/cao3.jpg', 'rb')
# 参数images：图像base64编码
img2 = base64.b64encode(f.read())

params = {"images":img1 + ',' + img2}
params = urllib.urlencode(params)

access_token = '24.06a1c20fbdcf40764946c1aa23accb2b.2592000.1509349184.282335-10206533'
request_url = request_url + "?access_token=" + access_token
request = urllib2.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
content = response.read()
if content:
    print content