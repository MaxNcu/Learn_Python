# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 0019 18:41
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : __init__.py.py
# @Software: PyCharm
import sys
from flask import Flask
reload(sys)
sys.setdefaultencoding('utf-8')

def create_app():
    app = Flask(__name__,template_folder=('templates'))
    app.config.from_object('config')
    Blueprint(app)
    return app

def Blueprint(app):
    from app.web.Mmzi import web
    app.register_blueprint(web)
