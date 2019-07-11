# -*- coding:utf-8 -*-
import abc
class magic(object,metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        return self + ':Run'

    @abc.abstractmethod
    def stop(self):
        return self + ':Stop'

a = magic
print(a.run('a'))
print(a.stop('a'))
print('-'*10)
class magics(magic):
    def run(self,name):
        return name + ':runnging'
    def stop(self):
        pass

b = magics()
print(b.run('浪子'))
