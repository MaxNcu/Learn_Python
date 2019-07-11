# # coding:utf-8
# from docx import Document
# # 传入实例化对象，好比from flask import Flask
#
# document = Document()
# # 把对象实例化，好比app=Flask()
# document.add_paragraph('你好啊世界'.decode('utf-8'),'Title')
# # 写入内容，中文的话需要进行utf-8编码
# # 或者用unicode编码写入
# document.add_paragraph('hellw,word','Subtitle')
# document.add_paragraph(u'我是正文')
# document.add_paragraph(u'我也是正文')
# document.add_paragraph(u'难道我就不是了吗','Body Text')
# document.add_paragraph(u'你说呢','Normal')
#
# # add_paragraph 方法的第一个参数是段落的文字，第二个可选参数就是段落的样式。
# # 通过这个样式参数即可设置所添加段落的样式。如果不指定这个参数，则默认样式为『正文』
# # 比如 document.add_paragraph('我是标题'.decode('utf-8'),'title')
# # Title一级标题，Subtitle 二级标题,Heading n：n级标题,Normal：正文,Body Text 2正文
# # 注意首字母一定要大写
# document.save('demo.docx')
# # 注意，如果一个文正已经被系统打开后是无法再进行写入的
import time
a = str(time.strftime('%Y-%M-%D-%h-%m-%s',time.localtime()))
print a