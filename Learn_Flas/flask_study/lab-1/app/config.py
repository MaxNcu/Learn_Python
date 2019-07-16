# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 0017 20:42
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : config.py
# @Software: PyCharm
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@127.0.0.1:3306/meizi'
# SQLALCHEMY_DATABASE_URI是flask定义好的配置项，就像DEBUG一样
# mysql + cymysql ： 使用mysql数据库，驱动使用cymysql（需要pipenv install cymysql）,你还可以使用pymysql
# 然后数据库账号密码,主机和端口以及数据库名字
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/meizi?charset=utf8'
# SQLALCHEMY_TRACK_MODIFICATIONS = True
