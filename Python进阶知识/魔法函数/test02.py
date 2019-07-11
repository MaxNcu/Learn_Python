#-*- coding:utf-8 -*-
class wallet(object):
    def __init__(self,man):
        self.man=man

    def __enter__(self):
        print(self.man + '放心大胆的掏出了钱包')
        return self
    # return self 这一步非常重要，作用是返回实例

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.man + '小心翼翼的收起来钱包')

    def use_money(self,money):
        print(self.man + '花了' + money +'元')

with wallet('浪子')as a:
    a.use_money('600')

# import contextlib
#
# @contextlib.contextmanager
# def use_money(man):
#     try:
#         print(man + '十分放心大胆的掏出钱包')
#         yield None
#     finally:
#         print(man + '万分谨慎的收起了钱包')
#
# with use_money('langzi')as a:
#     print('花了1块钱')