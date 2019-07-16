# coding:utf-8
import sys
sys.path.append('..')
reload(sys)

# 下面两行注册蓝图
from flask import Blueprint
home = Blueprint('home',__name__)

# 导入并且运行主要逻辑函数
import views






