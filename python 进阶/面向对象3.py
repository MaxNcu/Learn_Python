# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 0003 17:16
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 面向对象3.py
# @Software: PyCharm
import sys
import time
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

class dd:
    def __init__(self,url):
        self.url=url
    def runx(self):
        print requests.get(self.url).status_code

a = dd('http://www.langzi.fun')
a.runx()
# 这种调用方法就是实例方法

