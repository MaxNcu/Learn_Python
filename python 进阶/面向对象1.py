# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 0003 16:42
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 面向对象1.py
# @Software: PyCharm

import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

class studetn:
    # 定义一个类名为studetn
    def __init__(self,idx):
    # 定义初始化构造，这里使用init，还有别的属性比如reversed，iter之类的
        self.idx=idx
        # 初始化变量，方便继承
    def run(self):
    # 定义运行函数，从上面继承变量
        print self.idx
        # 打印出idx的值，或者做一些别的处理
        time.sleep(1)

a=studetn('a')
a.run()
# 这是类的调用，一定要记得类的使用方法，首先传入参数，类赋值给一个变量
# 然后调用这个类下面定义的函数
