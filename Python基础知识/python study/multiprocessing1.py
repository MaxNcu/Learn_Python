# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 0003 8:58
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : multiprocessing1.py
# @Software: PyCharm
from multiprocessing.dummy import Pool as tp
def fun(i):
    print i+i+i+i

list_i=[range(100)]

px = tp(processes=8)
# 开启8个线程池
px.map(fun,list_i)
px.close()
px.join()