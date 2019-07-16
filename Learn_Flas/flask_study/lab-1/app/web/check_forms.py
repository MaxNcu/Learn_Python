# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 0022 22:50
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : wtforms.py
# @Software: PyCharm
import sys
sys.path.append('..')
from wtforms import Form, StringField,IntegerField
# Form是wtforms的基类，StringField主要负责验证字符串类型的参数,Int负责数字类型
from wtforms.validators import Length,NumberRange,DataRequired
# validators是内置的验证对象，Length主要用来验证对象长度，NumberRange验证数字的大小,DataRequired验证传入的敏感参数，比如空格
reload(sys)
sys.setdefaultencoding('utf-8')


class check_form(Form):
    name = StringField(validators=[DataRequired(),Length(min=1,max=10)],default='浪子')
    # 验证name参数，DataRequired()验证传入的参数，其中Length负责校验长度的最大最小值，validators是一个数组，里面除了Length之外还可以放别的函数
    id = IntegerField(validators=[DataRequired(),NumberRange(min=1,max=1000)],default=1)
    # 验证id参数，要求在1-1000之间


# 传递参数的时候可以直接传入request.args
# 然后实例化对象的validate
# form = check_form(request.args)
# if form.validate():
#     name = form.name.data
#     id = form.id.data
# else:
#      return form.errors
# 当然还可以使用strip()清洗传入的参数
