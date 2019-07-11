# -*- coding: utf-8 -*-
# @Time    : 2018/4/30 0030 20:58
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 多线程.py
# @Software: PyCharm
import sys
import threading
import time
reload(sys)
sys.setdefaultencoding('utf-8')

def fun(key):
    print key
    print threading.current_thread
    time.sleep(2)
t1 = threading.Thread(target=fun,args=(1,))
t1.start()