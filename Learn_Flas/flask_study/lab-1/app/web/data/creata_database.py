# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 0024 13:40
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : creata_database.py
# @Software: PyCharm
import sys
sys.path.append('..')
from sqlalchemy import Column,Integer,String
# 导入column（字段），Integer（数字类型）
from flask_sqlalchemy import SQLAlchemy
# 实例化sqlalchemy对象，在flask中导入进来
reload(sys)
sys.setdefaultencoding('utf-8')

db = SQLAlchemy()
class data(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 设置id号为数据库的主键，并且自增长
    # 相当于SQL:id int primary key auto_increment
    title = Column(String(100), nullable=True, default='获取该妹子信息失败')
    # 页面标题长度为100，并且允许为空，如果为空的话就生成上面的default
    url = Column(String(100), nullable=False, unique=True)
    # 该页面的主网址长度100，不允许为空,不允许重复
    show_img = Column(String(100), nullable=False)
    # 页面的单张展示图片
    all_img = Column(String(2000), nullable=False)

    # 页面的所有图片


    def sample(self):
        pass