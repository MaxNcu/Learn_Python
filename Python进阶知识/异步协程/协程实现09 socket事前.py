# -*- coding:utf-8 -*-
import asyncio
from urllib.parse import urlparse
import time


async def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = '/'

    # 建立socket连接
    reader, writer = await asyncio.open_connection(host, 80)  # 协程 与服务端建立连接
    writer.write(
        "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))
    all_lines = []
    async for raw_line in reader:  # __aiter__ __anext__魔法方法
        line = raw_line.decode('utf8')
        all_lines.append(line)
    html = '\n'.join(all_lines)
    return html


async def main():
    tasks = []
    tasks = [asyncio.ensure_future(get_url('http://www.langzi.fun')) for i in range(10)]
    for task in asyncio.as_completed(tasks):  # 完成一个 print一个
        result = await task
        print(result)

# if __name__ == '__main__':
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     print('last time:{}'.format(time.time() - start_time))


import asyncio
from concurrent.futures import ThreadPoolExecutor
import socket
from urllib.parse import urlparse
import time
import re


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = '/'

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))
    client.send(
        "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))
    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode('utf8')
    html_data = data.split('\r\n\r\n')[1]
    # 把请求头信息去掉， 只要网页内容
    title = re.search('<title>(.*?)</title>',html_data,re.S|re.I).group(1)
    print(title)
    client.close()


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    p = ThreadPoolExecutor(3)  # 线程池 放3个线程
    tasks = [loop.run_in_executor(p,get_url,'http://www.langzi.fun') for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print('last time:{}'.format(time.time() - start_time))

