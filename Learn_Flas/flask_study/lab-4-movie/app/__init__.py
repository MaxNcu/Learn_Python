# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 0015 14:27
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : __init__.py.py
# @Software: PyCharm
import sys
sys.path.append('..')
from admin import admin_print
from home import home_print
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

reload(sys)
sys.setdefaultencoding('utf-8')
app = Flask(__name__,template_folder='templates',static_folder='static')
app.congih['SQLALCHEMY_DATABASE_URI']=''
app.register_blueprint(admin_print,url_prefix='/admin')
app.register_blueprint(home_print)