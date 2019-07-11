# -*- coding:utf-8 -*-
import threading
import time
import random

boys = ['此时一位捡瓶子的靓仔路过\n------------','此时一位没钱的网友路过\n------------','此时一位推着屎球的屎壳郎路过\n------------']
event = threading.Event()
def lighter():
    event.set()
    while 1:
        ti = (random.randint(1, 10))
        time.sleep(ti)
        print('等待 {} 秒后'.format(str(ti)))
        event.clear()
        time.sleep(ti)
        event.set()


def go(boy):
    while 1:
        if event.is_set():
            # 如果事件被设置
            print('在辽阔的街头')
            print(boy)
            time.sleep(random.randint(1, 5))
        else:
            print('在寂静的田野')
            print(boy)
            event.wait()
            print('突然，一辆火车驶过')
            time.sleep(5)

t1 = threading.Thread(target=lighter)
t1.start()

for boy in boys:
    t2 = threading.Thread(target=go,args=(boy,))
    t2.start()