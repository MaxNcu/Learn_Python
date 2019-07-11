# -*- coding:utf-8 -*-
import asyncio
import time

async def get_url_title(url):
    print('开始访问网站:{}'.format(url))
    await asyncio.sleep(2)
    # 这一步至关重要
    # asyncio.sleep(2) 功能:异步非阻塞等待2s，作用是模拟访问网站消耗的事件
    # await 的作用类似 yield，即这个时候把线程资源控制权交出去,监听这个描述符直到这个任务完成
    # await 后面只能接三种类型
    '''
    1. 协程:Python 协程属于 可等待 对象，因此可以在其他协程中被等待:
    2. 任务:任务 被用来设置日程以便 并发 执行协程。(当一个协程通过 asyncio.create_task() 等函数被打包为一个 任务，该协程将自动排入日程准备立即运行)
    3. Future 对象:Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果。(当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。)
    
    如果await time.sleep(2) 是会报错的
    '''
    print('网站访问成功')

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # 一行代码创造事件循环
    loop.run_until_complete(get_url_title('http://www.langzi.fun'))
    # 这是一个阻塞的方法,可以理解成多线程中的join方法
    # 直到get_url_title('http://www.langzi.fun')完成后，才会继续执行下面的代码
    end_time = time.time()
    print('消耗时间:{}'.format(end_time-start_time))

