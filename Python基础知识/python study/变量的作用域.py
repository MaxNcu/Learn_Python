# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 0018 17:07
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 变量的作用域.py
# @Software: PyCharm
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

name = 'xiaotaohong'
def f2():
    name = 'langzi'
    return f1
def f1():
    print name
ret=f2()
ret()
