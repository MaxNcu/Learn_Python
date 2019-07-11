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
import pymysql
reload(sys)
sys.setdefaultencoding('utf-8')
# conn = pymysql.connect(host='127.0.0.1', user='root', passwd="root", db='mysql')
# cur = conn.cursor()
# cur.execute("show databases")
# for r in cur:
#     print(r)
# cur.close()
# conn.close()
import pymysql
global coon
coon = pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='url')
cur = coon.cursor()
cur.execute('show databases')
for x in cur:print x
cur.execute(r'select * from tv')
for x in cur:print x
cur.execute('show tables')
for x in cur:print x
# cur.execute('create database test1')
# for x in cur:print x
# cur.execute('drop database test1')
# for x in cur:print x

cur.close()
coon.close()
