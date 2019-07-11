# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 0018 21:12
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 递归函数.py
# @Software: PyCharm
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 函数自己调用自己
# def sum(munber):
#     total=0
#     for i in range(1,munber+1):
#         total+=i
#     return total
# print sum(100)

def sum_number(number):
    if number==0:
        return False
    return sum_number(number-1)+number
    # 第一次是sum_number(99)+100的值
    # 第二次是sum_number(98)+99的值
    # 最后一个是sum_number(0)
print sum_number(100)
print sum(range(10))

res = [lambda x:x+i for i in range(10)]
# lambda x:x+i,
print res[0](10)
