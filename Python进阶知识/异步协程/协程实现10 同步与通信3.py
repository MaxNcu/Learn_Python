import asyncio
from asyncio import Queue
import random
import string
q = Queue(maxsize=100)

async def add():
    while 1:
        await q.put(random.choice(string.ascii_letters))

async def desc():
    while 1:
        res = await q.get()
        print(res)
        await asyncio.sleep(1)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([add(),desc()]))
    loop.run_forever()