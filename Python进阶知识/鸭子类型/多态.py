# -*- coding:utf-8 -*-

class dog:
    def gaga():
        print('汪汪汪汪汪~')
class cat:
    def gaga():
        print('喵喵喵喵喵喵喵~')
def you_say(you):
    you.gaga()
    you.gaga()
you_say(dog)
print('-'*10)
you_say(cat)