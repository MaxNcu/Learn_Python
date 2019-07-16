# coding:utf-8
# 导入蓝图
from . import home

# 导入其他配置文件
from flask import session,url_for,redirect,render_template
# 导入数据库模型操作，这个要根据需求来导入编辑

# 编写登陆状态监测装饰器
from functools import wraps
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'login' in session:
            '''
            这里的login等等需要根据你自己设置的session判断
            '''
            if session['login'] == True:
                return func(*args, **kwargs)
            else:
                return redirect(url_for('home.error'))
        else:
            return redirect(url_for('home.error'))
    return wrapper


# 主要逻辑视图函数
@home.route('/')
def index():
    return 'hello home'

@home.route('/error/')
def error():
    return '404 not found'
