# -*- coding:utf-8 -*-
from collections import Iterable,Iterator
# a = [1,2,3]
# a = iter(a)
# print(isinstance(a,Iterator))
# print(isinstance(a,Iterable))
# print(next(a))
# print('----')
# for x in a:
#     print(x)

class s:
    def __init__(self,x):
        self.x = x
        # 获取传入的对象
        self.index = 0
        # 维护索引值
    def __next__(self):
        try:
            result = self.x[self.index]
            # 获取传入对象的值
        except IndexError:
            # 如果索引值错误
            raise StopIteration
        # 抛出停止迭代
        self.index += 1
        # 索引值+1，用来获取传入对象的下一个值
        return result
        # 返回传入对象的值
    # def __iter__(self):
    #     return self
class b(s):
    def __init__(self,x):
        self.x = x
        self.index = 0
    def __iter__(self):
        return s(self.x)
a = b([1,2,3])
print(next(a))
print(next(a))

# a = s([1,2,3])
# print(next(a))
# print('----------')
# for x in a:
#     print(x)
