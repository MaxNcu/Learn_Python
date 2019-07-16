# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 0015 13:37
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : manage.py
# @Software: PyCharm
import sys
sys.path.append('..')
from app import app


reload(sys)
sys.setdefaultencoding('utf-8')

app.run()