# -*- coding:utf-8 -*-



# class MyMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         # 这里必须有4个参数
#         print('传入的类:'+name)
#         print('传入的类继承的父类:'+str(bases))
#         print('传入类的属性:'+str(attrs))
#         attrs['user'] = "浪子"
#         # 传入类的属性中 新加一个user
#         return super().__new__(cls, name, bases, attrs)

class MyMetaclass(type):
    def __init__(cls, nameee, basesss, attrs):
        cls.user = '浪子'
        print(basesss)
        super().__init__(nameee, basesss, attrs)
class Foo(object,metaclass=MyMetaclass):
    pass

foo = Foo()
print(foo.user)