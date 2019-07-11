# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 0021 20:22
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 装饰器.py
# @Software: PyCharm
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def outer(func):
# 定义装饰器，接受一个参数，这个参数可以是任何对象(装饰器接受一个函数)
    def inner():
        print("装饰器加载开始")
        result = func()
        # 把传入的函数执行，执行后返回的结果赋值给result
        print("装饰器加载成功！")
        # 传入的函数执行后，显示装饰成功
        return result
        # 返回传入函数执行的结果
    return inner
    # 这里返回内部函数本体，这里返回的inner会被赋值给下面的f1，于是f1就变成了inner,f1函数被inner函数覆盖

@outer
# 当程序执行到这里，发现了@outer，立即执行这个装饰器，于是把被装饰对象(就是下面这个函数名：注意是f1并不是f1()传递进去)
def f1():
    # 当上面的执行后，这里f1就是inner。在这里调用f1其实就是调用inner()
    print("f1函数执行......")

f1()
