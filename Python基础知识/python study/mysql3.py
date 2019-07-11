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
global coon
#host charset db port 字符串类型
#常用 cursor commit close

def select(sql):
    coon = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='lang_cms', charset='utf8')
    cur = coon.cursor()
    try:
        cur.execute(sql)
        coon.commit()
        print cur
        print coon
        # print cur.fetchall()
        print cur.fetchall()

    # fetch* 对数组遍历  使用指针  移动指针 在缓冲区取出数据
    except:
        coon.rollback()
    finally:
        print cur.rowcount
        cur.close()
        coon.close()

sql_insert = "insert into url_3(urllist,cms) VALUES ('www123456798','1111111')"
select(sql_insert)


#conn.commit()  让前面所有执行操作同时生效
#conn.rollback() 让前面所有执行操作同时取消操作

#总结
当存在多条语句执行的时候，先建议一个函数，然后批量执行这个函数
比如 defult(sql1)
defult(sql2)
defult(sql3)
然后输入COON.COMMIT（）
就可以批量执行了
优化版

try:
    select(sql1)
    select(sql2)
    select(sql3)
    coon.commit()
except:
    coon.rollback()  #这样就会  如果都是成功就可以执行 如果任何一个语句执行失败就全部不要执行