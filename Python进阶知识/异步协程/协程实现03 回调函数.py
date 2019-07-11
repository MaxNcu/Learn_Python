# -*- coding:utf-8 -*-
import asyncio
from functools import partial
# partial的功能是 固定函数参数，返回一个新的函数。你可以这么理解：
'''
from functools import partial
    def go(x,y):
        return x+y
    g = partial(go,y=2)
    print(g(1))
返回结果：3

    g = partial(go,x=5,y=2)
    print(g())
返回结果：7
    
'''
async def get_url_title(url):
    print('开始访问网站:{}'.format(url))
    await asyncio.sleep(2)
    print('网站访问成功')
    # 当这个协程函数快要结束返回值的时候，会调用下面的call_back函数
    # 等待call_back函数执行完毕后，才返回这个协程函数的值
    return 'success'

def call_back(future,url):
    # 注意这里必须要传递future参数，因为这里的future即代表下面的get_future对象
    print('检测网址:{}状态正常'.format(url))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # 创建一个事件循环

    get_future = loop.create_task(get_url_title('http://www.langzi.fun'))
    # 将一个任务注册到loop事件循环中

    get_future.add_done_callback(partial(call_back,url = 'http://www.langzi.fun'))
    # 这里是设置，当上面的任务完成要返回结果的时候，执行call_back函数
    # 注意call_back函数不能加上()，也就意味着你只能依靠partial方法进行传递参数

    loop.run_until_complete(get_future)
    # 等待任务完成
    print('获取结果:{}'.format(get_future.result()))
    # 获取结果
