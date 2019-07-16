# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 0002 7:49
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : meizi.py
# @Software: PyCharm
import sys
import requests
import re
reload(sys)
sys.setdefaultencoding('utf-8')

def meizi(id):
    headerss = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }
    headers = {'Content-Type':'html/text'}
    r = requests.get(url=str('http://www.mzitu.com/search/' + str(id)),headers=headerss)
    rr = re.findall("</a><span><a.*?href=\"(.*?)\" target=\"_blank\">(.*?)</a></span><span",r.content,re.S)
    list_dir=[]
    for x,y in rr:
        img_logo = re.search('<img src="(.*?)" alt=',requests.get(x).content).group().replace('<img src="','').replace('" alt=','')
        list_dir.append((img_logo,x,y))
    return list_dir

meizi('可爱')