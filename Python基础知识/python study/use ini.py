# -*- coding: utf-8 -*-
"""
__author__ = 'Langziyanqin'
__QQ__ = '982722261'
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import sys
import os
import ConfigParser
reload(sys)
sys.setdefaultencoding('utf-8')
cfg = ConfigParser.ConfigParser()
#print help(cfg.read)
with open('use.ini','w+')as f:
    f.write('''[Server] #MYSQL配置
Server=localhost   #主机
Username=root     #用户名
password=root #密码
db=url    #数据库url
[DATA] #软件配置
TX_Queue=1    #消息队列维护线程,此设置不要修改，一定为1，不然数据库压力大
TX_openrul=2  ;设置采集线程，2个就相当够了，主要是cms识别花时间
    ''')
cfg.read('use.ini')
print cfg.sections()
for x in cfg.sections():
    #print x
    print cfg.items(x)

name = cfg.get("Server", "Username")
print(name)
age = cfg.get("DATA", "TX_openrul")
print age
print type(age)
cfg.set("Server","Username","oooo")
print cfg.get("Server","Username")
cfg.write(open('use.ini', 'w'))