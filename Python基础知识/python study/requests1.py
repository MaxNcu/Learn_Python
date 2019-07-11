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
import requests
import re
reload(sys)
sys.setdefaultencoding('utf-8')
url = 'http://www.puahome.com/bbs/forum.php?gid=37'
req = requests.get(url)
print req.status_code
print req.headers
print req.is_redirect
print req.close()
print req.request
print req.history  #跳转
print req.reason
print req.url
print req.elapsed  #请求浪费多少时间
print req.encoding
print req.raw  #直接读取原始对象  print req.raw(10) 选前面是个
#content  原来格式 text 解析后的
print req.apparent_encoding
print req.text
print [line for line in req.text]
try:
    print req.json()
except Exception,e:
    print e