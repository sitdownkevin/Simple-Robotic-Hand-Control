import serial
import time
import asyncio

import configs
from utils import encode

time_delay = 2.2

class Kyle:
    def __init__(self, com_port=configs.COM_PORT, baud_rates=configs.BAUD_RATES):
        self.in_connect = False
        self.ser = serial.Serial(com_port, baud_rates)

    def connect(self, timeout=10):
        print(f'Kyle ## 尝试连接')
        count = 0
        t1 = time.time()
        while not self.in_connect:
            time.sleep(1) # 尝试时间间隔1秒
            t2 = time.time()
            count += 1
            print(f'Kyle ## 第{count}次连接 经过{(t2 - t1):.2f}秒')
            # 超时
            if t2 - t1 > timeout:
                print('Kyle ## 连接超时')
                break
            # 收到消息
            while self.ser.in_waiting:
                data_raw = self.ser.readline()
                data = data_raw.decode()[:-2] # 去除'\n'
                if data == 'Connected@UNO':
                    print(f'Kyle <= {data}')
                    print('Kyle ## 连接成功')
                    self.in_connect = True
                    break
                else:
                    print(f'Kyle <= {data}')
                    print('Kyle ## 错误连接信息')


    def send_msg(self, msg=None):
        if msg == None:
            msg = input('msg: ')
        if not self.in_connect: return 
        print(f"Kyle ## 发送消息 {msg}")
        self.ser.write(msg.encode(encoding="utf-8"))
        time.sleep(time_delay)
        self.listen_port()

    def listen_port(self):
        print(self.ser.in_waiting)
        while self.ser.in_waiting > 0:
            data = self.ser.readline().decode()[:-2]
            print(data)

data = [2, 4, 5, 2, 4, 5, 10000]

def main():
    kyle = Kyle()
    kyle.connect()

    for cmd in data:
        kyle.send_msg(encode(cmd))



if __name__ == "__main__":
    main()
