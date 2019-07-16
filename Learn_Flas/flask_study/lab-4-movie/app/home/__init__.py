# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 0015 13:41
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : __init__.py.py
# @Software: PyCharm
import sys
from flask import Blueprint
reload(sys)
sys.setdefaultencoding('utf-8')

home_print = Blueprint('home',__name__)

import view