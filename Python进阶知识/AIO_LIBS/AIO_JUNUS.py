# -*- coding:utf-8 -*-
import asyncio
import janus
loop = asyncio.get_event_loop()
queue = janus.Queue(loop=loop)
# queue队列可以设置异步队列和同步队列
# queue.async_q:异步
# queue.sync_q:同步

def threaded(sync_q):
    # 这个函数接受的是同步的队列
    for i in range(10):
        sync_q.put(i)
        # 队列放入数据
    sync_q.join()
    # 等待所有数据存放完毕


async def async_coro(async_q):
    for i in range(10):
        val = await async_q.get()
        print(val)
        # assert val == i
        # 等同于 if val == i:
        if val == i:
            async_q.task_done()


fut = loop.run_in_executor(None, threaded, queue.sync_q)
# 该方法是把阻塞的队列注册加载到loop中，等待完成
loop.run_until_complete(async_coro(queue.async_q))
# 执行async_coro()函数，传入的参数是 queue.async_q (queue队列的异步队列)
loop.run_until_complete(fut)
# 这行代码不要也行