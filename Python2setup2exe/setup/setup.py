# -*- coding: utf-8 -*-  
from distutils.core import setup  
import py2exe  
includes = ["encodings", "encodings.*"]  
options = {"py2exe": {"compressed": 1, "optimize": 2, "includes": includes, "bundle_files": 1}}  
setup(  
 version = "1.7",  
 description = u"xie.will",  
 name = "FormatTable",  
 options = options,  
 zipfile = None,  
 console = [{"script": "yellow.py",  
            "icon_resources": [(1, u"logo.ico")]}])  
