# -*- coding:utf-8 -*-

'''
对于bytes编码的数据来说
只有decode方法
就是把bytes编码的数据转换成utf-8编码

对于utf-8编码的数据来说
只有encode方法
就是把utf-8编码的数据转换成bytes编码

'''
a = '浪子'
print(a.encode())
# 默认是编码成bytes
print(a.encode('gbk'))
# 将utf-8编码格式转换成gbk编码格式
print(a.encode().decode('utf-8'))
print(a.encode('gbk').decode('gbk'))
