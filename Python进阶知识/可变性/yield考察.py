# -*- coding:utf-8 -*-
import time
def fib(n):
    a,b = 0,1
    while b<n:
        a,b = b,a+b
        yield b
for x in fib(10):
    print(x)
# def test1():
#     while 1:
#
#         print('开始运行')
#         yield None
#         time.sleep(1)
# def test2(t):
#     next(t)
#     while 1:
#         t.send(None)
#         print('我也开始运行')
#         time.sleep(1)
#
#     #t.close()
#
# t = test1()
# test2(t)