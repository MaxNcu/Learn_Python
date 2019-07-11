# -*- coding:utf-8 -*-
# import threading
# import random
# import queue
#
# q = queue.Queue(maxsize=1)
#
#
# def produce(q):
#     while 1:
#         result = str(random.randint(1, 100))
#         q.put(result)
#         print('我生成了一个随机数字:' + result)
#
#
# def consume(q):
#     while 1:
#         res = q.get()
#         print('我获取到了你生成的随机数字:' + str(res))
#
#
# t1 = threading.Thread(target=produce, args=(q,))
# t2 = threading.Thread(target=consume, args=(q,))
# t1.start()
# t2.start()
import time
import threading
import random

def produce():
    global q
    while 1:
        con.acquire()
        # 必须在有锁的前提下才能使用条件变量
        q = str(random.randint(1,100))
        print('我生成了一个随机数字:'+q)
        con.notify()
        # 发起一个信号，释放一个被堵塞的线程
        con.wait()
        # 发起一个信号，堵塞当前线程，等待另一个notify出现的时候就执行下面的代码
        con.release()
        # 必须要解锁
def consume():
    global q
    while 1:
        con.acquire()
        # 必须在有锁的前提下才能使用条件变量
        print('我获取到你生成的随机数字:'+q)
        con.notify()
        # 发起一个信号，释放一个被堵塞的线程
        con.wait()
        # 堵塞当前线程
        con.release()

t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)
con = threading.Condition()
t1.start()
t2.start()
