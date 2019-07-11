# -*- coding: utf-8 -*-
"""
__author__ = 'Langziyanqin'
__QQ__ = '982722261'
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import sys
import re
import requests
import json
import urllib2
reload(sys)
sys.setdefaultencoding('utf-8')
#get post
#head  相当于get  但是响应速度更快  requests.head
data = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }
json1 = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
#print json1
json2 = json.loads(json1)
#json2 = json.loads(url.read())
#print json2
#print json2['b']
try:
    req = urllib2.urlopen(url='http://www.jb51.net/article/73450.htm')
    print req.info()
except Exception,e:
    print e
try:
    json3 = json.loads(req.read())
    print json3
except Exception,e:
    print e.args

req2 = requests.get(url = 'https://www.baidu.com/')
try:
    print req2.json()
except Exception,e:
    print e