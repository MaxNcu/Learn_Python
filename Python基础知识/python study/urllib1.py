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
import urllib
import urllib2
reload(sys)
sys.setdefaultencoding('utf-8')
url = 'http://blog.csdn.net/lzy98'
req = urllib2.urlopen(url)
#print req.info()  #headers
#print ''.join([line for line in req.readlines()])



#url_get = 'http://www.puahome.com/bbs/forum.php?gid=37'
url1_get = 'http://www.puahome.com/bbs/forum.php'
def url_get():
    params = urllib.urlencode({'gid':'37'})
    print params
    req1 = urllib2.urlopen(str('?'.join([url1_get,'%s']))%params)
    print req1.info()
    print req1.getcode()    #状态吗
url_get()


page = urllib2.urlopen("http://example")
text = unicode(page.read(), "utf-8")
#query = PyQuery(text)