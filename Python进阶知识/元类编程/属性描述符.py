# -*- coding:utf-8 -*-
class magic:
    def __init__(self):
        self.user = '浪子'
    def __get__(self, instance, owner):
        # 用于访问属性。它返回属性的值，或者在所请求的属性不存在的情况下出现 AttributeError 异常。
        print('正在进行【获取】属性，内容为:{}'.format(owner))
        return self.user + '真帅'
    def __set__(self, instance, value):
        # 将在属性分配操作中调用。不会返回任何内容。
        print('正在进行【设置】属性，内容为:{}'.format(value))
        self.user = value
    def __delete__(self, instance):
        # 控制删除操作。不会返回内容。
        print('正在进行【删除】属性')
        del self.user
    # tips:需要注意，描述符被分配给一个类，而不是实例。修改此类，会覆盖或删除描述符本身，而不是触发它的代码。

class person:
    person = magic()

user = person()
print(user.person)
print('*'*25)
user.person = '小桃红'
print('*'*25)
print(user.person)
print('*'*25)
del user.person