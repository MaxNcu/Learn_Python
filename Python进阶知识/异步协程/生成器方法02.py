# -*- coding:utf-8 -*-
def gene():
    for c in 'AB':
        yield c  #遇到yeild程序返回循环，下次从yeild后面开始。
    for i in range(3):
        yield i
if __name__=="__main__":
    print(list(gene()))#list内部会预激生成器


def gene():
    yield from 'ab'
    yield from range(3)
if __name__ == "__main__":
    print(list(gene()))


import requests
from collections import namedtuple
# 引入一个具名元组,可以后面实现一个简单的类。

Response = namedtuple("rs", 'url status')
# 对请求参数做一个格式化处理，后面通过获取属性即可。


# 子生产器
def fecth():
# 一个协程，通过requests模块可以发起网络请求。
    res=[]
    while 1:
        url = yield
        # main函数的发送的值绑定到这里的url上
        if url is None:
        # url为None即没有url的时候结束循环的。
            break
        req = requests.get(url)
        res.append(Response(url=url, status=req.status_code))
    return res

#委派生成器
def url_list(l, key):
    while 1:
    # 这个循环每次都会新建一个fetch 实例，每个实例都是作为协程使用的生成器对象。
        l[key] = yield from fecth()
    # url_list发送的每个值都会经由yield from 处理，然后传给fetch 实例。
    # url_list会在yield from表达式处暂停，等待fetch实例处理客户端发来的值。
    # fetch实例运行完毕后，返回的值绑定到l[key]  上。
    # while 循环会不断创建fetch实例，处理更多的值。

#调用方
def main():
    l = {}
    u = ["http://www.baidu.com", "http://www.cnblogs.com"]
    for index, url in enumerate(u):
        if index == 0:
            ul = url_list(l, index)
            next(ul)
            # 激活url_list生成器
        ul.send(url)
        # 把各个url以及其序列号index，
        # 传给url_list传入的值最终到达fetch函数中,
        # url_list并不知道传入的是什么，
        # 同时url_list实例在yield from处暂停。
        # 直到fetch的一个实例处理完才进行赋值。
    ul.send(None)
    # 关键的一步，
    # 把None传入url_list，传入的值最终到达fetch函数中，导致当前实例终止。
    # 然后继续创建下一个实例。
    # 如果没有ul.send(None)，那么fetch子生成器永远不会终止，
    # 因为ul.send()发送的值实际是在fetch实例中进行，
    # 委派生成器也永远不会在此激活，也就不会为l[key]赋值
    return l


if __name__ == '__main__':
    res = main()
    print(res)

