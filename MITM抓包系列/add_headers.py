# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
from mitmproxy import http

def response(flow:http.HTTPResponse)->None:
    print('-'*30)
    print(flow.request)
    # Request(GET langzi.fun:80/upload/TIM%E6%88%AA%E5%9B%BE20190422162029.png)
    # 请求发送 请求的url
    print(flow.response)
    # Response(200 OK, image/png, 61.29k)
    # 返回状态码 返回的信息类型 返回的文件大小
    print(flow.client_conn)
    # <ClientConnection: 127.0.0.1:28055>
    # 本地发起连接
    print(flow.server_conn)
    # <ServerConnection: langzi.fun:80>
    # 服务器端口
    print('-'*30)
