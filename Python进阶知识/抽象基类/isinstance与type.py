# -*- coding:utf-8 -*-

class A:
    pass

class B(A):
    pass
c = A()
d = B()
print(type(B))
# 打印类B的类型：<class 'type'>
print(type(d))
# 打印实例化对象d的类型：<class '__main__.B'>
print(B)
# 打印类B：<class '__main__.B'>
print(d)
# 打印实例化对象d：<__main__.B object at 0x000001FD129C1860>
print(type(d) is B)
# 判断实例化对象d的类型是不是就是B
print(type(d) == A)
# print(issubclass(B,A))
# print(isinstance(B,A))
#print('-'*10)
print(B.__bases__ is type(c))
print(type(c))

# print(isinstance(c,A))
# print(isinstance(c,B))
# print(isinstance(d,A))
# print(isinstance(d,B))