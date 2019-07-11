# -*- coding:utf-8 -*-
import random
import asyncio
from aiohttp import ClientSession


async def fetch(sem,url):
    async with sem:
        # 最大访问数
        async with ClientSession() as session:
            async with session.head(url) as response:
                    res = await response.text()
                    status = response.status
                    print("{}:{} ".format(response.url, status))
                    return res

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    url = "http://www.langzi.fun"
    sem = asyncio.Semaphore(1000)
    # 设置最大并发数为1000
    tasks = [loop.create_task(fetch(sem,url))for i in range(100)]
    # 对网站访问100次
    loop.run_until_complete(asyncio.wait(tasks))
