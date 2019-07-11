# -*- coding:utf-8 -*-

class A:
    def __init__(self,name):
        self.name = name
    def run(self):
        print(self.name+'6666666')

class B(A):
    def __init__(self,name):
        self.name = name
    def run(self):
        print(self.name+'7777777')
        #super().run()

c = B('浪子')
c.run()

