# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 0020 21:42
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : mysql.py
# @Software: PyCharm
import sys
import pymysql
reload(sys)
sys.setdefaultencoding('utf-8')

c = pymysql.connect(user='root',passwd='root',host='127.0.0.1',port=3306,db='test')