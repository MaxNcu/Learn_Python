# -*- coding:utf-8 -*-

import subprocess  # line:2
import os  # line:3
import random  # line:4
import re  # line:5
import requests  # line:6
import time  # line:7
import multiprocessing  # line:8
from bs4 import BeautifulSoup  # line:9

requests.packages.urllib3.disable_warnings()  # line:11
os_python = os.path.join(os.getcwd(), 'lib\python.exe')  # line:13
os_sqlmap = os.path.join(os.getcwd(), 'lib\sqlmap\\')  # line:14
os_run = os_python + ' ' + os_sqlmap  # line:15


def writedata(O000O0O0O000000OO):  # line:18
    with open('log.txt', 'a+')as O00OOO0O0OO0O0O0O:  # line:19
        O00OOO0O0OO0O0O0O.write('-------------------------------------' + '\n')  # line:20
        O00OOO0O0OO0O0O0O.write(
            str(time.strftime('%Y-%m-%d:%H:%M:%S   ', time.localtime())) + O000O0O0O000000OO + '\n')  # line:21


REFERERS = ["https://www.baidu.com", "http://www.baidu.com", "https://www.google.com.hk", "http://www.so.com",
            "http://www.sogou.com", "http://www.soso.com", "http://www.bing.com", ]  # line:32
headerss = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]  # line:52
headers = {'User-Agent': random.choice(headerss),
           'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Cache-Control': 'max-age=0', 'referer': random.choice(REFERERS),
           'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3', }  # line:60


