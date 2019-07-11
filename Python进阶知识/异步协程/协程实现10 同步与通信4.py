import asyncio
import functools


def set_event(event):
    print('开始设置事件')
    event.set()


async def test(name, event):
    print('{} 的事件未设置'.format(name))
    await event.wait()
    print('{} 的事件已设置'.format(name))


async def main(loop):
    event = asyncio.Event()
    # 声明事件
    print('事件是否设置: {}'.format(event.is_set()))
    loop.call_later(0.1, functools.partial(set_event, event))
    # 在0.1s后执行set_event()函数，对事件进行设置
    await asyncio.wait([test('e1', event), test('e2', event)])
    print('最终事件状态: {}'.format(event.is_set()))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
