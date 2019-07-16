# -*- coding: utf-8 -*-
# @Time    : 2018/8/4 0004 18:51
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : download_meizi.py
# @Software: PyCharm
# Python_Version: Python3
import sys
import requests
import threading
import os

def download(title,url):
    headers={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
                'Referer':'http://www.mzitu.com/zipai/'

    }
    if os.path.exists(title):
        pass
    else:
        os.mkdir(title)
        #Python2判断路径的编码，不同电脑编码都不一样
        #path = os.path.join(os.getcwd(), title.encode('utf-8')) if isinstance(os.getcwd(), unicode) else os.path.join(os.getcwd().encode('utf-8'),title.encode('utf-8'))
        path = os.path.join(os.getcwd(), title)
        for _id,_name in enumerate(url):
            try:
                name = path + '\\' + str(_id)+'.jpg'
                with open(name,'wb') as s:
                    try:
                        r = requests.get(_name,headers=headers,timeout=5)
                        print (str(_id),str(_name),r.status_code)
                        s.write(r.content)
                    except Exception as e:
                        print (e)
            except Exception as e:
                print (e)


download(title=title,url=url)
