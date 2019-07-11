# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
from docx import Document
from docx.shared import Inches
from docx.dml.color import ColorFormat
from docx.shared import Pt
from docx.shared import RGBColor
from docx.oxml.ns import qn
from docx.enum.style import WD_STYLE_TYPE

document = Document()

UserStyle1 = document.styles.add_style('UserStyle1', 1)
# 设置字体尺寸
UserStyle1.font.size = Pt(9)
# 设置字体颜色
UserStyle1.font.color.rgb = RGBColor(10,105,105)
#UserStyle1.font.color.rgb = RGBColor(0xff, 0xde, 0x00)
# 居中文本
UserStyle1.font.name = '仿宋'
UserStyle1._element.rPr.rFonts.set(qn('w:eastAsia'), '仿宋')

document.add_paragraph('正文','UserStyle1')

document.save('测试样式01.docx')