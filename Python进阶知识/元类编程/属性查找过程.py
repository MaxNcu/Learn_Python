# -*- coding:utf-8 -*-
class magic:
    # 定义一个属性描述符的类
    def __init__(self):
        self.user = '浪子'
    # 初始化，当前用户名为 浪子
    def __get__(self, instance, owner):
    # 属性描述符 之 【获取】
        return self.user
    # def __set__(self, instance, value):
    # # 属性描述符 之 【设置】
    #     self.user=value + '大帅哥'

import re
string = '12345.shdjdjdj.124876797'
result = re.findall('\d+',string)
print(result)

# class Person:
#     def __getattr__(self, item):
#         return ('不管你多牛逼，反正要调用老子')
#     person = magic()
#
# p = Person()
# print(p.personsssssss)
