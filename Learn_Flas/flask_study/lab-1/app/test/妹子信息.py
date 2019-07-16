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
# )charset=utf8,engine=INNODB;
# ALTER TABLE `data` ADD UNIQUE (
# `title`
# )

def start():
    lock.acquire()
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Referer':'www.mzitu.com'

    }
    url = 'http://www.mzitu.com/page/'
    for _ in range(1,188):
        list_dir=[]
        img_dir=[]
        try:
            rr = re.findall("data-original='(.*?)' /></a><span><a.*?href=\"(.*?)\" target=\"_blank\">(.*?)</a></span><span",requests.get(url=str(url+str(_)),timeout=5).content,re.S)
            for x,y,z in rr:
                count = re.search('><span>(\d\d)</span></a><a',requests.get(url=y,timeout=5).content,re.S).group().replace('<span>','').replace('</span></a><a','').replace('<','').replace('>','')
                for test_1 in range(1,int(count)):
                    url_1 = y+str('/')+str(test_1)
                    img = re.search('<img src="(.*?)" alt=',requests.get(url_1).content).group().replace('<img src="','').replace('" alt=','')
                    img_dir.append(img)
                print unicode(('Page:%s  Title:%s  URL:%s  count_img:%s')%(str(_), z, y,str(count)), 'utf-8')
                with mysql() as cursor:
                   sql = "insert into data(title,url,show_img,all_img) VALUES (%s,%s,%s,%s)"
                   cursor.execute(sql,(z,y,x,str(img_dir).replace("'",'|')))
        except Exception,e:
            print e
    lock.release()

lock =threading.Lock()
for x in range(10):
    t=threading.Thread(target=start).start()