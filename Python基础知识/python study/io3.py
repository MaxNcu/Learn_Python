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
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')

# f1 = open('io1.txt','a+')
# f1.write('你好')
# print f1.read()
# print f1.read().encode('utf-8')
# f1.close()




# f=codecs.open('io2.txt','r','utf-8')
# print f.encoding
# print f.name
# for x in f.readlines():
#     print x
# f.close()

import fileinput

with fileinput.input(files=('spam.txt', 'io2.txt')) as f:
    for line in f:
        print line