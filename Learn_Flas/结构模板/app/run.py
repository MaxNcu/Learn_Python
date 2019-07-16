# -*- coding: utf-8 -*-
import os
from flask import Flask
import config
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# 注册蓝图
def start_Blueprint(app):
    from home import home
    from admin import admin
    app.register_blueprint(home)
    app.register_blueprint(admin,prefix_url='/admin')

def create_app():
    app = Flask(__name__,template_folder=('templates'),static_folder=('static'))
    app.config.from_object(config)
    start_Blueprint(app)
    return app


if __name__ == '__main__':
    app = create_app()
    print 'Waiting......'
    app.run(host='0.0.0.0',threaded=True,port=5000)
