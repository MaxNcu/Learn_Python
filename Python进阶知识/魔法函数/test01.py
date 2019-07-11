# -*- coding:utf-8 -*-

class magic:
    def __init__(self,num):
        self.num = num

    def __getitem__(self, item):
        return self.num[item]

a = magic(['1','2','3'])
for x in a:
    print x