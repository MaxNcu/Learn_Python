# -*- coding:utf-8 -*-
#import uvloop
#asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import requests
import asyncio
import time
import re

def get_url_title(url):
    # 功能是获取网址的标题
    r = requests.get(url)
    try:
        title = re.search('<title>(.*?)</title>',r.content.decode(),re.S|re.I).group(1)
    except Exception as e:
        title = e
    print(title)

if __name__ == '__main__':
    start_time = time.time()

    loop = asyncio.get_event_loop()
    # 创建一个事件循环
    p = ProcessPoolExecutor(5)
    # 创建一个线程池，开启5个线程
    tasks = [loop.run_in_executor(p,get_url_title,'http://www.langzi.fun')for i in range(10)]
    # 这一步很重要，使用loop.run_in_executor()函数:内部接受的是阻塞的线程池，执行的函数，传入的参数
    # 即对网站访问10次，使用线程池访问
    loop.run_until_complete(asyncio.wait(tasks))
    # 等待所有的任务完成
    print(time.time()-start_time)


