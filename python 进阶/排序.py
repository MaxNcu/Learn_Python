# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 0025 14:39
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 排序.py
# @Software: PyCharm
import sys
import bisect
import random
reload(sys)
sys.setdefaultencoding('utf-8')

arr = [random.randint(1,20)for _ in range(20)]
# def insertionSort(arr):
#     for i in range(len(arr)):
#         preIndex = i-1
#         current = arr[i]
#         while preIndex >= 0 and arr[preIndex] > current:
#             arr[preIndex+1] = arr[preIndex]
#             preIndex-=1
#         arr[preIndex+1] = current
#     return arr
# for x in insertionSort(arr):print x
# arr = [random.randint(1,20)for _ in range(20)]
# x=10
# ret=bisect.bisect(arr,x)
# ## 打印x在列表中排第几
# print ret
#
# def binarySearch3(lst,x):
#     i = bisect.bisect_left(lst,x)
#     if i != len(lst) and lst[i] == x:
#         return i
#     raise ValueError
# print binarySearch3(arr,x)
def insort(a,x,lo=0,hi=None):
    if lo <0:
        raise ValueError
    if hi is None:
        hi=len(a)
    while lo<hi:
        mid = (lo+hi)//2
        if x <a[mid]:hi=mid
        else:lo=mid+1
    a.insert(lo,x)
arr = [1,5,6,4,2]
x=5
insort(arr,x)
print arr