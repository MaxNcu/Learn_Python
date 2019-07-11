# -*- coding:utf-8 -*-
class magic:
    def __init__(self,num):
        self.num = num

    def __iter__(self):
        # 使用__iter__，magic类为可迭代对象
        return self

    def __next__(self):
        # __next__魔法函数的作用是在循环的时候，无限提供输出下一个值，直到没有数据后抛出异常
        if self.num >5:
            # 设置上限
            raise StopIteration
        else:
            self.num += 1
            return self.num

a = magic(-5)
print(a.__next__())
print(next(a))
