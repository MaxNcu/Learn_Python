# -*- coding: utf-8 -*-
"""
__author__ = 'Langziyanqin'
__QQ__ = '982722261'
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import sys
import threading
import time
reload(sys)
sys.setdefaultencoding('utf-8')
l = threading.Lock()
t00 = time.time()
def cs1():
    l.acquire()
    time0 = time.time()
    for x in range(5):
        print str(x)
        print threading.current_thread().name
    l.release()


def cs2():
    l.acquire()
    for x in range(6,9):
        print x
        print threading.current_thread().name
    l.release()


threads=[]

t1 = threading.Thread(target=cs1)
t2 = threading.Thread(target=cs2)
threads.append(t1)
threads.append(t2)
for x in threads:
    x.start()
print 'use time{}'.format(time.time()-t00)