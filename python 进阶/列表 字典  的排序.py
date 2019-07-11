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
from random import randint
reload(sys)
sys.setdefaultencoding('utf-8')

list_ = [randint(0,20) for _ in range(10)]
print [x for x in list_ if x >10]

dic = {v:randint(1,10) for v in range(5)}
print {v:k for v,k in dic.iteritems() if k >2}

#字典中比较大小
dict = {i:randint(1,10) for i in range(10)}
print dict
print dict.iteritems()
print dict.has_key(2)
