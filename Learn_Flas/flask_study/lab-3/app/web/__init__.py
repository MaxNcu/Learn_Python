# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 0019 18:41
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : check_forms.py.py
# @Software: PyCharm

from flask import Blueprint

web = Blueprint('web',__name__)

from app.web import Mmzi

