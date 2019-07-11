# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 0003 17:27
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 面向对象5.py
# @Software: PyCharm
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
class gg:
    url = 0
    stat = 0
    # 因为使用classmethod后会传入新的变量，所以一开始是需要自己先定义类变量
    def __init__(self,url=0,stat=0):
    # 这里按照正常的定义构造函数
        self.url=url
        self.stat=stat
    @classmethod
    # 装饰器，立马执行下面的函数
    def split(cls,info):
        # 这个函数接受两个参数，默认的cls就是这个类的init函数，info就是外面传入进来的
        url,stat=map(str,info.split('-'))
        # 这里转换成了格式化的结构
        data = cls(url,stat)
        # 然后执行这个类第一个方法，这个类构造函数需要传入两个参数，于是就传入了两个参数
        return data
        # 这里就直接返回了函数结果
    def outer(self):
        print self.url
        print self.stat

r = gg.split(('langzi-200'))
r.outer()
# 这里是调用类方法，与调用实例方法一样
