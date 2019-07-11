# -*- coding:utf-8 -*-
import time
import asyncio
async def sum_tion(x,y)->int:
    print('开始执行传入参数相加:{} + {}'.format(x,y))
    await asyncio.sleep(1)
    # 模拟等待1S
    return (x+y)

async def print_sum(x,y):
    result = await sum_tion(x,y)
    return result

def callback(future):
    return future.result()

if __name__ == '__main__':
    t1 = time.time()
    loop = asyncio.get_event_loop()

    future = loop.create_task(print_sum(100,200))
    # 如果想要获取嵌套协程返回的值，就必须使用回调

    future.add_done_callback(callback)
    loop.run_until_complete(future)

    print(future.result())

    loop.close()
    print(time.time()-t1)