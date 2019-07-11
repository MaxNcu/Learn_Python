# -*- coding:utf-8 -*-
import asyncio
import aiomultiprocess
import aiohttp

async def get_url_info(url):
    # 这一部分就是发起网络请求，没有aiomultiprocess的参与
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.read()

async def main():
    # main()函数是核心函数，负责给每个CPU提供任务
    tasks = ['http://www.langzi.fun' for i in range(10)]
    # 10个网址保存到列表

    async with aiomultiprocess.Pool() as pool:
        # 开启进程池
        result = await pool.map(get_url_info,tasks)
        # 这里必须要await，使用pool.map()方法
    print(result)
    # 返回的结果是一个列表


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # 如果是python3.7的话，就直接使用asyncio.run(mian())即可