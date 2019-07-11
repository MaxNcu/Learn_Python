# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 0018 21:48
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : sys模块.py
# @Software: PyCharm
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import sys
import time
## 获取系统的环境变量
print sys.path
## 获取系统的平台
print sys.platform
## 获取系统的编码
print sys.getdefaultencoding()
## 获取文件的编码格式(win-->mbcs,mac-->utf-8)
print sys.getfilesystemencoding()
## 设置系统的编码
sys.setdefaultencoding('utf-8')
## 更改打印样式
### sys.stdout.write()打印的数据并不会自动换行
# sys.stdout.write("hello")
# sys.stdout.write("hello \n")
# ### sys.stdin.readline( )会将标准输入全部获取
# a = raw_input('raw_input_name: ')
# print(a)
# print 'stdin_name: ',
# b = sys.stdin.readline()
# print(b)
# #因此如果在平时使用sys.stdin.readline( )获取输入的话，不要忘了去掉末尾的换行符，可以用strip( )函数去掉（sys.stdin.readline( ).strip('\n')）
# ## 清除当前线程所出现的当前的或最近的错误信息
# #sys.exc_clear()
# ## 退出程序
# #sys.exit()




from tqdm import tqdm
for i in tqdm(range(1,3601)):
    time.sleep(1)

## 外部传入参数
# import time
# def bar(num, total):
#     rate = num / total
#     rate_num = int(rate * 100)
#     r = '\r[%s%s]%d%%' % ("="*num, " "*(100-num), rate_num, )
#     sys.stdout.write(r)
#     sys.stdout.flush()
#
# if __name__ == '__main__':
#     for i in range(0, 101):
#         time.sleep(0.5)
#         bar(i, 100)
