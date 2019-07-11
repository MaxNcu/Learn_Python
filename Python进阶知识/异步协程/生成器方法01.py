# -*- coding:utf-8 -*-
import requests
import re

def get_title(url):
    try:
        r = requests.get(url)
        title = re.search('<title>(.*?)</title>',r.content.decode(),re.I)
        return title.group(1)
    except:
        return '获取标题失败'

def get_urls():
    url1 = yield 'https://www.baidu.com'
    # 这样可以产出yield的值，并且能获取到传递进来的值，传递进来的值赋值给url1
    print(url1)

    yield 'http://www.langzi.fun'


gen = get_urls()
# 在调用send发送非None值之前，必须先启动生成器，启动方式有如下两种：
'''
1. url = gen.send(None)
2. url = next(gen)
这两种都能启动生成器函数，并且获取到yield的值
'''
url_1 = next(gen)
print(url_1)
print('-----------')
urls = (gen.send(get_title(url_1)))# send可以传递值到生成器内部，同时还能重启生成器到下一个yield的位置
print(urls)
# 传递值到生成器内部，这个时候生成器重启到下一个yield位置





# def gen_func():
#     yield 1
#     yield 2
#     yield 3
#
#
# if __name__ == '__main__':
#     gen = gen_func()
#     print(next(gen))
#     gen.close()
#     next(gen)  # gen_func中还有yield  再调用next就会报异常







