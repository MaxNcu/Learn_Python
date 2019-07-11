# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 0018 14:11
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 判断字符串的开头与结尾.py
# @Software: PyCharm
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
data_str='langzi'
if data_str.startswith('l'):
    print True
if data_str.endswith('i'):
    print True
#可以接受也只能接受元祖，只要其中一个是真的即可
if data_str.endswith(('l','2','i')):
    print True
for x in os.listdir('.'):
    print x.decode('gbk').encode('utf-8')
    # 解决中文乱码

for x in  [name.decode('gbk').encode('utf-8') for name in os.listdir('.') if name.endswith('.py')]:print x




