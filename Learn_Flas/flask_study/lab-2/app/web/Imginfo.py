# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 0019 19:36
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : Imginfo.py
# @Software: PyCharm
import sys
import requests
from . import web
from flask import render_template
reload(sys)
sys.setdefaultencoding('utf-8')

@web.route('/imginfo')
def imginfo():
    return render_template('404.html')