def get_links(OO00000OO00OO0OO0):  # line:63
    ""  # line:73
    if 'gov.cn' in OO00000OO00OO0OO0 or 'edu.cn' in OO00000OO00OO0OO0:  # line:74
        return 0  # line:75
    O0000O00O0OO0OO00 = OO00000OO00OO0OO0.split('//')[1].strip('/').replace('www.', '')  # line:76
    OO000OO0O00OOO00O = []  # line:77
    O00OO00OO00O0O000 = []  # line:78
    O0OOO00O000O00000 = []  # line:79
    OO00O0OO00O000OO0 = {}  # line:80
    OOO00O0OOO0O0OO0O = []  # line:81
    OO00O0OO00O000OO0['title'] = '网址标题获取失败'  # line:82
    O0OO00OO0OO00OOO0 = []  # line:83
    OOO0O0O000OO0O0OO = []  # line:84
    try:  # line:85
        O0O00000000OO0O0O = {'User-Agent': random.choice(headerss),
                             'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                             'Cache-Control': 'max-age=0', 'referer': random.choice(REFERERS),
                             'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3', }  # line:92
        OO0O00000O00OOO0O = requests.get(OO00000OO00OO0OO0, headers=O0O00000000OO0O0O, timeout=5).content  # line:93
        O0O0O000O000O00OO = BeautifulSoup(OO0O00000O00OOO0O, 'html.parser')  # line:94
        try:  # line:95
            OO00O0OO00O000OO0['title'] = O0O0O000O000O00OO.title.string  # line:96
        except Exception as O0OO0O000OOOOO00O:  # line:97
            writedata('[WARNING ERROR]' + str(O0OO0O000OOOOO00O))  # line:98
            try:  # line:99
                OO00O0OO00O000OO0['title'] = re.search('<title>(.*?)</title>', OO0O00000O00OOO0O, re.I | re.S).group(
                    1)  # line:100
            except Exception as O0OO0O000OOOOO00O:  # line:101
                writedata('[WARNING ERROR]' + str(O0OO0O000OOOOO00O))  # line:102
                pass  # line:103
        if OO00O0OO00O000OO0['title'] == '' or OO00O0OO00O000OO0['title'] == None:  # line:104
            OO00O0OO00O000OO0['title'] = '网址标题获取失败'  # line:105
        O0OOO0000OOO00OO0 = O0O0O000O000O00OO.findAll('a')  # line:106
        for O00OO0OOO0O00OOOO in O0OOO0000OOO00OO0:  # line:107
            _O0O0O000OOOO0O000 = O00OO0OOO0O00OOOO.get('href')  # line:108
            OOOO00O0O0OOOO000 = re.search('(javascript|:;|#)', str(_O0O0O000OOOO0O000))  # line:109
            OO0OOO0000O00O00O = re.search('.(jpg|png|bmp|mp3|wma|wmv|gz|zip|rar|iso|pdf|txt|db)',
                                          str(_O0O0O000OOOO0O000))  # line:110
            if OOOO00O0O0OOOO000 == None and OO0OOO0000O00O00O == None:  # line:111
                OO000OO0O00OOO00O.append(str(_O0O0O000OOOO0O000))  # line:112
            else:  # line:113
                pass  # line:114
        if OO000OO0O00OOO00O != []:  # line:115
            OO00000O0O0OO0OO0 = list(set(OO000OO0O00OOO00O))  # line:116
            for O000OO0OO00OO0000 in OO00000O0O0OO0OO0:  # line:117
                if '//' in O000OO0OO00OO0000 and 'http' in O000OO0OO00OO0000:  # line:118
                    if O0000O00O0OO0OO00 in O000OO0OO00OO0000:  # line:121
                        if '?' in O000OO0OO00OO0000 and '=' in O000OO0OO00OO0000:  # line:122
                            O00OO00OO00O0O000.append(O000OO0OO00OO0000)  # line:124
                        if '.html' in O000OO0OO00OO0000 or '.shtml' in O000OO0OO00OO0000 or '.htm' in O000OO0OO00OO0000 or '.shtm' in O000OO0OO00OO0000:  # line:125
                            if '?' not in O000OO0OO00OO0000:  # line:126
                                O0OOO00O000O00000.append(O000OO0OO00OO0000)  # line:128
                else:  # line:130
                    if '?' in O000OO0OO00OO0000 and '=' in O000OO0OO00OO0000:  # line:132
                        O00OO00OO00O0O000.append(OO00000OO00OO0OO0 + '/' + O000OO0OO00OO0000)  # line:134
                    if '.html' in O000OO0OO00OO0000 or '.shtml' in O000OO0OO00OO0000 or '.htm' in O000OO0OO00OO0000 or '.shtm' in O000OO0OO00OO0000:  # line:135
                        if '?' not in O000OO0OO00OO0000:  # line:137
                            O0OOO00O000O00000.append(OO00000OO00OO0OO0 + '/' + O000OO0OO00OO0000)  # line:138
            for OOOOOOOOO0O0000O0 in O0OOO00O000O00000:  # line:140
                try:  # line:141
                    O0OO000OO0OO0O000 = requests.head(url=OOOOOOOOO0O0000O0, headers=O0O00000000OO0O0O,
                                                      timeout=5).status_code  # line:142
                    if O0OO000OO0OO0O000 == 200:  # line:143
                        OOO0O0O000OO0O0OO.append(OOOOOOOOO0O0000O0)  # line:144
                except Exception as O0OO0O000OOOOO00O:  # line:145
                    writedata('[WARNING ERROR]' + str(O0OO0O000OOOOO00O))  # line:146
                    pass  # line:147
            for O00OO0O0O0O00O0O0 in O00OO00OO00O0O000:  # line:148
                try:  # line:149
                    O0O0000OOOOOOOOO0 = requests.head(url=O00OO0O0O0O00O0O0, headers=O0O00000000OO0O0O,
                                                      timeout=5).status_code  # line:150
                    if O0O0000OOOOOOOOO0 == 200:  # line:151
                        O0OO00OO0OO00OOO0.append(O00OO0O0O0O00O0O0)  # line:152
                except Exception as O0OO0O000OOOOO00O:  # line:153
                    writedata('[WARNING ERROR]' + str(O0OO0O000OOOOO00O))  # line:154
                    pass  # line:155
            if OOO0O0O000OO0O0OO == []:  # line:157
                pass  # line:158
            else:  # line:159
                for O00O00OO0O000000O in OOO0O0O000OO0O0OO:  # line:160
                    if O00O00OO0O000000O.count('/') > 3:  # line:161
                        OO0000000OOOO00OO = re.search('.*?/[0-9]\.', O00O00OO0O000000O)  # line:162
                        if OO0000000OOOO00OO == None:  # line:163
                            pass  # line:164
                        else:  # line:165
                            OOO00O0OOO0O0OO0O.append(O00O00OO0O000000O)  # line:166
                        if OOO00O0OOO0O0OO0O == []:  # line:167
                            OOO00O0OOO0O0OO0O.append(random.choice(OOO0O0O000OO0O0OO))  # line:168
                if OOO00O0OOO0O0OO0O == []:  # line:170
                    OO00O0OO00O000OO0['html_links'] = random.choice(OOO0O0O000OO0O0OO)  # line:171
                else:  # line:172
                    OO00O0OO00O000OO0['html_links'] = random.choice(OOO00O0OOO0O0OO0O)  # line:173
            if O0OO00OO0OO00OOO0 == []:  # line:175
                pass  # line:176
            else:  # line:177
                OO00O0OO00O000OO0['id_links'] = random.choice(O0OO00OO0OO00OOO0)  # line:178
        if OO00O0OO00O000OO0 == {}:  # line:179
            return None  # line:180
        else:  # line:181
            return OO00O0OO00O000OO0  # line:182
    except Exception as O0OO0O000OOOOO00O:  # line:183
        writedata('[WARNING ERROR]' + str(O0OO0O000OOOOO00O))  # line:184
        pass  # line:185
    return None  # line:186


