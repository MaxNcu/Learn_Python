# -*- coding:utf-8 -*-

class magic:
    a = 'langzi'
    def __init__(self,x):
        self.x = x
        # 这里传入的x已经属于这个对象

    def run(self):
        return self.x

m = magic('xx')
m.a = 'LANGZILANGZI'
print(m.a)
# 查找实例的属性
print(magic.a)
# 查找类的属性

print(m.x)