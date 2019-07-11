# -*- coding:utf-8 -*-
from concurrent.futures import ThreadPoolExecutor,wait
import time
t1 = time.time()
def task(i):
    return i**2

p = ThreadPoolExecutor(100)

res = p.map(task,range(100000))
# with ThreadPoolExecutor() as p:   #类似打开文件,可省去.shutdown()
#     future_tasks = [p.submit(task, i) for i in range(100000)]
# print('=' * 30)
# print([obj.result() for obj in future_tasks])
print(list(res))
t2 = time.time()

print(t2-t1)