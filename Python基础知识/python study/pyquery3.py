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
from pyquery import PyQuery as pq
reload(sys)
sys.setdefaultencoding('utf-8')
r = requests.get('http://www.baidu.com')
# d = pq(r.content)
u = unicode(r.content, 'utf-8')
d = pq(u)
#print d

d1 = pq(url='http://eladies.sina.com.cn/photo/')
d2 = d1('ul')#.find('a')#.attr('href')
r1 = re.findall('href="(.*?)" target=',str(d2))
for x in r1:print x