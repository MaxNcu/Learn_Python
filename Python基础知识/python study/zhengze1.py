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
#match 是从头开始匹配
#search 是全部匹配
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
a = 'aa.123ABC123123'
pa1 = re.compile('aa.*') #*代表全部
pa1 = re.compile('aa....') #一个。代表多匹配一个字符
pa1 = re.compile('^a.*') #必须a开头
pa1 = re.compile('.*?123') #任意开头 但是不贪婪
pa1 = re.compile('a....*?')
ma1 = pa1.match(a)

print ma1.group()
ma2 = re.search('.*',(re.S,re.I),a)