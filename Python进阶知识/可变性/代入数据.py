# -*- coding:utf-8 -*-
import random
import threading
import multiprocessing
import string
import time
t1 = time.time()
def write(x):
    with open('a.txt','a+')as a:
        a.write(x + '\n')

def run():
    for x in range(10000000):
        strs = str(random.randint(1000,2000)) +random.choice(string.ascii_letters)*10
        write(strs)
for x in range(10):
    t = threading.Thread(target=run)
    t.start()
t2 = time.time()
print(t2 - t1)