# -*- coding:utf-8 -*-

class magic:
    '我是注释'
    user = '浪子'
    def run(age):
        print(age)

for x,y in magic.__dict__.items():
    print(x,':',y)
