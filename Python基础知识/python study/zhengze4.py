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
reload(sys)
sys.setdefaultencoding('utf-8')
'''
*    匹配前一个字符0次或者无数次
+    匹配前一个字符1次或者无数次
？   匹配前一个字符1次或者0次
{m}  匹配前一个字符m次
{m,n}匹配M到n次
*？[0次]  +？[1次]  ？？[0次]  匹配模式变成非贪婪模式（尽可能少的匹配字符）

'''
ma = re.match(r'a+?','aaaaaaac')
print ma.group()

a = 'PpqQaAbB0123465798CcDdeEfF'
ma1 = re.search(r'[a-z][A-Z]*',a)
print ma1.group()   ##

ma2 = re.findall(r'[0-9]?[0-9]','09')
# for mm2 in ma2:print mm2
print ma2

ma3 = re.match(r'[a-zA-Z0-9]{6}@123.con','abc124@123.con')
print ma3.group()

ma4 = re.match(r'[a-z0-9]{4}','aacc987')
print ma4.group()

