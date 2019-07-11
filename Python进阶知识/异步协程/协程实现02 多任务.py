# -*- coding:utf-8 -*-
import asyncio
import time

async def get_url_title(url):
    print('开始访问网站:{}'.format(url))
    await asyncio.sleep(2)
    print('网站访问成功')

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # 创造一个事件循环
    tasks = [get_url_title('http://www.langzi.fun')for i in range(10)]
    # 这个列表代表总任务量，即执行10次get_url_title()函数
    loop.run_until_complete(asyncio.wait(tasks))
    # asyncio.wait后面接上非空可迭代对象,一般来说是功能函数列表
    '''
    查看源码
    @coroutine
    def wait(fs, *, loop=None, timeout=None, return_when=ALL_COMPLETED)
    可以设置超时，以及何时返回,返回的是一个future对象，这个future对象中有两个值 done和pending
    (done, pending) = yield from asyncio.wait(fs)
    '''
    # 这里会等到全部的任务执行完后才会执行后面的代码
    end_time = time.time()
    print('消耗时间:{}'.format(end_time-start_time))
