# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 0015 14:54
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : models.py
# @Software: PyCharm
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@127.0.0.1:3306/movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# 创建会员模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)
    phone = db.Column(db.String(11),unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(255),unique=True)
    addtime = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    uuid = db.Column(db.String(255),unique=True)

    def __repr__(self):
        return "<User %r>"%self.name
# 创建会员日志模型
class Userlog(db.Model):
    __tablename__ = 'userlog'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    # 使用外键绑定user表的id


