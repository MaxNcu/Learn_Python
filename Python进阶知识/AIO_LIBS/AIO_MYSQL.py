# import asyncio
# from aiomysql import create_pool
# loop = asyncio.get_event_loop()
# async def go():
#     async with create_pool(host='127.0.0.1', port=3306,
#                            user='root', password='root',
#                            db='mysql', loop=loop) as pool:
#
#         async with pool.get() as conn:
#             async with conn.cursor() as cur:
#                 await cur.execute("show databases;")
#                 value = await cur.fetchall()
#                 print(value)
# loop.run_until_complete(go())


import asyncio
import aiomysql

async def test_example(loop):
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='root',
                                      db='mysql', loop=loop)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("show databases;")
            print(cur.description)
            r = await cur.fetchone()
            print (r)
    pool.close()
    await pool.wait_closed()

loop = asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))


