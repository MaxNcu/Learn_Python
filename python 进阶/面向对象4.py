# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 0003 17:21
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 面向对象4.py
# @Software: PyCharm
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
class ff:
    @staticmethod
    def runx():
        print requests.get('http://www.langzi.fun').status_code
ff.runx()
#这里就直接调用了类的变量，只在类中运行而不在实例中运行的方法

