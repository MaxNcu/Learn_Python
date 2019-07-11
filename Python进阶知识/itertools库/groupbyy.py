# -*- coding:utf-8 -*-
import itertools
a = itertools.groupby([1,0,2,3,4,5,6],lambda x:x>5)
for x,y in a:
	print(x,'::::',list(y))