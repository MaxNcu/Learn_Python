# -*- coding:utf-8 -*-
import multiprocessing
import random


result = set()

def rand(x, y):
    return str(random.randint(x, y))

def go(q):
    A = rand(1,254)
    if A == '127':
        A = rand(129,254)
        if A == '192':
            A = rand(1, 125)

    res = A + '.' + rand(1, 254) + '.' + rand(1, 254) + '.' + rand(1, 254)
    q.append(res)

if __name__ == '__main__':
    q = multiprocessing.Manager().list()
    New_start = input('输入生成IP总数:')
    for n in range(int(New_start)):
        p = multiprocessing.Process(target=go,args=(q,))
        p.start()
        p.join()

    print(q)

