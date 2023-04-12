import serial
import configs

import utils
import time

import asyncio

ser = serial.Serial(configs.COM_PORT, configs.BAUD_RATES)

def send(msg):
    time.sleep(5)
    ser.write(msg.encode())
    print(f'send: {msg}')

async def listen(cur):
    while True:
        # asyncio.sleep(1)
        time.sleep(1)
        if ser.in_waiting == 0:
            print('No msg')
            continue
        else:
            data = ser.readline().decode()[:-2]
            print(data)

async def main():
    tasks = asyncio.gather(listen(3))
    
    send("eudd")
    

if __name__ == "__main__":
    asyncio.run(main())

