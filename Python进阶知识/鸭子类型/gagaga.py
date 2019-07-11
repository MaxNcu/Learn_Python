# -*- coding:utf-8 -*-
class magic:
    def __init__(self,num):
        self.num = num
    def __getitem__(self, item):
        return self.num[item]

a = magic([1,2,3,4,5])
b = [666]
b.extend(a)
for x in b:
    print(x)
