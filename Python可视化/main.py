# coding:utf-8
#import pyecharts
from pyecharts import Bar
bar = Bar('WWW.langzi.fun文章数量统计','这个只是二级标题')
bar.use_theme('light')
utctime = ['2018-1','2018-2','2018-3','2018-4','2018-5']
count_1 = [1,5,3,4,6]
count_2 = [10,55,53,24,16]
bar.add('文章数量',utctime,count_1,is_stack=True)
bar.add('评论数量',utctime,count_2,is_stack=True)
bar.render('2.html')
