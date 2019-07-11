# -*- coding:utf-8 -*-
import itertools
a = itertools.repeat(1,5)
print(list(a))
# a = itertools.islice([0,0,2,2,4,4,5,5],4)
# # 获取前4为，就是0，4
# print(list(a))
#
# a = itertools.islice([0,0,2,2,4,4,5,5],0,2)
# # 获取前2为，就是0，2
# print(list(a))
#
# a = itertools.islice([0,0,2,2,4,4,5,5],3,6)
# # 获取前3-6位
# print(list(a))
#
# a = itertools.islice([0,0,2,2,4,4,5,5],0,5,2)
# # 获取前0-5位，并且间隔位2
# print(list(a))