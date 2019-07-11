# -*- coding:utf-8 -*-
import itertools

zz = itertools.filterfalse(lambda a:a<5,range(10))
print(list(zz))