def check(O00OO0O0O00O0O00O, O0000O0OOO0000OOO, O00OO0O0O00OO0OO0, title='获取标题失败'):  # line:189
    O0000O0OOO0000OOO = O0000O0OOO0000OOO.replace('^', '')  # line:190
    if '---' in O00OO0O0O00O0O00O:  # line:191
        if 'sqlmap was not able to fingerprint the back-end database management syste' not in O00OO0O0O00O0O00O:  # line:192
            try:  # line:193
                O0O000OO0OO0O00OO = re.search('---(.*?)---.*?\[INFO\] (the back-end DBMS is .*?)\[', O00OO0O0O00O0O00O,
                                              re.S)  # line:194
                O00O0OO0000OO00O0 = O0O000OO0OO0O00OO.group(1)  # line:195
                O0OOO00O0O00O0O00 = O0O000OO0OO0O00OO.group(2)  # line:196
                with open('result.txt', 'a+')as O00000OOO0O0O0O00:  # line:197
                    O00000OOO0O0O0O00.write(
                        '发现时间 : ' + str(time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())) + '\n')  # line:198
                    O00000OOO0O0O0O00.write('网站标题 : ' + title + '\n')  # line:199
                    O00000OOO0O0O0O00.write('注入网址 : ' + O0000O0OOO0000OOO + '\n')  # line:200
                    O00000OOO0O0O0O00.write('执行命令 : ' + O00OO0O0O00OO0OO0 + '\n')  # line:201
                    O00000OOO0O0O0O00.write(
                        O00O0OO0000OO00O0.replace('Parameter: ', '注入参数(方式) : ').replace('Type: ', '注入方式 : ').replace(
                            'Title: ', '注入标题 : ').replace('Payload: ', '注入攻击 : ') + '\n')  # line:204
                    if 'back-end DBMS' in O0OOO00O0O00O0O00:  # line:205
                        O00000OOO0O0O0O00.write(O0OOO00O0O00O0O00.replace('the back-end DBMS is ', '数据库类型 : ').replace(
                            'web server operating system: ', '服务器版本 : ').replace('web application technology: ',
                                                                                 '服务器语言 : ').replace('back-end DBMS: ',
                                                                                                     '数据库版本 : ') + '\n')  # line:210
                    else:  # line:211
                        O00000OOO0O0O0O00.write('\n' + '可能存在注入但被拦截,或者无法识别数据库版本' + '\n')  # line:212
                    print('---------------------------' + '\n')  # line:213
                    return 'INJ'  # line:214
            except Exception as O0O00OO0OOO00OOOO:  # line:215
                writedata('[WARNING ERROR]' + str(O0O00OO0OOO00OOOO))  # line:216
        else:  # line:217
            try:  # line:218
                O0O000OO0OO0O00OO = re.search('---(.*?)---.*?INFO\] (.*?)\[', O00OO0O0O00O0O00O, re.S)  # line:219
                O00O0OO0000OO00O0 = O0O000OO0OO0O00OO.group(1)  # line:220
                with open('result.txt', 'a+')as O00000OOO0O0O0O00:  # line:221
                    O00000OOO0O0O0O00.write(
                        '发现时间 : ' + str(time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())) + '\n')  # line:222
                    O00000OOO0O0O0O00.write('网站标题 : ' + title + '\n')  # line:223
                    O00000OOO0O0O0O00.write('注入网址 : ' + O0000O0OOO0000OOO + '\n')  # line:224
                    O00000OOO0O0O0O00.write('执行命令 : ' + O00OO0O0O00OO0OO0 + '\n')  # line:225
                    O00000OOO0O0O0O00.write(
                        O00O0OO0000OO00O0.replace('Parameter: ', '注入参数(方式) : ').replace('Type: ', '注入方式 : ').replace(
                            'Title: ', '注入标题 : ').replace('Payload: ', '注入攻击 : ') + '\n')  # line:228
                    O00000OOO0O0O0O00.write('\n' + '存在注入但无法识别数据库版本' + '\n')  # line:229
                    O00000OOO0O0O0O00.write('---------------------------' + '\n')  # line:230
                    return 'INJ'  # line:231
            except Exception as O0O00OO0OOO00OOOO:  # line:232
                writedata('[WARNING ERROR]' + str(O0O00OO0OOO00OOOO))  # line:233


