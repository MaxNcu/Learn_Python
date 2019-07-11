# -*- coding:utf-8 -*-
import socket
from urllib.parse import  urlparse
# 对url做解析

def get_url(url):
    url = urlparse(url)
    # 对传入的网址进行解析，比如传入http://www.langzi.fun/admin.php
    host,path = url.netloc,url.path
    # 获取传入网址的主域名和后面的url路径
    if path == '':
        path = '/'
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    c.setblocking(False)
    # 这里设置成非阻塞模式

    try:
        c.connect((host, 80))
    except BlockingIOError as e:
        pass
    # 这里不停的循环请求，一直到TCP完成三次握手


    headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    # 绑定ip与端口
    while True:
        try:
            c.send('GET {}\r\nHost:{}\r\nUser-Agent:{}\r\n'.format(path, host, headers).encode('utf-8'))
            break
        except OSError as e:
            pass
    # 发送请求，请求方式为GET 内容是url的路径，然后分隔换行
    # 发送请求，请求的HOST主机就是主域名
    # 在这里可以把请求头，cookie加进来


    data = b''
    # 获取数据
    while 1:
        try:
            d = c.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data +=d
        else:
            break
    print(data.decode('utf-8'))


get_url('http://www.langzi.fun/admin.php')
