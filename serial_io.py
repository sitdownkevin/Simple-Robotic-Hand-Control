'''
@author: sitdownkevin
@date:   2023.4.14
'''
import serial
import time
import utils, config
import threading
import asyncio, websockets

class Kyle():
    def __init__(self) -> None:
        self.ser = None
        self.is_port_open = False
        self.thread_wait_stop = None
        self.thread_task = []
        self.msg_list = []

    def start(self, event):
        self.ser = serial.Serial(
            port=config.COM_PORT,
            baudrate=config.BAUD_RATES,
            timeout=1
        )

        if self.ser.isOpen():
            self.thread_wait_stop = threading.Event()
            self.is_port_open = True
            for task in [self.Reader, self.Sender, event]:
                task = threading.Thread(target=task)
                task.setDaemon(True)
                task.start()
                self.thread_task.append(task)
            return True
        else:
            print(time.strftime("%X") + f'{" #":4} 端口打开失败')
            return False


    def waiting(self):
        if not self.thread_wait_stop is None:
            self.thread_wait_stop.wait()


    def stop(self):
        if self.ser.isOpen():
            self.ser.close()


    def Sender(self):
        # if self.is_port_open:
        while True:
            if len(self.msg_list) > 0:
                msg = self.msg_list[0]
                if msg == 'q':
                    break
                self.msg_list = self.msg_list[1:]
                print(time.strftime("%X") + f'{" >":4} {msg}')
                self.ser.write(msg.encode())
                time.sleep(0.5)

        self.thread_wait_stop.set()
        # self.is_port_open = False


    def Reader(self):
        while self.is_port_open:
            try:
                if self.ser.inWaiting():
                    data = self.ser.readline().decode('utf-8')             
                    print(time.strftime("%X") + f'{" <":4} ' + data.strip())
                    if len(data)==1 and ord(data[len(data)-1])==113: 
                        # 收到字母q，程序退出
                        break
            except Exception as ex:
                print (ex)

        self.thread_wait_stop.set()


    # def WSServer(self):

    #     pass

if __name__ == "__main__":
    kyle = Kyle()
    if kyle.start():
        kyle.waiting()
        # kyle.stop()