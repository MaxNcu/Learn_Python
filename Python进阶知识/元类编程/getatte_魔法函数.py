# -*- coding:utf-8 -*-

class magic:
    def __init__(self,info):
        self.info = info
    def __new__(cls, user):
        cls.user = user
        return object.__new__(cls)
    def __getattribute__(self, item):
        return '你想让我干啥子嘛'

a = magic({'user':'浪子','age':18})
print(a.user)
print(a.ageafa)
print(a.ag124125ad)
print(a.info)
