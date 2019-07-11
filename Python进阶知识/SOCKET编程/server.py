# -*- coding:utf-8 -*-
import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('0.0.0.0',9999))
s.listen()

def handle_sock(sock,addr):
    while 1:
        inp = input('输入消息:')
        sock.send(inp.encode('utf-8'))
        data = sock.recv(1024)
        print('接收消息:' + data.decode('utf-8'))

while 1:
    sock, addr = s.accept()
    clinent_thread = threading.Thread(target=handle_sock,args=(sock,addr))
    clinent_thread.start()
