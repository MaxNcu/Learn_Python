# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 0015 13:42
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : __init__.py.py
# @Software: PyCharm
import sys
from flask import Blueprint
reload(sys)
sys.path.append('..')
sys.setdefaultencoding('utf-8')
admin_print = Blueprint('admin',__name__)


import view