# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import datetime,re
from mitmproxy import http

def write_data(x):
    with open('log.txt','a+',encoding='utf-8')as a:
        a.write(x + '\n\n')

def response(flow:http.HTTPResponse)->None:
    print('-'*30)
    if 'image' not in str(flow.response) and '/css' not in str(flow.response) and 'video' not in str(flow.response):
        write_data('当前请求:'+str(flow.request.url))
        write_data('请求方式:'+str(flow.request.method))
        write_data('状态码:'+str(flow.response.status_code))
        write_data('内容长度:'+str(flow.response.headers.get('Content-Length', 0)))
        write_data('返回内容:'+str(flow.request.content))
        write_data('--------------------------------------------------------------------------')




    print('-'*30 + '\n数据：'+str(flow.request.content)+'\n'+'-'*30)