import threading
import time


class Kyle(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # 串口
        self.ser = None
        # 线程
        # self.thread_send = None
        # self.thread_read = None
        self.thread_event = None
        self.thread_list = []
        self.a = 10


    def start(self):
        # 打开串口
        pass
        # 打开串口开始read, send线程
        self.thread_event = threading.Event()
        # self.thread_read = threading.Thread(target=self.read)
        # self.thread_read.setDaemon(True)
        # self.thread_send = threading.Thread(target=self.send)
        # self.thread_send.setDaemon(True)
        for target in [self.send, self.read]:
            thread_ = threading.Thread(target=target)
            thread_.setDaemon(True)
            thread_.start()
            self.thread_list.append(thread_)

    def waiting(self):
        if not self.thread_event is None:
            self.thread_event.wait()
        pass

    def send(self):
        while True:
            time.sleep(1)
            self.a += 1
            print(f'{time.strftime("%X")} send {self.a}')
        pass


    def read(self):
        while True:
            time.sleep(2)
            self.a += 1
            print(f'{time.strftime("%X")} read {self.a}')
        pass

    def stop(self):
        pass

kyle = Kyle()
kyle.start()
kyle.waiting()