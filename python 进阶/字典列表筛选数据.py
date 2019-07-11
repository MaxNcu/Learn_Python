# -*- coding: utf-8 -*-
# @Time    : 2018/4/15 0015 22:12
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 字典列表筛选数据.py
# @Software: PyCharm
import sys
import random
reload(sys)
sys.setdefaultencoding('utf-8')
# 生成列表，从1-100选择10个数字
data_list=[random.randint(1,100) for _ in range(10)]
# 生成字典，键为1-20，值为60-100
data_dict={k:random.randint(60,100) for k in range(1,21)}

# 使用Filter筛选
print (filter(lambda x:x>60,data_list))
# 使用列表推导
print [x for x in data_list if x>60]
# 字典筛选
print {k:v for k,v in data_dict.iteritems() if v>5}