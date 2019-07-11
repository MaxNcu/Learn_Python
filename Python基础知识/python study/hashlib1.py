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
reload(sys)
sys.setdefaultencoding('utf-8')
import uuid
import hashlib
import base64
import time
mac=uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
mac_address = '%s:%s:%s:%s:%s:%s' % (mac[0:2],mac[2:4],mac[4:6],mac[6:8],mac[8:10],mac[10:])
print mac_address
md5 = hashlib.md5()
md5.update(mac)
md7 = md5.hexdigest()[::-1]
md8 = md7[2:6] + 'zhaohan'+md7[5:10]
sha1 = hashlib.sha256(md8).hexdigest()
sha2 = hashlib.md5(sha1[2:12]).hexdigest()[5:15]
yonghukey=sha2.replace('0','L').replace('5','O').replace('2','E')
print yonghukey
# md4 = mmd5[3:7]   #取md5zhongjian1
# md6 = mac_address.split(':',5)[3]
# md7 = mac_address.split(':',5)[1]
# diyihuihe = str(md4) + str(md7) + str(md6)
# print 'diyi:'+diyihuihe
# sha1 = hashlib.sha1(diyihuihe).hexdigest()
# dierhuihe = 'zhaohan' +str(sha1[6:14]) + 'zhaohan'
# base641 = base64.b64encode(dierhuihe)
# disanhuihe = (str(base641))
# yonghu = hashlib.md5(diyihuihe).hexdigest()
# yonghukey = yonghu[9:18]
# print 'YEY:' + str(yonghukey)

# md5 = hashlib.md5()
# md5.update('langzi')
# print md5.hexdigest()
# sha1 = hashlib.sha1()
# sha1.update('langzi')
# print sha1.hexdigest()
# list1 = [11,123]
# list2 = [2,3,5]
# req = requests.get(url='http://360.mafengwo.cn/robots.txt')
# md5 = hashlib.md5()
# md5.update(req.content)
# print md5.hexdigest()