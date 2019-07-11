# -*- coding:utf-8 -*-
# class test:
#     pass
# print(type(test))
# print(type(test()))
#
# print(sum([1,2,3]))
# print(type(sum))

class test:
    def __init__(self):
        print(666)

class test1(test):
    # test1继承test
    pass

a = test1
# 实例化test1
print(a.__bases__)
# 获取a的父类
print(type(a()))
# 执行a，获取执行a后的基类

