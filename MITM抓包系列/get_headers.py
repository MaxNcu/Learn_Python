# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import mitmproxy
def response(flow: mitmproxy.http.HTTPFlow):
    #print(flow.request.headers)
    # Headers[(b'Host', b'www.syztfj.com'), (b'User-Agent', b'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'), (b'Accept', b'*/*'), (b'Accept-Language', b'zh-CN,zh;q=0.8,en-US;q=0.5,en;q
    # =0.3'), (b'Accept-Encoding', b'gzip, deflate'), (b'Referer', b'http://www.syztfj.com/css/stylelunbo_nei.css'), (b'Cookie', b'online_service_status=1; ASPSESSIONIDCQTTRCBC=HDPJBKAAAFJOACLEDEGCNDAF'), (b'DNT',
    # b'1'), (b'X-Forwarded-For', b'8.8.8.8'), (b'Connection', b'keep-alive')]

    #print(flow.request.host)
    # www.syztfj.com

    print(flow.request.query)
    # 访问网址 http://c.cnzz.com/core.php?web_id=1271804123&t=z ，返回的结果如下：
    # MultiDictView[('web_id', '1271804123'), ('t', 'z')]
    # 可以使用flow.request.query.keys()获取所有的键

