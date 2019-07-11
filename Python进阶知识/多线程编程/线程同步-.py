# -*- coding:utf-8 -*-
import threading
def run1():
    while 1:
        if l1.acquire():
            # 如果第一把锁上锁了
            print('我是老大，我先运行')
            l2.release()
            # 释放第二把锁
def run2():
    while 1:
        if l2.acquire():
            # 如果第二把锁上锁了
            print('我是老二，我第二运行')
            l3.release()
            # 释放第三把锁

def run3():
    while 1:
        if l3.acquire():
            # 如果第三把锁上锁了
            print('我是老三，我最后运行')
            l1.release()
            # 释放第一把锁


t1 = threading.Thread(target=run1)
t2 = threading.Thread(target=run2)
t3 = threading.Thread(target=run3)

l1 = threading.Lock()
l2 = threading.Lock()
l3 = threading.Lock()
# 实例化三把锁

l2.acquire()
l3.acquire()

t1.start()
t2.start()
t3.start()
