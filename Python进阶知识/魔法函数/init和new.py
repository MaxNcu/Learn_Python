# -*- coding:utf-8 -*-

class magic(object):
    def __init__(self,nums):
        self.nums = self.nums
        self.langzi = 'langzi'
        print '666'
        print 'init:' + self.nums

    def __new__(cls, nums):
        print nums
        # 这里打印出传递进来的数值
        cls.nums = nums+'BCDEFG'
        cls.langzi = '浪子'
        print 'new:'+cls.nums
        return object.__new__(cls)


a = magic('A')
print '-'*10
print a.langzi
print a.nums