import requests
import socket
import re
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

danger_port_list = [21, 22, 25, 53, 80, 110, 113, 135, 139, 143, 179, 199, 443, 445, 465, 514, 548, 554, 587, 646, 993, 995,
              1025, 1026, 1433, 1720, 1723, 2000, 3306, 3389, 5060, 5666, 5900, 6001, 8000, 8008, 8080, 8443, 8888,
              10000, 32768, 49152, 49154]

def get_open_port(ip,port):
    s = socket.socket()
    s.settimeout(5)
    try:
        print('Check ip : {} port : {}'.format(ip,port))
        s.connect((ip,int(port)))
        s.close()
        print('Connect Success!!')
        return port
    except Exception as e:
        s.close()
        pass


def scan_open_port(ip):
    res = []
    for port in danger_port_list:
        s = socket.socket()
        s.settimeout(5)
        try:
            s.connect((ip,port))
            res.append(port)
        except:
            pass
    return res

class Info_Scan:
    def __init__(self,url):
        self.url = url

    def Get_Title(self):
        title = 'TITLE NONE'
        try:
            r = requests.get(self.url,timeout=10)
            encoding = requests.utils.get_encodings_from_content(r.text)[0]
            content = r.content.decode(encoding,'replace')
            title = re.search('<title>(.*?)</title>',content,re.S|re.I).group(1)
        except:
            pass
        finally:
            return title
    def Get_Power(self):
        power = 'POWER NONE'
        try:
            r = requests.get(self.url,timeout=10)
            power = r.headers.get('server')
        except:
            pass
        finally:
            return power

    def Get_Ip(self):
        host = 'IP NONE'
        try:
            host = socket.gethostbyname(self.url.split('//')[1])
        except:
            pass
        return host

    def Get_Port(self):
        host = self.Get_Ip()
        if host != 'IP NONE':
            ports = scan_open_port(host)
        else:
            ports = ['THERE IS NO PORT OPEN']
        return ports

    def Get_Result(self):
        url = self.url
        title = self.Get_Title()
        power = self.Get_Power()
        ip = self.Get_Ip()
        print(title)
        print(power)
        print(ip)
        port =self.Get_Port()
        retult = (url,title,power,ip,port)
        return retult

if __name__ == '__main__':
    #r = Info_Scan('http://www.langzi.fun').Get_Result()
    #print(r)
    print(scan_open_port('118.24.11.235'))