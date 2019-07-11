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
from collections import Iterable,Iterator
reload(sys)
sys.setdefaultencoding('utf-8')

class weather(Iterator):
    # 天气迭代器，继承Iterator，使用next
    def __init__(self,citys):
        # 构造器  描述哪些城市
        self.citys = citys
        self.index = 0
        # 记录迭代的位置
    def getweather(self,city):
        r = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=" + city)
        data = r.json()['data']['forecast'][0]
        #print data
        return '%s:%s,%s'%(city,data['low'],data['high'])
    def next(self):
        if self.index == len(self.citys):
            # 当全部的城市加载完毕
            raise StopIteration
        city = self.citys[self.index]
        # 迭代出当前城市
        self.index +=1
        return self.getweather(city)
        # 返回出城市的气温信息

class weather1(Iterable):
    # 可迭代对象，继承Iterable，使用_iter__
    def __init__(self,city):
        self.city = city
        # 内部维护citys，为了传给Iter
    def __iter__(self):
        return weather(self.city)
        #可迭代接口，返回上面的weather

for x in weather1([u'北京','上海','南京','广州','深圳','长沙']):print x
