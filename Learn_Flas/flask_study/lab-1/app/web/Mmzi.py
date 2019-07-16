# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 0017 21:06
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : Mmzi.py
# @Software: PyCharm
import sys
sys.path.append('..')
reload(sys)
from flask import Flask,make_response,request,Response,render_template,url_for
import time,re
import pymysql
import requests
from flask import Blueprint
from . import web

import contextlib
sys.setdefaultencoding('utf-8')

@contextlib.contextmanager
def mysql(host='127.0.0.1', port=3306, user='root', passwd='root', db='meizi',charset='utf8'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = conn.cursor()
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()

# def meizi(id):
#     headerss = {
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
#         'Referer':'www.mmjpg.com'
#
#     }
#     headers = {'Content-Type':'html/text'}
#     r = requests.get(url=str('http://www.mzitu.com/search/' + str(id)),headers=headerss)
#     rr = re.findall("</a><span><a.*?href=\"(.*?)\" target=\"_blank\">(.*?)</a></span><span",r.content,re.S)
#     list_dir=[]
#     for x,y in rr:
#         img_logo = re.search('<img src="(.*?)" alt=',requests.get(x).content).group().replace('<img src="','').replace('" alt=','')
#         list_dir.append((img_logo,x,y))
#     return list_dir

def meizi(id):
    idx = id.replace("'",'').replace('"','').replace('-','').replace('\\','').replace('and','').replace('or','').replace('&','').replace('|','').replace(')','').replace('(','').replace('=','').replace('#','').replace('%','')
    if len(idx)>10 or idx =='' or idx ==' ':
        return None
    with mysql() as cursor:
        sql = "select * from data where title like '%" + idx + "%'"
        row_count = cursor.execute(sql)
        row_1 = cursor.fetchall()
        return row_1

def meizii(id):
    idx = id.replace("'",'').replace('"','').replace('-','').replace('\\','').replace('and','').replace('or','').replace('&','').replace('|','').replace(')','').replace('(','').replace('=','').replace('#','').replace('%','')
    if len(idx)>30 or idx =='' or idx ==' ' or idx.find('http')<0:
        return None
    with mysql() as cursor:
        sql = "select * from data where url ='" + idx + "'"
        row_count = cursor.execute(sql)
        row_1 = cursor.fetchall()
        return row_1


@web.route('/')
def index():
    return render_template('index.html')



@web.route('/search/',methods=['POST','GET'])
def search():
    if request.method == 'POST':
        idx = request.form['idx']
        data=meizi(idx)
        print data
        if data == [] or data == None:
            return render_template('404.html')
        else:
            return render_template('result.html', data=data)

    else:
        return render_template('404.html')

@web.route('/code/')
def get_code():
    return render_template('down.html')


@web.route('/downimg/',methods=['POST','GET'])
def downimg():
    if request.method == 'POST':
        idx = str(request.form['name']).replace('+','').replace('=','').replace('%2c','')
        data = meizii(idx)
        if data == [] or data == None :
            return render_template('404.html')
        else:
            for a,b,c,d,e in data:
                print a,b,c
                e = e+'|]'
                return render_template('downimg.html', data_title=b,data_url=e)
    else:
        return render_template('404.html')




