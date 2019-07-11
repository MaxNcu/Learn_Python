# -*- coding:utf-8 -*-
import asyncio

async def get_url_title(url):
    print('开始访问网站:{}'.format(url))
    await asyncio.sleep(2)
    print('网站访问成功')
    return 'success'

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # 使用gather方法传递任务获取结果
    group1 = asyncio.ensure_future(get_url_title('http://www.langzi.fun'))
    loop.run_until_complete(asyncio.gather(group1))
    print(group1.result())

    # 使用wait方法
    # tasks = [get_url_title('http://www.langzi.fun')for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))

    # # 使用gather方法实现分组导入(方法1)
    # group1 = [get_url_title('http://www.langzi.fun')for i in range(3)]
    # group2 = [get_url_title('http://www.baidu.com')for i in range(5)]
    # loop.run_until_complete(asyncio.gather(*group1,*group2))
    # # 这种方法会把两个全部一次性导入
    #
    # # 使用gather方法实现分组导入(方法2)
    # group1 = [get_url_title('http://www.langzi.fun')for i in range(3)]
    # group2 = [get_url_title('http://www.baidu.com')for i in range(5)]
    # group1 = asyncio.gather(*group1)
    # group2 = asyncio.gather(*group2)
    # #group2.cancel() 取消group2任务
    # loop.run_until_complete(asyncio.gather(group1,group2))
    # # 这种方法会先把group1导入，然后导入group2

    # 使用gather方法传递任务获取结果
    group1 = asyncio.ensure_future(get_url_title('http://www.langzi.fun'))
    loop.run_until_complete(asyncio.gather(group1))
    print(group1.result())
