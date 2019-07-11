# -*- coding: utf-8 -*-
"""
__author__ = 'Langziyanqin'
__QQ__ = '982722261'
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
'''
.           匹配任意字符
[...]       匹配字符集
\d          匹配数字
\s          匹配字母
\D   \S     匹配和上面的相反
\w          匹配 a-z A-Z 0-9

'''
a = '0123.qwertyuiopkljhgfdsazxcvbnmASDATGGBVXCVCRTIEUDCNKLabcdgded'
ma1 = re.search('.*',a)
print ma1.group()
ma2 = re.search('\d+',a)
print ma2.group()
ma3 = re.search('[a-z|\d]*?',a)
print ma3.group()

ma4 = re.findall('[0-9]',a)
#for x in ma4:print x
