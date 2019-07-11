# -*- coding:utf-8 -*-
class magic:
    def __enter__(self):
        print('enter魔法函数执行')
        return 'enter魔法函数执行完毕'
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exti魔法函数执行')
        print(exc_type)
        return 'exit魔法函数执行完毕'

def ma():
    return magic()

with ma() as a:
    print('随便执行一些东西')