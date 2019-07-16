# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 0003 22:09
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 妹子信息.py
# @Software: PyCharm
import sys
import requests
import re
import pymysql
import contextlib
import threading
#定义上下文管理器，连接后自动关闭连接
reload(sys)
sys.setdefaultencoding('utf-8')

@contextlib.contextmanager
def mysql(host='127.0.0.1',user='root',passwd='root',db='meizi',port=3306,charset='utf8'):
    conn = pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='meizi',port=3306,charset='utf8')
    cursor = conn.cursor()
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()

# # 执行sql
# with mysql() as cursor:
#    print(cursor)
#    row_count = cursor.execute("select * from tb7")
#    row_1 = cursor.fetchone()
#    print row_count, row_1

# 创建数据库
# create table data(
# id int primary key auto_increment,
# title varchar(80),
# url varchar(100),
# show_img varchar(80),
# all_img varchar(2000),
# index index_neme1 (title),
# index index_neme2 (url)
# )charset=utf8,engine=INNODB;
# ALTER TABLE `data` ADD UNIQUE (
# `title`
# )

def start():


    for _ in range(1,3):
        url = 'http://www.mmjpg.com/data.php?id=%s&page=8999' % str(_)
        headers = {
            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive',
            'DNT': '1',
            'Host': 'www.mmjpg.com',
            'Referer': 'http://www.mmjpg.com/mm/%s',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'

        }
        headers['Referer'] = headers['Referer']%str(_)
        print headers
        try:

            r = requests.get(url=url,headers=headers,timeout=5)
            print r.status_code
            print r.content
            # 标题，图片，url就是url
            rr = re.findall('<h2>(.*?)</h2>.*?data-img="(.*?)" alt=',r.content,re.S)
            print rr
        except Exception,e:
            print e
start()
