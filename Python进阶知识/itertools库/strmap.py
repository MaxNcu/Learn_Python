# -*- coding:utf-8 -*-
import itertools

import re

s = 'aaaaa-8-aaaaa-9-aaaa'
a = re.search('-(\d)-',s).group(0)
print(a)
a = re.match('-(.*?)-',s)
print(a)


# a = itertools.product('浪子', '好帅')
# print(list(a))
# import string
# def test(x):
#     if x in string.ascii_lowercase:
#         return True
#     else:
#         return False
# a = itertools.starmap(test,['a','A','1'])
# print(list(a))