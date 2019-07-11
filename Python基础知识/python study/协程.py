# -*- coding: utf-8 -*-
# @Time    : 2018/6/23 0023 10:19
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 协程.py
# @Software: PyCharm
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

def fun_1():
    while 1:
        yield 'FUN_1 执行完毕,切换到FUN_2'
        # 函数运行到yield会暂停函数执行，存储这个值。并且有next():调用这个值，与send():外部传入一个值
        time.sleep(1)
        print 'FUN_1 函数开始执行'

def fun_2(t):
    t.next()
    while 1:
        print '-'*20
        print 'FUN_2 函数开始执行'
        time.sleep(1)
        ret = t.send('over')
        print ret
    t.close()

if __name__ == '__main__':
    n = fun_1()
    fun_2(n)

