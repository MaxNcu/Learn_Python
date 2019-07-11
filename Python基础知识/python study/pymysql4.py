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

global passwd
##查询
def select():
    coon = pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='test')


##插入
def insert(name, pwd):
    conn = pymysql.connect(user='root', passwd='你的密码',
                           host='localhost', db='test', charset='utf8')
    cur = conn.cursor()
    sql = "INSERT INTO user (Name,Password) VALUES ('" + name + "','" + pwd + "')"
    print(sql)
    sta = cur.execute(sql)
    if sta == 1:
        print('Done')
    else:
        print('Failed')
    conn.commit()
    cur.close()
    conn.close()


##更新
def update(name, pwd):
    conn = pymysql.connect(user='root', passwd='你的密码',
                           host='localhost', db='test', charset='utf8')
    cur = conn.cursor()
    sql = "UPDATE USER SET PASSWORD='" + pwd + "' WHERE NAME='" + name + "'""'"
    print(sql)
    sta = cur.execute(sql)
    if sta == 1:
        print('Done')
    else:
        print('Failed')
    conn.commit()
    cur.close()
    conn.close()


##删除
def delete(name):
    conn = pymysql.connect(user='root', passwd='你的密码',
                           host='localhost', db='test', charset='utf8')
    cur = conn.cursor()
    sql = "DELETE FROM USER WHERE Name='" + name + "'"
    print(sql)
    sta = cur.execute(sql)
    if sta == 1:
        print('Done')
    else:
        print('Failed')
    conn.commit()
    cur.close()
    conn.close()