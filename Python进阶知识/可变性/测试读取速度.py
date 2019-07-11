# -*- coding:utf-8 -*-
import time
t1 = time.time()
x = [x for x in open('a.txt','r').readlines()]
for a in x:
    pass
t2 = time.time()
print(t2 - t1)