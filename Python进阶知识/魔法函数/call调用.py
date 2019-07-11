# -*- coding:utf-8 -*-
class A(object):
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
    def myprint(self):
        print('a=', self.__a, 'b=', self.__b)
    def __call__(self, *args, **kwargs):
        print(args)


a1=A(10,20)
a1.myprint()

a1(80)
# class ao:
#     def __init__(self,name):
#         self.name =name
#
#     def __call__(self, money):
#         return self.name + '大老板买了一个馒头~~花了%s元~~让我们感谢这位老铁~~'%money
#
# a = ao('小桃红')
# print(a(15))
# b = ao('猫饼饼')
# print(b(666))