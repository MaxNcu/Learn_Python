# coding:utf-8
import os
fd = os.open('io3.txt',os.O_CREAT | os.O_RDWR) #创建 | 读写方式打开
n = os.write(fd,'hello word')
l = os.lseek(fd,0,os.SEEK_SET)
str1 = os.read(fd,5)
os.close(fd)

#os.listdir(path)
#os.listdir('./')   --常用--   列目录

os.access('io3.txt',os.R_OK)
#判断是否存在这个文件  R_OK读权限  W_OK写权限



#os.remove('io3.txt')
#os.rename('io3.txt','ioo.txt')  --常用-- 重命名文件或者文件夹


# mkdir(path,'name') --常用-- 创建目录   madir('test')
# rmdir(path) --常用-- 删除目录
#makedirs('text/test')  --常用-- 多级目录
#removedirs('text/test') --常用--


# os.path.exists(path)  --常用-- 当前目录是否存在
# os.path.isdir(s) --常用-- 是否存在一个目录
# os.path.isfile(s) --常用-- 是否存在一个文件