def scan_level_0(OOOOO000OO0O0OO00, O0OO0O0OOOOO0OO0O):  # line:236
    OOOOO000OO0O0OO00 = OOOOO000OO0O0OO00.replace('&', '^&')  # line:237
    O00OOO00O00000O0O = os_run + 'sqlmap.py -u %s --technique B --batch --thread=10 --random-agent' % OOOOO000OO0O0OO00  # line:238
    print('Level 0 : ' + OOOOO000OO0O0OO00.replace('^', '').replace('*', ''))  # line:239
    writedata(O00OOO00O00000O0O)  # line:240
    try:  # line:241
        OOO00OO000000000O = subprocess.Popen(O00OOO00O00000O0O, shell=True, stdout=subprocess.PIPE)  # line:242
        OOO0O0OO0OO0000OO = OOO00OO000000000O.stdout.read()  # line:243
        writedata(OOO0O0OO0OO0000OO)  # line:244
        OO000OO000OOO00O0 = check(OOO0O0OO0OO0000OO, url=OOOOO000OO0O0OO00, common=O00OOO00O00000O0O,
                                  title=O0OO0O0OOOOO0OO0O)  # line:245
    except Exception as O00O000OOOOOOOOOO:  # line:246
        writedata('[WARNING ERROR]' + str(O00O000OOOOOOOOOO))  # line:247
        pass  # line:248
    finally:  # line:249
        OOO00OO000000000O.terminate()  # line:250
        return OO000OO000OOO00O0  # line:251


def scan_level_1(O000OOO000OOOOOO0, O0O000OO00O0O0OO0):  # line:253
    O000OOO000OOOOOO0 = O000OOO000OOOOOO0.replace('&', '^&')  # line:254
    OOOO00OO000O0O00O = os_run + 'sqlmap.py -u %s --batch --thread=10 --random-agent' % O000OOO000OOOOOO0  # line:255
    print('Level 1 : ' + O000OOO000OOOOOO0.replace('^', '').replace('*', ''))  # line:256
    writedata(OOOO00OO000O0O00O)  # line:257
    try:  # line:258
        OO0OOO000OOO0OO00 = subprocess.Popen(OOOO00OO000O0O00O, shell=True, stdout=subprocess.PIPE)  # line:259
        OOOO00OO0000O00O0 = OO0OOO000OOO0OO00.stdout.read()  # line:260
        writedata(OOOO00OO0000O00O0)  # line:261
        OOOOOO0000O000O00 = check(OOOO00OO0000O00O0, url=O000OOO000OOOOOO0, common=OOOO00OO000O0O00O,
                                  title=O0O000OO00O0O0OO0)  # line:262
    except Exception as O0OO000O0O0O000O0:  # line:263
        writedata('[WARNING ERROR]' + str(O0OO000O0O0O000O0))  # line:264
        pass  # line:265
    finally:  # line:266
        OO0OOO000OOO0OO00.terminate()  # line:267
        return OOOOOO0000O000O00  # line:268


