# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 0022 10:24
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : os模块_1.py
# @Software: PyCharm
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

## 查看当前操作系统名称(win-->nt,linux-->posix)
print os.name

## 查看系统环境变量
print os.environ

## 打印目录下所有文件，当前目录的话加上点，或者使用别的路径
print os.listdir('.')
### 出现乱码的话，使用编码再解码一下即可
for x in os.listdir('.'):print x.decode('gbk').encode('utf-8')

## 打印当前路径
print os.getcwd()

## 跟换路径,演示切换到D盘
print os.chdir('D:\\')

# ## 创建文件夹
# ### 创建单个文件夹
# os.mkdir('dir')
# ### 在文件夹中创新的文件夹
# os.makedirs('dir1/dir2')
#
# ## 递归删除空的文件夹，如果有文件就不删除
# os.removedirs('dir1\dir2')
#
# ## 删除文件
# os.remove('1.py')
#
# ## 重命名文件夹或者文件
# os.rename('2.txt','2-1.txt')
#
# ## 判断文件或者文件夹是否存在
# os.path.exists('2.txt')
#
# ## 路径与文件名组合
# print os.path.join('D:\\','dir1')
#
# ## 获取文件的大小
# print os.path.getsize('2.txt')
#
# # 高级用法
# ## 常规列出目录下的所有文件并统计文件数
# import os,sys
# def listdir(dir,file):
#     file.write(dir + '\n')
#     fielnum = 0
#     list = os.listdir(dir)
#     #列出目录下的所有文件和目录
#     for line in list:
#         filepath = os.path.join(dir,line)
#         if os.path.isdir(filepath):
#             #如果filepath是目录，则再列出该目录下的所有文件
#             myfile.write('   ' + line + '\\'+'\n')
#             for li in os.listdir(filepath):
#                 myfile.write('     '+li + '\n')
#                 fielnum = fielnum + 1
#         elif os.path:
#             #如果filepath是文件，直接列出文件名
#             myfile.write('   '+line + '\n')
#             fielnum = fielnum + 1
#     myfile.write('all the file num is '+ str(fielnum))
# dir = raw_input('please input the path:')
# myfile = open('list.txt','w')
#
# ## 使用os.walk把给定的目录下的所有目录和文件遍历出来。
# #方法：os.walk(path),遍历path，返回一个对象，他的每个部分都是一个三元组,('目录x'，[目录x下的目录list]，目录x下面的文件)
# import os
# def walk_dir(dir,fileinfo,topdown=True,onerror=None):
#     for root, dirs, files in os.walk(dir, topdown):
#         for name in files:
#             print(os.path.join(name))
#             fileinfo.write(os.path.join(root,name) + '\n')
#         for name in dirs:
#             print(os.path.join(name))
#             fileinfo.write('  ' + os.path.join(root,name) + '\n')
# dir = raw_input('please input the path:')
# fileinfo = open('list.txt','w')
# walk_dir(dir,fileinfo)

# ## 筛选文件,统计子目录的大小
# import os
# from os.path import getsize,join
# for root,dirs,files in os.walk(r'D:\\python3'):
#     print root
#     print sum(getsize(join(root,name))for name in files)
#     # 因为getsize的时候，传入的name是相对的并不是完整的路径，使用join加在一起
#     if 'txt' in dirs:
#         # 如果存在txt目录，就删除该目录
#         dirs.remove('txt')
print os.popen('ipconfig').read()
os.path.isfile('')
os.path.isdir()
