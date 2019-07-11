# -*- coding: utf-8 -*-

import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')
class obj:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        # 把这些设置成私有变量
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if isinstance(value,int):
            self.__age=value
        else:
            raise ValueError('非整数类型')
    @age.deleter
    def age(self):
        print 'delete over'
a = obj('langzi',18)
# 使用这些装饰器，可以使用类与对象的方法直接调用
print a.age
# 这里就是直接调用返回age的值
a.age=20
# 这里就是直接使用setter把值转换
print a.age
del a.age
# 删除age
# 方法调用伪装成属性使用。在Django源码中常常有这种方法使用。
