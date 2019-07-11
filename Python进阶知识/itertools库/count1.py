# -*- coding:utf-8 -*-
import time
import itertools
a = itertools.count(10,-1)
for x in a:
    print(x)
    time.sleep(0.2)