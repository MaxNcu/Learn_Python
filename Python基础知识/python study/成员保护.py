# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 0008 11:41
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 成员保护.py
# @Software: PyCharm
import sys
import time
import random
reload(sys)
sys.setdefaultencoding('utf-8')

class obj:
    def __init__(self,name):
        self.name=name
    def prin(self):
        print self.name
    __age = 18
    # 加上双下划线的就是私有变量，只能在类的内部访问，外部无法访问
    @classmethod
    # 如果要在类中调用，首先调用类方法
    def pri(cls):
        print cls.__age
        # 然后在使用
    @classmethod
    def set_age(cls,value):
        cls.__age = value
        return cls.__age
        # 这个用法就是改变__age的值
    @classmethod
    def get_age(cls):
        return cls.__age
        # 这个用法就是直接返回__age的值
    @classmethod
    def del_age(cls):
        del cls.__age
        # 这个用法就是直接删除__age的值
time.sleep(random.choice([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.5,2.3]))
print obj.get_age()
# 这里是直接调用出__age的值  返回值18
print obj.set_age(20)
# 这里是直接改变__age的值  返回值20
obj.del_age()
# 这里是直接删除__age的值
