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
from itertools import chain
from random import randint
reload(sys)
sys.setdefaultencoding('utf-8')


#统计语文数学英语的总成绩
c = [randint(10,100) for _ in range(10)]
m = [randint(10,100) for _ in range(10)]
e = [randint(10,100) for _ in range(10)]
# for cc,mm,ee in zip(c,m,e):
#     t = int(cc) + int(mm) + int(ee)
#     print cc,mm,ee
#     print 'SCORE:' + str(t)





#统计4个班里面成绩高于90分的人数
#   （）串行
# c = [randint(10,100) for _ in range(10)]
# m = [randint(10,100) for _ in range(10)]
# e = [randint(10,100) for _ in range(10)]
# for x in chain(['A','B','C'],[1,2,3]):print x
# for x,v in enumerate(c):print x,v
#
# count = 0
# for x in chain(c,m,e):  #其中cme的人数不一致也可以用
#     if x >60:
#         count +=1
# print count

c = [randint(10, 100) for _ in range(10)]
for i in range(len(c)):
    print i,c[i]