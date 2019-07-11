# -*- coding:utf-8 -*-
class magic:
    def __init__(self):
        self.user = '浪子'
    def fget(self):
        print('正在进行【获取】属性，内容为:{}'.format(self.user))
        return self.user + '真帅'
    def fset(self,value):
        print('正在进行【设置】属性，内容为:{}'.format(value))
        self.user = value
    def fdel(self):
        print('正在进行【删除】属性')
        del self.user
    name = property(fget, fset, fdel)

user = magic()
print(user.user)
print('-------------------')
print(user.name)
print('-------------------')
user.name = '小桃红'
print('-------------------')
print(user.user)
print(user.name)