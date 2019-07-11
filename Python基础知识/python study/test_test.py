# -*- coding: utf-8 -*-
# @Time    : 2018/6/23 0023 10:35
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : test_test.py
# @Software: PyCharm
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import time

def consumer():
    while True:
        n = yield 'TEST_1'
        if not n:
            return
        print('first fun is : %s...' % n)


def produce(c):
    c.next()
    while 1:
        print('secend fun is run...')
        r = c.send('over')
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__=='__main__':
    c = consumer()
    produce(c)