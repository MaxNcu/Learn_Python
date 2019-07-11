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

reload(sys)
sys.setdefaultencoding('utf-8')
class Diedai:
    def __init__(self,start,end,step=0.5):
        self.start=start
        self.end=end
        self.step=step
    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step
    def __reversed__(self):
        t = self.end
        while t >=self.start:
            yield t
            t -= self.step

for x in Diedai(1,10,0.5):print x
for x in reversed(Diedai(1,20,0.2)):print x