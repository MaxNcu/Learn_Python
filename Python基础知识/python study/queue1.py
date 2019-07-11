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
import Queue
reload(sys)
sys.setdefaultencoding('utf-8')

list1=[1,2,3,4,5,6,7,8,9]
q=Queue.Queue(maxsize=5)   #正序
q1 = Queue.LifoQueue()  #倒序
q3 = Queue.PriorityQueue(5)

for x in list1:
    q.put(x)
    while not q.empty():
        print q.get(x)
        #q.task_done()
        q.join()
        q.task_done()


# while 1:
#     print q.get(x)
#     print '\n'
#     print q1.get(x)
