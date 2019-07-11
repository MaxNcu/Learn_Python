# -*- coding:utf-8 -*-
import threading
import time
import threading
import time


def mop_floor():
    print('我要拖地了')
    time.sleep(1)
    print('地拖完了')


def heat_up_watrt():
    print('我要烧水了')
    time.sleep(6)
    print('水烧开了')

start_time = time.time()
t1 = threading.Thread(target=heat_up_watrt)
t2 = threading.Thread(target=mop_floor)
t1.run()
t2.run()
# 注意这里不能加上join()
end_time = time.time()
print('总共耗时:{}'.format(end_time - start_time))

# class mop_floor(threading.Thread):
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         print('我要拖地了')
#         time.sleep(1)
#         print('地拖完了')
#
# class heat_up_watrt(threading.Thread):
#     def __init__(self,name):
#         # 这里传入参数name，就是传入子线程名字
#         super().__init__(name=name)
#         # 记住这里的格式不能错
#
#     def run(self):
#         print('我要烧水了')
#         print(self.name)
#         print(threading.current_thread().name)
#         # 这两个都是打印出当前子线程的名字
#         time.sleep(6)
#         print('水烧开了')
#
# start_time = time.time()
# t1 = mop_floor()
# t2 = heat_up_watrt('***我是烧水员***')
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end_time = time.time()
# print('总共耗时:{}'.format(end_time-start_time))