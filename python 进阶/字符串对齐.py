# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 0017 18:13
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 字符串对齐.py
# @Software: PyCharm
import sys
import random
reload(sys)
sys.setdefaultencoding('utf-8')

data_text='langzi'
print data_text.ljust(20,'-')
print data_text.rjust(20,'-')
print data_text.center(20,'-')
li1=['A','B','C','D']
#注意必须要是字符串，不能是数字类型
for x in li1:
    print x.center(20,'-')

print format(data_text,'^20')
#<20左对齐20个长度，>右对齐，^居中对齐

data_dic={k:random.randint(1,20) for k in ('xiaotaohong','chenyanqin','zhaotiaogeng')}
for k,v in data_dic.iteritems():
    print k.ljust(20) + ' : ' + str(v)