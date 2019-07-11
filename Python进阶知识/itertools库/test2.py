# -*- coding:utf-8 -*-
import itertools
# a = range(100)
# b = (itertools.accumulate(a))
# print(type(b))
# for x in b:
#     print(x)
a = range(10)
b = range(20)
c = itertools.chain(a,b)
print(list(c))