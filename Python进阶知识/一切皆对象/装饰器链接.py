# -*- coding:utf-8 -*-

def outer(func):
    def inter(x):
        if 'gov' in x:
            return None
        result = func(x)
        return result
    return inter

@outer
def run(x):
    print(x)

run('gov')
