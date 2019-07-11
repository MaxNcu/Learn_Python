# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 0017 15:56
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 生成器.py
# @Software: PyCharm
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Sushu:
    def __init__(self,start,end):
        # 构造器，维护传入的初始值与最终值
        self.start=start
        self.end=end
    def issushu(self,k):
        # 接受传入的k值
        if k<2:
            # k值必须大于2
            return False
        for x in range(2,k):
            if k%x == 0:
                return False
            else:
                return True
            # 只有确认k是素数的时候返回正确
    def __iter__(self):
        #在Python中加双下划线的方法基本上都是对Python默认行为的重载。所以都会有对应的函数，或者Python内部来调用。在这里，__iter__是iter内建函数。__next__是next内建函数。
        for k in range(self.start,self.end):
            if self.issushu(k):
                # 如果这个类中的issushu函数是存在或者正确的
                yield k


for x in Sushu(1,30):print x
