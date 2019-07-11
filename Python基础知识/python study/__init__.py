#coding=utf-8


url = 'http://www.baidu.com'
dic_ = [url +'/'+ x.replace('\n','') for x in open(str(raw_input('Set Dir:'))).readlines()]
for x in dic_:print x