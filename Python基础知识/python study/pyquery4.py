# -*- coding: utf-8 -*-
"""
__author__ = 'Langziyanqin'
__QQ__ = '982722261'
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import sys
from pyquery import PyQuery as pq
reload(sys)
sys.setdefaultencoding('utf-8')

p = pq('<p id="hello" class="hello"></p>')('p')
print p.addClass('beauty')
print p.removeClass('hello')


from pyquery import PyQuery as pq
print pq('http://cuiqingcai.com/', headers={'user-agent': 'pyquery'})
print pq('http://httpbin.org/post', {'foo': 'bar'}, method='post', verify=True,allrow_redirects=False)