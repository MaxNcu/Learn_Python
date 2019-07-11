# -*- coding:utf-8 -*-

a = [1,2,3]
print(type(a))
b = iter(a)
print(type(b))
# for x in b:
#     print(x)
print(next(b))
print(next(b))
print(next(b))
