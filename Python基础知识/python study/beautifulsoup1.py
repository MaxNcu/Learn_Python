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
import re
from bs4 import BeautifulSoup as bs
import lxml
reload(sys)
sys.setdefaultencoding('utf-8')
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
bp = bs(html,'lxml')
#print bp.name
#print bp.text
print bp.title  #输出结果带有<title>
print bp.title.string  #只输出标签里面的内容
print bp.a  #输出的结果带有<a>
print bp.a.string  #输出的结果是<a>里面的内容
#print bp.prettify()  #格式化输出

print bp.a.attrs  #输出的结果是字典，就是每个=号对应的字典  那么
print bp.a.attrs['id']  #这样就能得到id对应的链接


#遍历文档树
print bp.p.contents  #只输出p标签的内容，不带有标签，返回对象是列表,可以在列表中选择[0]

#print bp.body.children   #返回对象不是列表，返回所有标签的内容 ，所有
#for x in bp.body.children:print x

#print bp.find_all('a')  #寻找所有a标签，但是输出结果带有<a>   bp.find_all(['a','b'])两个都寻找
for x in bp.find_all('a'):print x.string   #寻找所有a标签，并且输出结果不带有标签
print bp.find_all('a',limit=3) #只要三个

#配合正则表达式一起使用
for x in bp.find_all(re.compile('hea')):print x.string   #和上面同理 string 换成name 都可以 这个只能匹配标签头

print bp.find_all(id='link2')
print bp.find_all(href=re.compile('till'))
print bp.find_all(id='link1',href=re.compile('el'))


print bp.find_all('a',class_='sister')
print bp.find_all(attrs={'id':'link3'})

print bp.find_all(text=re.compile('D'))  #text是在内容寻找，不能在标签里寻找


####################################################
#通过标签来查找  返回对象是列表
print bp.select('a')
#类名 class='sister'  其中sister就是类名
print bp.select('.sister')
#id名称来查找
print bp.select('#link2')
#组合在一起查找  中间空格分开
print bp.select('p #link2')  #输出结果不带有p标签
#直接用子标签查找
print bp.select('head > title')
for x in bp.select('a'):print x.get_text

