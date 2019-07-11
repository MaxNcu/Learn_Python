# -*- coding:utf-8 -*-
import asyncio
import functools


def unlock(lock):
    print('线程锁释放成功')
    lock.release()


async def test(locker, lock):
    print(f'{locker} 等待线程锁释放')
    # ---------------------------------
    # with await lock:
    #     print(f'{locker} 线程锁上锁')
    # ---------------------------------
    # 上面这两行代码等同于：
    # ---------------------------------
    # await lock.acquire()
    # print(f'{locker} 线程锁上锁')
    # lock.release()
    # ---------------------------------
    await lock.acquire()
    print(f'{locker} 线程锁上锁')
    lock.release()
    print(f'{locker} 线程锁释放')


async def main(loop):
    lock = asyncio.Lock()
    await lock.acquire()
    loop.call_later(0.5, functools.partial(unlock, lock))
    # call_later() 表达推迟一段时间的回调, 第一个参数是以秒为单位的延迟, 第二个参数是回调函数
    await asyncio.wait([test('任务 1 ', lock), test('任务 2', lock)])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()