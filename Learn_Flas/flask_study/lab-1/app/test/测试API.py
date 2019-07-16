# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 0017 21:13
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 测试API.py
# @Software: PyCharm
import sys
import requests,re
reload(sys)
sys.setdefaultencoding('utf-8')


def meizi(id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }
    url = 'http://www.mzitu.com/search/'+str(id)
    print 'try connect :'+url
    r = requests.get(url,headers=headers)
    print r.status_code
    print r.content
    rr = re.findall("data-original='(.*?)' /></a><span><a.*?href=\"(.*?)\" target=\"_blank\">(.*?)</a></span><span",r.content,re.S)
    print '----------'
    for x ,y,z in rr:
        print x,y,z
meizi('可爱')
