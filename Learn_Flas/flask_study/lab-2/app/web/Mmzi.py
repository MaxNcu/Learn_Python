# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 0017 21:06
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : Mmzi.py
# @Software: PyCharm
import sys
from flask import Flask,make_response,request,Response,render_template
import time,re
import requests
from flask import Blueprint
from . import web
reload(sys)
sys.setdefaultencoding('utf-8')



def meizi(id):
    headerss = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Referer':'www.mmjpg.com'

    }
    headers = {'Content-Type':'html/text'}
    r = requests.get(url=str('http://www.mzitu.com/search/' + str(id)),headers=headerss)
    rr = re.findall("</a><span><a.*?href=\"(.*?)\" target=\"_blank\">(.*?)</a></span><span",r.content,re.S)
    list_dir=[]
    for x,y in rr:
        img_logo = re.search('<img src="(.*?)" alt=',requests.get(x).content).group().replace('<img src="','').replace('" alt=','')
        list_dir.append((img_logo,x,y))
    return list_dir


@web.route('/index/')
def index():
    return render_template('index.html')



@web.route('/search/',methods=['POST','GET'])
def search():
    if request.method == 'POST':
        idx = request.form['idx']
        data=meizi(idx)
        if data == []:
            return render_template('404.html')
        else:
            return render_template('result.html', data=data)
    else:
        return render_template('404.html')






