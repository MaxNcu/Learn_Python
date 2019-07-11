# -*- coding:utf-8 -*-
import socket
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('127.0.0.1',9999))
while 1:
    data = c.recv(1024)
    print('接收消息:'+data.decode('utf-8'))
    inp = input('输入消息:')
    c.send(inp.encode('utf-8'))

