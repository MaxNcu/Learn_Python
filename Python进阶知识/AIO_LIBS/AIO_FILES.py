# -*- coding:utf-8 -*-
import asyncio
import aiofiles

async def read_data():
    async with aiofiles.open('example.txt',mode='r',encoding='utf-8')as f:
        content = await f.readline()
        print(content)
loop = asyncio.get_event_loop()
loop.run_until_complete(read_data())