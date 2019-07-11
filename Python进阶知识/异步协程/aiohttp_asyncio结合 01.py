# -*- coding:utf-8 -*-
import asyncio
import aiohttp
import re

def encodings(content):
    charset_re = re.compile(b'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
    pragma_re = re.compile(b'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
    xml_re = re.compile(b'^<\?xml.*?encoding=["\']*(.+?)["\'>]')

    return (charset_re.findall(content) +
            pragma_re.findall(content) +
            xml_re.findall(content))


async def get_domain_info(url):
    async with asyncio.Semaphore(10000):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=20) as resp:
                result = (await resp.read())
                encoding = encodings(result)[0].decode()
                title = re.search('<title>(.*?)</title>',result.decode(encoding,'replace'),re.S|re.I).group(1)
                print(title)
                return title

if __name__ == '__main__':
    i = 0
    while 1:
        loop = asyncio.get_event_loop()

        tasks = [get_domain_info('http://www.langzi.fun') for _ in range(100)]
        loop.run_until_complete(asyncio.wait(tasks))

