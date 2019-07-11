# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 0016 9:40
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 按照字典的值排序.py
# @Software: PyCharm
import sys
import random
reload(sys)
sys.setdefaultencoding('utf-8')
# 字典的键
data_str=['xie','zhao','chen']
# 生成字典
data_dic={k:random.randint(61,80) for k in data_str}
from collections import OrderedDict
data_dic = OrderedDict()
# 生成字典
data_dic={k:random.randint(61,80) for k in data_str}
for x in data_dic:print x
print sorted(zip(data_dic.values(),data_dic.keys()))

print sorted(data_dic.items(),key=lambda x:x[1])
