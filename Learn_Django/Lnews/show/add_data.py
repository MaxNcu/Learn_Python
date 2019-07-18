# coding:utf-8
import requests
requests.packages.urllib3.disable_warnings()
import re

import django
import os
import sys
pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,pathname)
sys.path.insert(0,os.path.abspath(os.path.join(pathname,'..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Lnews.settings")
django.setup()
from show.models import News_Data

def Get_Content_Of_Url(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        r = requests.get(url, headers=headers, verify=False, timeout=5)
        encoding = 'utf-8'
        try:
            encoding = requests.utils.get_encodings_from_content(r.text)[0]
        except:
            pass
        content = r.content.decode(encoding, 'replace')
        return (content, r.status_code)
    except Exception as e:
        return ('langzi', 404)

def Get_Title_Of_Content(content):
    if content[1] != 404:
        Url_Title_pattern = re.compile('<a href="(http.*?)" target="_blank">(.*?)</a>',re.I|re.S)
        res = re.findall(Url_Title_pattern,content[0].strip().replace('\n',''))
        return res[0:-1]


All_Urls = ['https://www.xj.hk/?index-{}.htm'.format(page) for page in range(1,18)]
for url in All_Urls:
    CONTENT = Get_Content_Of_Url(url)
    result = Get_Title_Of_Content(CONTENT)
    for r in result:
        print('URL:{}'.format(r[0]))
        print('TITLE:{}'.format(r[1].strip().lstrip()))
        try:
            News_Data.objects.create(user='langzi',title=r[1].strip().lstrip(),content=r[0])
        except:
            print('REPEAT DATA')