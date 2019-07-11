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
def f():
    print 'test1'
    yield 1
    print 'test2'
    yield 2
g = f()
#生成器对象是可迭代对象
#for x in g:print x
print g.next()

list1 = [x for x in range(20)]
print list1

#yield  返回的是生成器

def club(n):
    for x in range(n):
        yield x + 1

for i in club(4):
    print i
print '==========='

def fab(x):
    a,b,c = 0,0,1
    while a<x:
        print c
        b,c = c,b+c
        a +=1
#fab(10)

def fac(x):
    a,b,c = 0,0,1
    while a<x:
        yield c
        b,c=c,b+c
        a+=1
for x in fac(5):print x   #生成器对象可以迭代
print '-----------------'


class Sushu:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def issushu(self,k):
        print k
        if k < 2:
            return False
        for x in xrange(2,k):
            if k % x == 0:
                print x
                return False
        return True
    def __iter__(self):
        for k in range(self.start,self.end):
            if self.issushu(k):
                yield k

for i in Sushu(1,100):
    print i
