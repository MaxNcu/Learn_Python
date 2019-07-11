# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 0023 18:03
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 词云-1.py
# @Software: PyCharm
import sys
from wordcloud import WordCloud
reload(sys)
sys.setdefaultencoding('utf-8')
wordcloud = WordCloud(background_color="white",width=1000, height=860, margin=2).generate()
wc = WordCloud(font_path=font_path,  # 设置字体
               background_color="white",  # 背景颜色
               max_words=2000,  # 词云显示的最大词数
               mask=back_coloring,  # 设置背景图片
               max_font_size=100,  # 字体最大值
               random_state=42,
               width=1000, height=860, margin=2,# 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
               )
https://blog.csdn.net/fontthrone/article/details/72782971