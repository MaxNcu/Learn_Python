# -*- coding:utf-8 -*-
import time
import asyncio

def callback(loop):
    print("传入loop.time()时间为: {} s".format(loop.time()))
def stoploop(loop):
    print('时间消耗完毕')
    loop.stop()


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()

    now = loop.time()
    # loop内部的时钟时间
    loop.call_at(now+1,callback,loop)
    # 等待loop内部时钟时间加上1s后，执行callba函数，传入参数为loop
    loop.call_at(now+3,callback,loop)
    # 等待loop内部时钟时间加上3s后，执行callba函数，传入参数为loop
    loop.call_at(now+5,stoploop,loop)
    # 等待loop内部时钟时间加上1s后，执行stoploop函数，传入参数为loop

    loop.run_forever()
    print('总共耗时:{}'.format(time.time()-start_time))

    # now = loop.time()
    # loop.call_later(5.5, callback, 5.5, loop)
    # #第一个参数设置的时间5.5秒后执行，
    # loop.call_at(now+2, callback, 2, loop)
    # #在指定的时间，运行，当前时间+2秒
    # loop.call_at(now+1, callback, 1, loop)
    # loop.call_at(now+3, callback, 3, loop)
    # #loop.call_soon_threadsafe(callback, 3, loop)   # 功能与call_soon类似，但这是线程安全的方法，变量在其他线程也会用到，这个时候就可以用这个方法
    # loop.call_soon(stoploop, loop)
    # # call_soon 立刻执行，并不是说到这行代码就马上执行。而是在队列里面，等到下一个循环时，立马执行
    # loop.call_soon(callback, 4, loop)
    # loop.run_forever()
    # #要用这个run_forever运行，因为没有传入协程
