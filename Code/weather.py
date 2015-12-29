#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json
import urllib.request
import urllib.response
import urllib.error

url = 'http://apis.baidu.com/heweather/weather/free?city=London'
appkey = '75d9cb08b74346ac08d21e5e55217904'

req = urllib.request.Request(url)

req.add_header("apikey", appkey)

resp = urllib.request.urlopen(req)
content = resp.read()
if(content):
    print(content)
    print("你好世界")