def scan_level_2(O0OOOO0OOOOOOO0OO, OOOOO00O0OOO000OO):  # line:271
    OOO00OO0OOO0OOO0O, O0OO0OOOOO000O000 = O0OOOO0OOOOOOO0OO.split('?')[0], O0OOOO0OOOOOOO0OO.split('?')[1]  # line:272
    OOO00OO0OOO0OOO0O = OOO00OO0OOO0OOO0O.replace('&', '^&')  # line:273
    O0OO0OOOOO000O000 = O0OO0OOOOO000O000.replace('&', '^&')  # line:274
    OOO0O0000O0O00O00 = os_run + "sqlmap.py -u {} --cookie {} --level 2 --batch --thread=10 --random-agent".format(
        OOO00OO0OOO0OOO0O, O0OO0OOOOO000O000)  # line:276
    print('Level 2 : ' + O0OOOO0OOOOOOO0OO.replace('^', '').replace('*', ''))  # line:277
    O00000000OO000OO0 = os_run + "sqlmap.py -u {} --data {} --level 2 --batch --thread=10 --random-agent".format(
        OOO00OO0OOO0OOO0O, O0OO0OOOOO000O000)  # line:278
    writedata(O00000000OO000OO0)  # line:279
    writedata(OOO0O0000O0O00O00)  # line:280
    try:  # line:282
        OOOOOO000OO0O0OO0 = subprocess.Popen(OOO0O0000O0O00O00, shell=True, stdout=subprocess.PIPE)  # line:283
        O0OOOOOOOOOOO0O00 = OOOOOO000OO0O0OO0.stdout.read()  # line:284
        writedata(O0OOOOOOOOOOO0O00)  # line:285
        OO0O00000O0OOO000 = check(O0OOOOOOOOOOO0O00, url=O0OOOO0OOOOOOO0OO, common=OOO0O0000O0O00O00,
                                  title=OOOOO00O0OOO000OO)  # line:286
    except Exception as O0OO0OO0OO00O0O0O:  # line:287
        writedata('[WARNING ERROR]' + str(O0OO0OO0OO00O0O0O))  # line:288
        pass  # line:289
    finally:  # line:290
        OOOOOO000OO0O0OO0.terminate()  # line:291
        if OO0O00000O0OOO000 == 'INJ':  # line:292
            return OO0O00000O0OOO000  # line:293
    try:  # line:295
        OOOOOO000OO0O0OO0 = subprocess.Popen(O00000000OO000OO0, shell=True, stdout=subprocess.PIPE)  # line:296
        O0OOOOOOOOOOO0O00 = OOOOOO000OO0O0OO0.stdout.read()  # line:297
        writedata(O0OOOOOOOOOOO0O00)  # line:298
        OO0O00000O0OOO000 = check(O0OOOOOOOOOOO0O00, url=O0OOOO0OOOOOOO0OO, common=O00000000OO000OO0,
                                  title=OOOOO00O0OOO000OO)  # line:299
    except Exception as O0OO0OO0OO00O0O0O:  # line:300
        writedata('[WARNING ERROR]' + str(O0OO0OO0OO00O0O0O))  # line:301
        pass  # line:302
    finally:  # line:303
        OOOOOO000OO0O0OO0.terminate()  # line:304
        return OO0O00000O0OOO000  # line:305


def scan_level_3(O0O00000000000O0O, O0OO000O00OO0000O):  # line:308
    O0O00000000000O0O = O0O00000000000O0O.replace('&', '^&')  # line:309
    OO00OOO00OO00OO00 = os_run + 'sqlmap.py -u %s --batch --tamper space2comment.py --thread=10 --random-agent' % O0O00000000000O0O  # line:310
    print('Level 3 : ' + O0O00000000000O0O.replace('^', '').replace('*', ''))  # line:311
    writedata(OO00OOO00OO00OO00)  # line:312
    try:  # line:313
        O0O00OOO000O00000 = subprocess.Popen(OO00OOO00OO00OO00, shell=True, stdout=subprocess.PIPE)  # line:314
        O00O00OOOO0O0O0O0 = O0O00OOO000O00000.stdout.read()  # line:315
        writedata(O00O00OOOO0O0O0O0)  # line:316
        O00O0OO000000O000 = check(O00O00OOOO0O0O0O0, url=O0O00000000000O0O, common=OO00OOO00OO00OO00,
                                  title=O0OO000O00OO0000O)  # line:318
    except Exception as O0OOOO000OOOOO0OO:  # line:319
        writedata('[WARNING ERROR]' + str(O0OOOO000OOOOO0OO))  # line:320
        pass  # line:321
    finally:  # line:322
        O0O00OOO000O00000.terminate()  # line:323
        return O00O0OO000000O000  # line:324


