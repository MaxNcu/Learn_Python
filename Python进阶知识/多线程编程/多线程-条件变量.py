# -*- coding:utf-8 -*-
import threading
import time
con1 = threading.Condition()
con2 = threading.Condition()
def run():
    while 1:
        con1.acquire()
        print('-----------------')
        print('我完事了，该你们了')
        con1.notify()
        con1.wait()
        con1.release()
        con2.acquire()
        print('--')
        con1.notify()
        con1.wait()
        con2.release()

def middle():
    while 1:
        with con2:
            con2.wait()
            time.sleep(0.5)
            print('五秒后....')
            print('我不行了，你们继续')
            con2.notify()

def result():
    while 1:
        with con1:
            con1.wait()
            time.sleep(0.3)
            print('三秒后....')
            print('我也完事了，你们加油')
            con1.notify()

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=middle)
t3 = threading.Thread(target=result)

