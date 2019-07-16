# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 0020 17:49
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : hahaha.py
# @Software: PyCharm
import sys
import requests,re
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://www.jieju.cn'
try:
    cms_title = '获取网站标题失败'
    r_cms_top = requests.get(url=url, timeout=5)
    if r_cms_top.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(r_cms_top.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = r_cms_top.apparent_encoding
        encode_content = r_cms_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
        cms_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
            '</title>', '')
    elif r_cms_top.encoding == 'GB2312':
        encodings = requests.utils.get_encodings_from_content(r_cms_top.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = r_cms_top.apparent_encoding
        encode_content = r_cms_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
        cms_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
            '</title>', '')
    elif r_cms_top.encoding == 'gb2312':
        encodings = requests.utils.get_encodings_from_content(r_cms_top.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = r_cms_top.apparent_encoding
        encode_content = r_cms_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
        cms_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
            '</title>', '')
    elif r_cms_top.encoding == 'GBK':
        encodings = requests.utils.get_encodings_from_content(r_cms_top.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = r_cms_top.apparent_encoding
        encode_content = r_cms_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
        cms_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
            '</title>', '')
    elif r_cms_top.encoding == 'gbk':
        encodings = requests.utils.get_encodings_from_content(r_cms_top.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = r_cms_top.apparent_encoding
        encode_content = r_cms_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
        cms_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
            '</title>', '')
    else:
        cms_title = re.search('<title>(.*?)</title>', r_cms_top.content, re.S).group().replace('<title>',
                                                                                               '').replace(
            '</title>', '')
except:
    try:
        cms_title = re.search('<title>(.*?)</title>', r_cms_top.content, re.S).group().replace('<title>',
                                                                                               '').replace(
            '</title>', '')
    except:
        cms_title = '暂时无法获取网站标题'

print cms_title