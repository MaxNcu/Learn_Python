# -*- coding:utf-8 -*-
# __author__:langzi
# __blog__:www.langzi.fun
# !/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import getpass
import psutil
import time
import logging


def getCPUState(interval=1):
    ''' function of Get CPU State '''
    cpuCount = psutil.cpu_count()
    cpuPercent = psutil.cpu_percent(interval)
    return ("Logic CPU: %s; CPU: %s%%" % (str(cpuCount), str(cpuPercent)), str(cpuPercent))
    pass


def getMemoryState():
    ''' function of GetMemory '''
    phymem = psutil.virtual_memory()
    usedmem = int(phymem.used / 1024 / 1024)
    totalmem = int(phymem.total / 1024 / 1024)
    phymemPercent = "{:.2f}".format(float(usedmem / totalmem * 100))
    return ("Memory used: %sM; Memory total: %sM; Memory percent: %s%%" % (
    str(usedmem), str(totalmem), str(phymemPercent)))
    pass


def getDiskState():
    ''' function of disk state '''
    diskinfo = psutil.disk_usage('/')
    disktotal = int(diskinfo.total / 1024 / 1024 / 1024)
    diskused = int(diskinfo.used / 1024 / 1024 / 1024)
    diskfree = int(diskinfo.free / 1024 / 1024 / 1024)
    return ("Disk total: %sG; Disk used: %sG; Disk free: %sG" % (str(disktotal), str(diskused), str(diskfree)))
    pass


def getProcessState():
    ''' function of proscess state '''
    pid = psutil.pids()
    for k, i in enumerate(pid):
        try:
            proc = psutil.Process(i)
            print(k, i, "%.2f%%" % (proc.memory_percent()), "%", proc.name(), proc.exe())
        except psutil.AccessDenied:
            print("psutil.AccessDenied")
    pass

# for pnum in psutil.pids():
#     p = psutil.Process(pnum)
#     print ("进程名 %-20s  内存利用率 %-18s 进程状态 %-10s 创建时间 %-10s "% (p.name(), p.memory_percent(), p.status(),  p.create_time()))
import datetime
print ("系统启动时间: %s" % datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))

net = psutil.net_io_counters()
bytes_sent = '{0:.2f} Mb'.format(net.bytes_recv / 1024/1024)
bytes_rcvd = '{0:.2f} Mb'.format(net.bytes_sent / 1024/1024)
print ("网卡接收流量 %s 网卡发送流量 %s" % (bytes_rcvd, bytes_sent))


def main():
    cpus = getCPUState()
    cpu = cpus[0]
    print(cpu)
    mem = getMemoryState()
    disk = getDiskState()
    print(mem)
    print(disk)

    # logging.basicConfig(filename="memory.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s",
    #                     filemode='w')
    # while 1:
    #     cpus = getCPUState()
    #     cpu = cpus[0]
    #     mem = getMemoryState()
    #     disk = getDiskState()
    #     processInfoList = getAllProcessInfo()
    #     outputInfo = [cpu, mem, disk, "#Username\tPid\tVms\tRss\tCpu\tStatus\tTime\tCMD",
    #                   "======================================================================"] + processInfoList
    #     logging.info("\n" + "\n".join(outputInfo) + "\n")
    #     time.sleep(30)
    #     pass


if __name__ == '__main__':
    main()
