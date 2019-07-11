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

reload(sys)
sys.setdefaultencoding('utf-8')
f1 = open('io1.txt','r')
#f2 = f1.read()
f3 = f1.readlines()  #返回的是一个列表
f1.close()
#print f2
print f3    #只能读取一次  第二次读取就没办法读取出来

#文件对象的属性
#file.fileno() 文件描述
# file.mode   文件打开权限  r  w  a+
# file.encoding  文件编码格式

s = sys.argv[0]
print s
if __name__=="__main__":
    # print len(sys.argv)
    diyigecanshu = sys.argv[1]
    print diyigecanshu
    for x in sys.argv:
        print x
    #main()