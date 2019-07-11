# -*- coding:utf-8 -*-
import time
class readlines:
    def __init__(self,books):
        self.books = books
        self.index = 0

    def __next__(self):
        try:
            result = self.books[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

class readbooks:
    def __init__(self,books):
        self.books = open(books,'r').readlines()

    def __iter__(self):
        return readlines(self.books)

t1 = time.time()
for x in readbooks('a.txt'):
    pass
t2 = time.time()
print(t2 - t1)