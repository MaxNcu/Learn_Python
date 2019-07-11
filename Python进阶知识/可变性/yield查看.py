# -*- coding:utf-8 -*-
def readbooks(f, newline):
    # f为传入的文件名，newline为分隔符
    buf = ""
    # 缓存，处理已经读出来的数据量
    while 1:
        while newline in buf:
            # 缓存中的数据是否存在分隔符
            pos = buf.index(newline)
            # 如果存在就找到字符的位置,比如0或者1或者2
            yield buf[:pos]
            # 暂停函数，返回缓存中的从头到字符的位置
            buf = buf[pos + len(newline):]
            # 缓存变成了，字符的位置到末尾
        chunk = f.read(2010 * 10)
        # 读取2010*10的字符
        if not chunk:
            # 已经读取到了文件结尾
            yield buf
            break
        buf += chunk
        # 加到缓存
with open('a.txt','r')as f:
    for line in readbooks(f,'\n'):
        print(line)
