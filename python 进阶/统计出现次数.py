# -*- coding: utf-8 -*-
# @Time    : 2018/4/15 0015 22:35
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 统计出现次数.py
# @Software: PyCharm
import sys
import random
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf-8')

## 生成列表，从1-20随机选择10个数字
data_list=[random.randint(1,20)for _ in range(10)]

## 选择生成的列表数字作为字典的键,0作为值
data_dic=dict.fromkeys(data_list,0)

## 统计次数
for x in data_list:
	data_dic[x]+=1
print data_dic

from collections import Counter  #专门处理字典中出现次数最duo
c2 = Counter(data_list)
print c2.most_common(6)  #三个出现次数最多
data='aaaaabbbbbcccccedg'
c3=Counter(data)
print c3.most_common(2)