# -*- coding:utf-8 -*-
import itertools
a = itertools.compress([1,2,3,4,5],(0,0,0,1,1))
print(list(a))

b = itertools.compress([1,2,3,4,5],(True,True,False,False,False))
print(list(b))