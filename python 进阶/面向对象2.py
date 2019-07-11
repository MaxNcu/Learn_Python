# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 0003 17:02
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 面向对象2.py
# @Software: PyCharm
import sys
import time
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

class cc:
    ccc = 'ccc'
    # cc就是类名 如果想要继承别的类 就class cc(threading) 意思就是从threading继承
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        # 定义构造的过程就是实例化
    def runx(self):
        print self.a*10
        print self.b*5
        print self.c*2
    def runy(self):
        print requests.get('http://www.langzi.fun').headers
e = cc('AAA','CCC','EEE')
e.runx()
e.runy()
# 这两个就是调用类里面的方法
print e.c
#实例变量指的是实例本身拥有的变量。每个实例的变量在内存中都不一样。
print e.ccc
#类变量，在类里面找到定义的变量。