def scan_level_4(O00O0O0O0O0000000, OOOOO0O0O000O000O):  # line:327
    O0OO0O00OO0OO00OO, OOOOOO0OO000O00OO = O00O0O0O0O0000000.split('?')[0], O00O0O0O0O0000000.split('?')[1]  # line:328
    O0OO0O00OO0OO00OO = O0OO0O00OO0OO00OO.replace('&', '^&')  # line:329
    OOOOOO0OO000O00OO = OOOOOO0OO000O00OO.replace('&', '^&')  # line:330
    OO0OOOO0OOO00OO00 = os_run + "sqlmap.py -u {} --cookie {} --level 2 --tamper space2comment.py --batch --thread=10 --random-agent".format(
        O0OO0O00OO0OO00OO, OOOOOO0OO000O00OO)  # line:332
    print('Level 4 : ' + O00O0O0O0O0000000.replace('^', '').replace('*', ''))  # line:333
    O0OO000000O00O00O = os_run + "sqlmap.py -u {} --data {} --level 2 --tamper space2comment.py --batch --thread=10 --random-agent".format(
        O0OO0O00OO0OO00OO, OOOOOO0OO000O00OO)  # line:335
    writedata(OO0OOOO0OOO00OO00)  # line:336
    writedata(O0OO000000O00O00O)  # line:337
    try:  # line:339
        OO00O0OO0O00OO00O = subprocess.Popen(OO0OOOO0OOO00OO00, shell=True, stdout=subprocess.PIPE)  # line:340
        OO0OO000OO0OO00O0 = OO00O0OO0O00OO00O.stdout.read()  # line:341
        writedata(OO0OO000OO0OO00O0)  # line:342
        O0O0OOOOOO00OOOO0 = check(OO0OO000OO0OO00O0, url=O00O0O0O0O0000000, common=OO0OOOO0OOO00OO00,
                                  title=OOOOO0O0O000O000O)  # line:344
    except Exception as OOO00O0O0O0O00O0O:  # line:345
        writedata('[WARNING ERROR]' + str(OOO00O0O0O0O00O0O))  # line:346
        pass  # line:347
    finally:  # line:348
        OO00O0OO0O00OO00O.terminate()  # line:349
        if O0O0OOOOOO00OOOO0 == 'INJ':  # line:350
            return O0O0OOOOOO00OOOO0  # line:351
    try:  # line:353
        OO00O0OO0O00OO00O = subprocess.Popen(O0OO000000O00O00O, shell=True, stdout=subprocess.PIPE)  # line:354
        OO0OO000OO0OO00O0 = OO00O0OO0O00OO00O.stdout.read()  # line:355
        writedata(OO0OO000OO0OO00O0)  # line:356
        O0O0OOOOOO00OOOO0 = check(OO0OO000OO0OO00O0, url=O00O0O0O0O0000000, common=O0OO000000O00O00O,
                                  title=OOOOO0O0O000O000O)  # line:357
    except Exception as OOO00O0O0O0O00O0O:  # line:358
        writedata('[WARNING ERROR]' + str(OOO00O0O0O0O00O0O))  # line:359
        pass  # line:360
    finally:  # line:361
        OO00O0OO0O00OO00O.terminate()  # line:362
        return O0O0OOOOOO00OOOO0  # line:363


def scan_level_5(OOOO00O0OO00OOO0O, O000O0OO0000OO000):  # line:366
    OOOO00O0OO00OOO0O = OOOO00O0OO00OOO0O.replace('&', '^&')  # line:368
    O000O00O000O0OO00 = os_run + 'sqlmap.py -u {} --batch --tamper space2comment.py --delay 2 --time-sec=15 --timeout=20  --level 5 --thread=10 --random-agent'.format(
        OOOO00O0OO00OOO0O)  # line:370
    print('Level 5 : ' + OOOO00O0OO00OOO0O.replace('^', '').replace('*', ''))  # line:371
    writedata(O000O00O000O0OO00)  # line:372
    try:  # line:374
        O00OOOO0O0O00OOO0 = subprocess.Popen(O000O00O000O0OO00, shell=True, stdout=subprocess.PIPE)  # line:375
        OOO0OOOO0O0000O00 = O00OOOO0O0O00OOO0.stdout.read()  # line:376
        writedata(OOO0OOOO0O0000O00)  # line:377
        OO000OO0OOOO000O0 = check(OOO0OOOO0O0000O00, url=OOOO00O0OO00OOO0O, common=O000O00O000O0OO00,
                                  title=O000O0OO0000OO000)  # line:379
    except Exception as O000000000O00OOOO:  # line:380
        writedata('[WARNING ERROR]' + str(O000000000O00OOOO))  # line:381
        pass  # line:382
    finally:  # line:383
        O00OOOO0O0O00OOO0.terminate()  # line:384
        return OO000OO0OOOO000O0  # line:385


