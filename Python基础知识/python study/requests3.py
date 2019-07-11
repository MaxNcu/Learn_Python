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
import requests
import re
reload(sys)
sys.setdefaultencoding('utf-8')
'''
1 带参数的请求  GET方式 requests.get(url=url,params={'id':'12'})

2 表单数据提交 POST方式（在网上发布数据 论坛）
content-type application/x-www-form-urldecoded  
requests.post(url=url,data={'idxx':'123'})

3 json 参数提交
content-type application/json
requests.post(url=url,json={'idxx':'123'})


'''

#卸载req。get里面    stream=True 在罕见的情况下你可能想获取来自服务器的原始套接字响应
req = requests.get(url='https://www.douban.com/photos/album/84559192/')
print req.reason
r1 = re.findall('<img width="201" src="(.*?)" />',req.content)
i = 1
for x in r1:
    f1 = open(str(i) + '.jpg','wb')
    print x
    f1.write(requests.get(url=x).content)
    i+=1

