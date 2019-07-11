# -*- coding:utf-8 -*-
# def gen(index):
#     if index<5:
#         yield index
#     else:
#         index+=1
# for x in gen(1):
#     print(x)
import dis
def gen():
    yield 1
    yield 2
    return 666

g = gen()
# g是生成器对象
print(dis.dis(g))
print('*'*10)
print(g.gi_frame.f_lasti)
# 这里还没有执行，返回的位置是-1
print(g.gi_frame.f_locals)
# 这里还没有执行，返回的对象是{}
next(g)
print('*'*10)
print(g.gi_frame.f_lasti)
print(g.gi_frame.f_locals)
next(g)
print('*'*10)
print(g.gi_frame.f_lasti)
print(g.gi_frame.f_locals)