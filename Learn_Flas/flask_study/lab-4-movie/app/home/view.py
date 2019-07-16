# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 0015 13:48
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : view.py
# @Software: PyCharm
import sys
sys.path.append('..')
from . import home_print
reload(sys)
sys.setdefaultencoding('utf-8')

@home_print.route('/')
def index():
    return 'hello word web'