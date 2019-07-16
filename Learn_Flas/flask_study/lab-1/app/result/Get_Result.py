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
reload(sys)
sys.setdefaultencoding('utf-8')


web = Blueprint('web',__name__)

def meizi(id):
    headerss = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }
    headers = {'Content-Type':'html/text'}
    r = requests.get(url=str('http://www.mzitu.com/search/' + str(id)),headers=headerss)
    print r.url
    rr = re.findall("data-original='(.*?)' /></a><span><a.*?href=\"(.*?)\" target=\"_blank\">(.*?)</a></span><span",r.content,re.S)
    return rr


@web.route('/index/')
def index():
    return render_template('index.html')



@web.route('/search/',methods=['POST','GET'])
def search():
    if request.method == 'POST':
        idx = request.form['idx']
        return render_template('result.html', data=meizi(idx))
    else:
        return render_template('404.html')




