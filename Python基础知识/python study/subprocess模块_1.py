# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 0022 12:48
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : subprocess模块_1.py
# @Software: PyCharm
import sys
import subprocess
reload(sys)
sys.setdefaultencoding('utf-8')

subprocess.call('whoami')
subprocess.check_call('whoami')
