# -*- coding:utf-8 -*-
from multiprocessing import Pipe,Process
import time
def produce(pipe):
    pipe.send('666')
    time.sleep(1)
def consumer(pipe):
    print(pipe.recv())
    # 有些类似socket的recv方法
if __name__ == '__main__':
    send_pi,recv_pi = Pipe()
    my_pro = Process(target=produce,args=(send_pi,))
    my_con = Process(target=consumer,args=(recv_pi,))
    my_pro.start()
    my_con.start()
    my_pro.join()
    my_con.join()