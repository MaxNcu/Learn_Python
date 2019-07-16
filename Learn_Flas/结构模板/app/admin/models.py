# coding:utf-8
# 导入必备的模块
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time
import contextlib
# 导入配置文件中的设置信息
from .. import config


# 创建数据库ORM模型
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(config)
db = SQLAlchemy(app)

class url_index(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    url = db.Column(db.String(80),unique=True,nullable=False)
    checks = db.Column(db.Integer,default=0,index=True)
    time = db.Column(db.String(50),default=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

    def __repr__(self):
        return '%s'%self.url




# 这一行代码是创建数据
db.create_all()

# 写一个装饰器用来每次的数据插入执行等等
@contextlib.contextmanager
def data2mysql():
    try:
        yield db
    except:
        db.session.rollback()
    finally:
        db.session.remove()

'''
使用方法

		url = 'http://www.langzi.fun'
        first_ins = url_index(url=url)
        with data2mysql() as dbs:
            dbs.session.add(first_ins)
            dbs.session.commit()

'''

