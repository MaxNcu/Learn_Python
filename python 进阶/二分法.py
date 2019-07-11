# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 0003 14:23
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 二分法.py
# @Software: PyCharm
import sys
import random
reload(sys)
sys.setdefaultencoding('utf-8')
def fun1(list_1,num):
    low,hight = 0,len(list_1)-1
    while low <= hight:
        mid = (low+hight)/2
        guess = list_1[mid]
        if guess == num:
            return mid
        if guess > num:
            hight = mid - 1
        else:
            low = mid + 1
    return None
list_1 = sorted([random.randint(1,20) for _ in range(10)])
print list_1
num = 5
print fun1(list_1,num)

