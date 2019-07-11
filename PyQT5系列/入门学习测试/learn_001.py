# -*- coding:utf-8 -*-
from functools import wraps

def outer(func):
    def inner(a):
        if a:
            print(a)
        result = func(a)
        print('over')
        return result
    return inner


@outer
def run(a):
    print('666')
    print(a)

run('777')