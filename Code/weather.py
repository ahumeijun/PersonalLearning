#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, urllib, urllib2, json

url = 'http://apis.baidu.com/heweather/weather/free?city=beijing'
appkey = '75d9cb08b74346ac08d21e5e55217904'

req = urllib2.Request(url)

req.add_header("apikey", appkey)

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)