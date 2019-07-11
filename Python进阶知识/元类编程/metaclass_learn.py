# -*- coding:utf-8 -*-

class magic(object):
    def __init__(self):
        self.name = '浪子'
    def say(self):
        return '浪子66666666'
m = magic()
print(m.name)
print(m.say())
print(m)
print('*'*50)



def say(*args):
    return '浪子66666666'
magic = type('随便起个名',(object,),{'name':'浪子','say':say})
m = magic()
print(m.name)
print(m.say())
print(m)