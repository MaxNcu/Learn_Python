# encoding:utf-8
from pyecharts import WordCloud

name = ['浪子','好帅啊','真的好帅啊','妈耶这么太帅了吧']
value = [15,10,9,3]

wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 100])
wordcloud.render("10.html")