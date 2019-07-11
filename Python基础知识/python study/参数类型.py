# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 0016 10:46
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 参数类型.py
# @Software: PyCharm
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 参数类型
# 位置参数，必传参数，顺序参数
def test(a=[]):
    a.append('A')
    print id(a)
    return a
print test()
print test()
print test()

def test_new(a=None):
    if a is None:
        a=[]
    a.append('A')
    print id(a)
    return a
print test_new()
print test_new()
print test_new()

def fun(*args):
    for x in args:
        print x
fun(1,2,3)
li=[1,2,3,4,5]
fun(li)
fun(*li)

def fun_test(**kwargs):
    for x in kwargs:
        print x,kwargs[x]

fun_test(k1=1,k2=[1,2,3])
