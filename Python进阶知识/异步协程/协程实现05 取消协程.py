# -*- coding:utf-8 -*-
import time
import asyncio
async def get_time_sleep(t):
    print('开始运行，等待:{}s'.format(t))
    await asyncio.sleep(t)
    print('运行结束')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # 创建一个事件循环
    task_1 = get_time_sleep(1)
    task_2 = get_time_sleep(2)
    task_3 = get_time_sleep(3)

    tasks = [task_1,task_2,task_3]
    # 三个协程任务加载到一个列表

    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt:
        # 当检测到键盘输入 ctrl c的时候
        all_tasks = asyncio.Task.all_tasks()
        # 获取注册到loop下的所有task
        for task in all_tasks:
            print('开始取消协程')
            task.cancel()
            # 取消该协程,如果取消成功则返回True
        loop.stop()
        loop.run_forever()
        # 这两步必须要做
    finally:
        loop.close()

