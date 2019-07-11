import asyncio


async def consumer(cond, name, second):
    # 消费者函数
    await asyncio.sleep(second)
    # 等待延迟
    with await cond:
        await cond.wait()
        print('{}: 得到响应'.format(name))


async def producer(cond):
    await asyncio.sleep(2)
    for n in range(1, 3):
        with await cond:
            print('生产者 {} 号'.format(n))
            cond.notify(n=n) # 挨个通知单个消费者
        await asyncio.sleep(0.1)


async def producer2(cond):
    await asyncio.sleep(2)
    with await cond:
        print('释放信号量，通知所有消费者')
        cond.notify_all()
        # 一次性通知全部的消费者


async def main(loop):
    condition = asyncio.Condition()
    # 设置信号量
    task = loop.create_task(producer(condition))
    # producer 和 producer2 是两个协程, 不能使用 call_later(), 需要用到 create_task() 把它们创建成一个 task
    consumers = [consumer(condition, name, index) for index, name in enumerate(('c1', 'c2'))]
    await asyncio.wait(consumers)
    task.cancel()
    print('---分割线---')
    task = loop.create_task(producer2(condition))
    consumers = [consumer(condition, name, index) for index, name in enumerate(('c1', 'c2'))]
    await asyncio.wait(consumers)
    task.cancel()
    # 取消任务


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()