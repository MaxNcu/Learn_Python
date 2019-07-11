# -*- coding: utf-8 -*-
"""
__author__ = 'Langziyanqin'
__QQ__ = '982722261'
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from PIL import Image
import pytesseract
threshold = 140
from PIL import Image
im = Image.open('v9am.png')
imgry = im.convert('L')
#imgry.show()
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
#out.show()

tessdata_dir_config = r'--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR\tessdata"'
text = pytesseract.image_to_string(out,config=tessdata_dir_config)
#text = pytesseract.image_to_string(Image.open('v9am.png'),config=tessdata_dir_config)
print(text)
