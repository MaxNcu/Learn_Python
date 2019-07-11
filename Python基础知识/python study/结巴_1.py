# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 0023 16:00
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 结巴_1.py
# @Software: PyCharm
import sys
import jieba
import jieba.analyse
reload(sys)
sys.setdefaultencoding('utf-8')
# data_str='可你觉得孤独又能怎么样啊?你觉得孤独也不过是心情更差而已嘛。以前没什么人跟你说话，你觉得孤独，也还是没人跟你说话啊。'
# ## 精准匹配
# print '/'.join(jieba.cut(data_str,cut_all=False,HMM=True))
# ## 全文匹配
# print '/'.join(jieba.cut(data_str,cut_all=True,HMM=True))
# ## 搜索引擎模式
# print '/'.join(jieba.cut_for_search(data_str,HMM=True))
# ## 关键词提
# print '/'.join(jieba.analyse.extract_tags(data_str))
#
# data_strs='如果黑暗中的蛾子曾经体会过那么一点点光,它也不会不惜把整个世界都烧起来,只为了让自己暖和起来。'
# print '/'.join(jieba.analyse.extract_tags(data_strs))
# jieba.add_word('黑暗中的蛾子')
# print '/'.join(jieba.analyse.extract_tags(data_strs,topK=10))
#encoding=utf-8
