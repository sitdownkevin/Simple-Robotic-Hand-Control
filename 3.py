import threading
import time

a = '5'

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_read = None
        self.thread_send = None
        self.stop_event = threading.Event()


    def start(self):
        self.thread_read = threading.Thread(target=self.read)
        self.thread_read.setDaemon(True)
        self.thread_send = threading.Thread(target=self.send)
        self.thread_send.setDaemon(True)

        self.thread_read.start()
        self.thread_send.start()

    def read(self):
        while not self.stop_event.is_set():
            print('hello')
            a = input('Type Here')
            time.sleep(1)
            if a == 'q':
                self.stop()
    
    def send(self):
        while True:
            print('hello')
            time.sleep(1)
            # print(not self.stop_event)

    def stop(self):
        self.stop_event.set()

if __name__ == "__main__":
    myThread = MyThread()
    myThread.start()

    if not myThread.stop_event is None:
        myThread.stop_event.wait()
        
    myThread.stop()