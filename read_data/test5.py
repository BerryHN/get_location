# -*- coding: utf-8 -*-
# author:BerryHN
# encoding:utf-8
import base64
import urllib
import urllib2

import json
'''
人脸探测
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v1/detect"

# 二进制方式打开图片文件
f = open('/Users/zhiren1111/Desktop/cao3.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"face_fields":"age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities","image":img,"max_face_num":5}
params = urllib.urlencode(params)

access_token = '24.06a1c20fbdcf40764946c1aa23accb2b.2592000.1509349184.282335-10206533'
request_url = request_url + "?access_token=" + access_token
request = urllib2.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
content = response.read()
content=json.loads(content)

if content:
    print content
