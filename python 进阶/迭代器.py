# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 0017 14:34
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 迭代器.py
# @Software: PyCharm
import sys
from collections import Iterable
reload(sys)
sys.setdefaultencoding('utf-8')

data_list=[1,2,3,4,5]
data_list=iter(data_list)
print next(data_list)
print next(data_list)
print next(data_list)