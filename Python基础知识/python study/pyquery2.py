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
from pyquery import  PyQuery as pq
reload(sys)
sys.setdefaultencoding('utf-8')
pq1 = pq(url='http://eladies.sina.com.cn/photo/', encoding="utf-8")
print pq1('span').text() + '\n'



#print pq1('li').text() + '\n'
print '++' + pq1('li').eq(3).text() + '\n'

print '--' + str(pq1('div').find('p').eq(1))



li = pq1('li')  #处理一个li的列表
#for i in li:print pq1(i).text() + '\n'



print pq1('a').attr('href') #寻找单独的的href  必须要在同一个标签里面
print pq1('#SI_Scroll_2_Prev')   #寻找id=SI_Scroll_2_Prev 的内容

print pq1('.next')  #寻找class=next#  的内容

# print '**' + str(pq1('div','a'))

#



#remove
#有时候我们获取文本信息的时候可能并列的会有一些其他标签干扰，这个时候通过remove就可以将无用的或者干扰的标签直接删除，从而方便操作
# wrap = pq1('.next')
# print(wrap.text())
# wrap.find('i').remove()
# print 'xx' + (wrap.text())