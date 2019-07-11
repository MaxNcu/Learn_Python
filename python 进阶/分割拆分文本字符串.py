# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 0017 17:34
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 分割拆分文本字符串.py
# @Software: PyCharm
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

data_text='''
shuob1uShang，why，943586926isM1?
YEAH。SUre，iamis、now i am so boring
xian9zais--hi2018-4-17,wozai shang hai jiading
say so&^me ?d-o some23thi^&ngs only for what
zhaohan only 00-//for\\||you
ho[pe you\] zhao yi sun
we can 17
--*</html>
'''

#print data_text.split()
# 默认是按照空白，空格，\t,\r,\n来分割

res = data_text.split('^')
#print map(lambda x:x.split('-'),res)

print re.split('\d|]',data_text)

