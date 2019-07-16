# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 0019 18:36
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : __init__.py.py
# @Software: PyCharm
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.web.data.creata_database import db
sys.path.append('..')
from app.web.data.cretae_data_pymysql import Base
reload(sys)
sys.setdefaultencoding('utf-8')


def create_app():
    app = Flask(__name__,template_folder=('web/templates'),static_folder=('web/static'))
    app.config.from_object('config')
    start_Blueprint(app)
    db.init_app(app)
    with app.app_context():
      db.create_all(app=app)
    return app

def start_Blueprint(app):
    from app.web import web
    app.register_blueprint(web)
