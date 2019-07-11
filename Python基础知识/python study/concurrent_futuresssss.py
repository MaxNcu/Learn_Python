# coding:utf-8
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# 导入线程池和进程池模块
import threading
# 导入线程模块，作用是获取当前线程的名称
import os,time

def task(n):
    print('%s:%s is running' %(threading.currentThread().getName(),os.getpid()))
    # 打印当前线程名和运行的id号码
    time.sleep(2)
    return n**2
    # 返回传入参数的二次幂

if __name__ == '__main__':
    p=ThreadPoolExecutor()
    #实例化线程池，设置线程池的数量，不填则默认为cpu的个数*5
    l=[]
    # 用来保存返回的数据，做计算总计
    for i in range(10):
        obj=p.submit(task,i)
        # 传入的参数是要执行的函数和该函数接受的参数
        l.append(obj)
        # 把返回的结果保存在空的列表中，做总计算
    p.shutdown()
    # 所有计划运行完毕，关闭结束线程池

    print('='*30)
    print([obj.result() for obj in l])

#上面方法也可写成下面的方法
    # with ThreadPoolExecutor() as p:   #类似打开文件,可省去.shutdown()
    #     future_tasks = [p.submit(task, i) for i in range(10)]
    # print('=' * 30)
    # print([obj.result() for obj in future_tasks])
