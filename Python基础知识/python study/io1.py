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
'''
print unicode('成功:','utf-8')  
print unicode(strName,'utf-8')  
#strName 是字符串          
通过res.content.decode("utf8","ignore").encode("gbk","ignore")就不会有乱码了
.decode('utf-8').encode('gbk')
s = '主播'  
s.decode('utf-8').encode('gb18030')  
'''
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
#iter  迭代器的使用
#items 字典中迭代
list = [1,2,3,4,5,6]
list1 = iter(list)
print list1.next()
print list1.next()
print list1.next()
print list1.next()
print '\n'
f1 = open('io1.txt','a+')
f1.writelines([str(x) for x in list])
#f1.write([str(x) for x in list]) 错误的
f1.close()



for i in iter(list):
    print i
dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}

print "字典值 : %s" % dict.items()

# 遍历字典列表
for key, values in dict.items():
    print key, values
    print type(key)

# f1 = open('urllib1.py','r')
# #尽量较少内存使用  不消耗大量内存
# f2 = iter(f1)
# for xx in f2:print xx

print sorted(dict)
print sorted(zip(dict.itervalues(),dict.iterkeys()))
for x in dict.iteritems():print x
