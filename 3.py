import asyncio
import time

async def fun1():
    while True:
        # await asyncio.sleep(2)
        time.sleep(2)
        print('1')

async def fun2():
    while True:
        # await asyncio.sleep(2)
        time.sleep(3)
        print('22')

async def func(cur):
    count = 0
    while True:
        count += 1
        print(cur, count)
        time.sleep(2)
        if count == 5:
            break


async def main():
    task = asyncio.gather(func('1'), func('2'))
    print('hello')
        


asyncio.run(main())
