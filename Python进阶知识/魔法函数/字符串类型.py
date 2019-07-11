# -*- coding:utf-8 -*-

class magic:
    def __init__(self,num):
        self.num = num

    def __repr__(self):
        return (self.num + '\n')*5

a = magic('浪子好帅啊')

b = a
print type(b)