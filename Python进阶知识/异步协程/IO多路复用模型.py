# -*- coding:utf-8 -*-
import socket
from urllib.parse import urlparse
from selectors import DefaultSelector,EVENT_READ,EVENT_WRITE
# 使用IO多路复用下的select方法实现，Python包中selectors是对select做了一个优化封装
# DefaultSelector会自动选择select还是epoll，windows是select,linux是epoll
# EVENT_READ,EVENT_WRITE 分别是读事件和写事件,即对文件描述符的操作


selector = DefaultSelector()
# 实例化一个全局的select方法

urls = ['http://www.langzi.fun/admin.php','https://www.lds.org']
# 需要访问的url
stop = False
# 设置全局变量stop，功能是如果一个socket连接完成后就继续下一个


class Fetcher:
    '''
    使用类方法更加易于操作，

    顺序逻辑如下
    1. 调用get_url函数 --(当某个socket连接可用发送数据，即可以写入数据)--> 2. 调用connected()函数发送数据--(当数据发送出去，数据变成可读)--> 3. 调用readable()函数，打印数据


    概念介绍：

    回调：当逻辑变成可写设置好状态(EVENT_WRITE可以写入/EVENT_READ可以读取)的时候，需要执行什么函数
    例子：(self.client.fileno(),EVENT_READ,self.readable)
        当 self.client.fileno() 的描述符  变成 EVENT_READ (可以读) 的时候 ，就执行readable()函数


    '''

    def connected(self,key):
        # connected 是回调函数
        # 回调函数：当逻辑变成可写EVENT_WRITE的时候，需要执行什么函数
        selector.unregister(key.fd)
        self.client.send('GET {}\r\nHost:{}\r\nUser-Agent:{}\r\n'.format(self.path, self.host, self.headers).encode('utf-8'))
        selector.register(self.client.fileno(),EVENT_READ,self.readable)


    def readable(self,key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            self.client.close()
            print(self.data.decode()+'\n\n\n')
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True



    def get_url(self,url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b''
        self.headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

        if self.path == '':
            self.path = '/'
        # 完成对传入的URL进行分割

        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.setblocking(False)
        # 实现一个客户请求端,设置成非阻塞模式

        try:
            self.client.connect((self.host,80))
        except BlockingIOError as e:
            pass
        # 实现对目前发起请求


        selector.register(self.client.fileno(),EVENT_WRITE,self.connected)
        '''
        注册文件描述符(传入事件的描述符，设置是等待【读事件】还是【写事件】，设置回调函数)
        
        self.client.fileno() 是发起连接的描述符
        EVENT_WRITE          是写入事件(因为要对链接发起请求)
        self.connected       是回调函数
        
        即当self.client的事件描述符变成可以写入的模式的时候，就调用self.connected函数
        功能是监听self.client 是否可以写入(是否完成连接，能否发起数据)
        
        '''

def loop():
    # 核心函数
    # 循环对selector监控，查看哪个clinet可读可写
    # 事件循环，不停请求socket状态并调用对应的回调函数
    # 1. seclet本身不支持register模式，但是selector对select优化封装
    # 2. socket状态变化后的回调是由程序员完成的
    # 3. 回调如果要系统运行那就只能通过aio(异步io模型)完成

    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)

    # 回调+事件循环+select(poll/epoll)



if __name__ == '__main__':
    for x in urls:
        fetcher = Fetcher()
        fetcher.get_url(x)
    loop()  # 事件循环