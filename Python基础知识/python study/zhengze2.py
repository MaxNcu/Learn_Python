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
#re.I 匹配大小写
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
a = 'abBcC123456'
pa1 = re.compile('([a-z|0-9])*',re.I)
ma1 = pa1.findall(a)
for x in ma1:print x
ma2 = pa1.search(a)
print ma2.group()

# pa3 = re.compile('.')
# ma3 = pa3.match(a)
# print ma3.group()