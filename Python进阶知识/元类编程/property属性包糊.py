# -*- coding:utf-8 -*-

class magic:
    def __init__(self):
        self._user = ''
    # 接受传入参数

    @property
    def login(self):
        return '用户:{}登陆成功，欢迎您！'.format(self._user)

    # 这里返回的是一个字符串，使用property装饰后，这个函数就代表这个字符串
    # 具体：使用property后，这个login函数调用方式就变成了
    # m = magic()
    # print(m.login) # 这里不能有m.login()括号
    # >> 用户:登陆成功，欢迎您！

    # 一旦login函数被property装饰，就拥有可读的属性 >> print(m.login)
    # 但是不能修改


    @login.setter
    # 如果想要拥有可修改的功能，就需要@login.setter装饰
    # 被装饰的checks函数，具有可以写的功能
    def checks(self,value):
        if value == '浪子':
            self._user = value
        else:
            raise ValueError('用户：{} 不许登陆'.format(value))
        self._user = value

if __name__ == '__main__':
    m = magic()
    # 实例化对象
    m.checks = '浪子'
    # 传入值
    print(m.login)
    # 打印值




