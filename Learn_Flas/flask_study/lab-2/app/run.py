# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 0019 18:38
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : run.py
# @Software: PyCharm
import sys
sys.path.append('..')
from app import create_app

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'sa'
app.config['MYSQL_DATABASE_DB'] = 'zhihu'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

reload(sys)
sys.setdefaultencoding('utf-8')
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'])