def scan_html(O0OOO0O0O0OO00000, O00O0O0O0O000OO00, OO00O000O00O0O00O):  # line:388
    OO0OOOOOO00O0O000 = O0OOO0O0O0OO00000.replace('.htm', '*.htm').replace('.shtm', '*.shtm')  # line:389
    O0000O0O00O0OO000 = OO0OOOOOO00O0O000.replace('&', '^&')  # line:390
    if OO00O000O00O0O00O == 1 or OO00O000O00O0O00O == 2 or OO00O000O00O0O00O == 0:  # line:391
        OO0O0OOOOO0O00O00 = os_run + 'sqlmap.py -u {} --batch --thread=10 --random-agent'.format(
            O0000O0O00O0OO000)  # line:392
        if OO00O000O00O0O00O == 1:  # line:393
            print('Level 1 : ' + O0000O0O00O0OO000.replace('^', '').replace('*', ''))  # line:394
        if OO00O000O00O0O00O == 2:  # line:395
            print('Level 2 : ' + O0000O0O00O0OO000.replace('^', '').replace('*', ''))  # line:396
        if OO00O000O00O0O00O == 0:  # line:397
            print('Level 0 : ' + O0000O0O00O0OO000.replace('^', '').replace('*', ''))  # line:398
    if OO00O000O00O0O00O == 3 or OO00O000O00O0O00O == 4:  # line:400
        OO0O0OOOOO0O00O00 = os_run + 'sqlmap.py -u %s --batch --tamper space2comment.py --thread=10 --random-agent' % O0000O0O00O0OO000  # line:401
        if OO00O000O00O0O00O == 3:  # line:402
            print('Level 3 : ' + O0000O0O00O0OO000.replace('^', '').replace('*', ''))  # line:403
        else:  # line:404
            print('Level 4 : ' + O0000O0O00O0OO000.replace('^', '').replace('*', ''))  # line:405
    if OO00O000O00O0O00O == 5 or OO00O000O00O0O00O == 6:  # line:406
        OO0O0OOOOO0O00O00 = os_run + 'sqlmap.py -u {} --batch --tamper space2comment.py --delay 2 --time-sec=15 --timeout=20  --level 5 --thread=10 --random-agent'.format(
            O0000O0O00O0OO000)  # line:408
        print('Level 5 : ' + O0000O0O00O0OO000.replace('^', '').replace('*', ''))  # line:409
    writedata(OO0O0OOOOO0O00O00)  # line:410
    try:  # line:412
        OO00OO00000O00OO0 = subprocess.Popen(OO0O0OOOOO0O00O00, shell=True, stdout=subprocess.PIPE)  # line:413
        O0O0OO00O00OO0000 = OO00OO00000O00OO0.stdout.read()  # line:414
        writedata(O0O0OO00O00OO0000)  # line:415
        check(O0O0OO00O00OO0000, url=O0000O0O00O0OO000, common=OO0O0OOOOO0O00O00, title=O00O0O0O0O000OO00)  # line:417
    except Exception as OOOO0O0O0OO0OOOOO:  # line:418
        writedata('[WARNING ERROR]' + str(OOOO0O0O0OO0OOOOO))  # line:419
        pass  # line:420
    finally:  # line:421
        OO00OO00000O00OO0.terminate()  # line:422


def get_url_sql(O0OOO0O0OO00O0OO0, level=1):  # line:425
    OO00O0O0OO000OO0O = get_links(O0OOO0O0OO00O0OO0)  # line:426
    if OO00O0O0OO000OO0O == None:  # line:427
        pass  # line:428
    else:  # line:429
        if 'html_links' in OO00O0O0OO000OO0O.keys():  # line:430
            scan_html(OO00O0O0OO000OO0O['html_links'].replace(' ', ''), OO00O0O0OO000OO0O['title'], level)  # line:431
        if 'id_links' in OO00O0O0OO000OO0O.keys():  # line:432
            if level == 0:  # line:433
                scan_level_0(OO00O0O0OO000OO0O['id_links'].replace(' ', ''), OO00O0O0OO000OO0O['title'])  # line:434
            if level == 1:  # line:435
                scan_level_1(OO00O0O0OO000OO0O['id_links'].replace(' ', ''), OO00O0O0OO000OO0O['title'])  # line:436
            if level == 2:  # line:437
                scan_level_2(OO00O0O0OO000OO0O['id_links'].replace(' ', ''), OO00O0O0OO000OO0O['title'])  # line:438
            if level == 3:  # line:439
                scan_level_3(OO00O0O0OO000OO0O['id_links'].replace(' ', ''), OO00O0O0OO000OO0O['title'])  # line:440
            if level == 4:  # line:441
                scan_level_4(OO00O0O0OO000OO0O['id_links'].replace(' ', ''), OO00O0O0OO000OO0O['title'])  # line:442
            if level == 5:  # line:443
                scan_level_5(OO00O0O0OO000OO0O['id_links'].replace(' ', ''), OO00O0O0OO000OO0O['title'])  # line:444
            if level == 6:  # line:445
                O000O0OOOOO0O00O0 = scan_level_1(OO00O0O0OO000OO0O['id_links'].replace(' ', ''),
                                                 OO00O0O0OO000OO0O['title'])  # line:446
                if O000O0OOOOO0O00O0 != None:  # line:447
                    return O000O0OOOOO0O00O0  # line:448
                OO00O00O00O0OO0O0 = scan_level_2(OO00O0O0OO000OO0O['id_links'].replace(' ', ''),
                                                 OO00O0O0OO000OO0O['title'])  # line:449
                if OO00O00O00O0OO0O0 != None:  # line:450
                    return OO00O00O00O0OO0O0  # line:451
                OO0OO0O00OO0OO00O = scan_level_3(OO00O0O0OO000OO0O['id_links'].replace(' ', ''),
                                                 OO00O0O0OO000OO0O['title'])  # line:452
                if OO0OO0O00OO0OO00O != None:  # line:453
                    return OO0OO0O00OO0OO00O  # line:454
                O000O000O0O000O00 = scan_level_4(OO00O0O0OO000OO0O['id_links'].replace(' ', ''),
                                                 OO00O0O0OO000OO0O['title'])  # line:455
                if O000O000O0O000O00 != None:  # line:456
                    return O000O000O0O000O00  # line:457
                OO0O00OOOOOOOOO0O = scan_level_5(OO00O0O0OO000OO0O['id_links'].replace(' ', ''),
                                                 OO00O0O0OO000OO0O['title'])  # line:458
                if OO0O00OOOOOOOOO0O != None:  # line:459
                    return OO0O00OOOOOOOOO0O  # line:460


