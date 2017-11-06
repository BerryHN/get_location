# -*- coding: utf-8 -*-
# author:BerryHN
import urllib, urllib2, sys
import ssl
import json

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=jxPsaOuAb5qV0SAlHRplrNjD&client_secret=rlIKKC1zHvZKULz0KwcbtjGVI6Wr4ldu'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
content=json.loads(content)

if (content):
    print content["access_token"]