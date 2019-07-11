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
import Queue
q = Queue.Queue()
import sys
import threading
import time
reload(sys)
sys.setdefaultencoding('utf-8')

def loop():
    l.acquire()
    # 这里相当于把线程加了锁，目前只允许这一个线程运行
    #定义一个要循环的函数，当然后面肯定会定义好几个函数
    print 'thread %s is running...' % threading.current_thread().name
    #threading.current_thread().name就是当前线程的名字  在声明线程的时候可以自定义子线程的名字
    n = 0
    while n < 10:
        n = n + 1
        print '%s >>> %s' % (threading.current_thread().name, n)
        #输出当前线程名字  和循环的参数n
    print 'thread %s ended.' % threading.current_thread().name
    l.release()
    # 这里是把线程锁解开，可以再运行写一个线程
print 'thread %s is running...' % threading.current_thread().name

#下面的一部分就是threading的核心用法
#包括target name args 之类的 一般我只用targer=你定义的函数名
t = threading.Thread(target=loop, name='线程名:')
l = threading.Lock()
# 这里申明一个线程锁
t.start()
#开始
t.join()
#关于join的相关信息我会在后面的代码详说
print 'thread %s ended.' % threading.current_thread().name