if __name__ == '__main__':  # line:463
    multiprocessing.freeze_support()  # line:464
    print('''

             _                           _
            | |                         (_)
            | |     __ _ _ __   __ _ _____
            | |    / _` | '_ \ / _` |_  / |
            | |___| (_| | | | | (_| |/ /| |
            |______\__,_|_| |_|\__, /___|_|
                                __/ |      Langzi_SQL_INJECTION
                               |___/       Version:3.7
                                           Datetime:2019-03-09

    ''')  # line:477
    print('''

        Description:
            Langzi_SQL_INJECTION v3.7版本是一款批量检测SQL注入漏洞的自动化工具
            对采集导入网址根据设置扫描等级进行全自动化扫描检测生成漏洞报告
            通过SQLMAP提供的API进行实现注入检测，扫描结果可百分百完全复现
            支持伪静态注入，cookie注入，post注入，加载绕过WAF的Tamper检测注入
            适用与6-80岁年龄段人群使用，简单，便捷，批量，自动生成检测结果

        扫描等级:
            level 0 : 仅仅使用BOOL类型的盲注检测
            level 1 : 使用多种类型判断注入方式
            level 2 : 支持cookie注入与post注入方式
            level 3 : 调用目录下绕过安全狗Tamper脚本检测
            level 4 : 调用Tamper绕过WAF加测cookie注入与post注入
            level 5 : 加载时间延迟与Tamper高风险等级注入
            level 6 : 调用0-5所有级别进行注入，直到成功完成注入检测

        Tips:    
            无法对GOV-EDU进行检测
            在WIN 7 下不兼容运行
            运行目录不能存在中文字符

    ''')  # line:501
    time.sleep(8)  # line:502
    New_start = input(('把采集的url文本拖拽进来:'))  # line:503
    levels = int(input(('设置扫描等级(0/1/2/3/4/5/6):')))  # line:504
    countss = int(input(('设置扫描进程数(2-36):')))  # line:505
    p = multiprocessing.Pool(countss)  # line:506
    list_ = list(set([OOOOOOO000O000000.replace('\n', '') if OOOOOOO000O000000.startswith(
        'http') else 'http://' + OOOOOOO000O000000.replace('\n', '') for OOOOOOO000O000000 in
                      open(New_start, 'r').readlines()]))  # line:509
    for x in list_:  # line:510
        if 'gov.cn' in x:  # line:511
            os._exit(0)  # line:512
        if 'edu.cn' in x:  # line:513
            os._exit(0)  # line:514
    for x in list_:  # line:516
        p.apply_async(get_url_sql, args=(x, levels))  # line:518
    p.close()  # line:519
    p.join()  # line:520
    print('浪子哥哥提醒您，这次任务扫完了哦，快去看看抓到了几个漏洞吧~')  # line:521
    time.sleep(300)  # line:522
    time.sleep(300)  # line:523
    time.sleep(300)  # line:524
    time.sleep(300)  # line:525
    time.sleep(300)  # line:526
    time.sleep(300)  # line:527
    time.sleep(300)  # line:528
