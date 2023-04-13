import threading, time
import serial
import string
import configs

class SerThread:
    def __init__(self):
        #初始化串口、blog文件名称
        self.my_serial = serial.Serial(
            configs.COM_PORT, configs.BAUD_RATES, timeout=1
        )
     
        self.alive = False
        self.waitEnd = None

        fname = time.strftime("%Y%m%d")#blog名称为当前时间
        # self.rfname='r'+fname #接收blog名称
        # self.sfname='s'+fname #发送blog名称
        self.thread_read= None
        self.thread_send=None      
             
 
    def waiting(self):
        # 等待event停止标志 
        if not self.waitEnd is None:
            self.waitEnd.wait()
 

    def start(self):
        #开串口以及blog文件 
        # self.rfile=open(self.rfname,'w')
        # self.sfile=open(self.sfname,'w')
        self.my_serial.open()
             
        if self.my_serial.isOpen():
            self.waitEnd = threading.Event()
            self.alive = True
            
            self.thread_read = threading.Thread(target=self.Reader)
            self.thread_read.setDaemon(True)
            
            self.thread_send=threading.Thread(target=self.Sender)
            self.thread_send.setDaemon(True)
            
            self.thread_read.start()
            self.thread_send.start()
            return True
        else:
            return False
 
   
    def Reader(self):
        while self.alive:
            try:
                n = self.my_serial.inWaiting()
                data=''
                if n:
                    data = self.my_serial.read(n).decode('utf-8')             
                    print ('recv'+' '+time.strftime("%Y-%m-%d %X")+' '+data.strip())
                    # print (time.strftime("%Y-%m-%d %X:")+data.strip(), file=self.rfile)
                    # print (time.strftime("%Y-%m-%d %X:") + data.strip())
                    if len(data)==1 and ord(data[len(data)-1])==113: #收到字母q，程序退出
                        break
            except Exception as ex:
                print (ex)
 
        self.waitEnd.set()
        self.alive = False
    
    def Sender(self):
        # time.sleep(2)
        while self.alive:
            try:
                snddata = input("input data:\n")
                self.my_serial.write(snddata.encode('utf-8'))
                print ('sent'+' '+ time.strftime("%Y-%m-%d %X"))
                # print (snddata,file=self.sfile)  
                
            except Exception as ex:
                print (ex)
        
        self.waitEnd.set()
        self.alive = False                   
                
        
 
    def stop(self):
        self.alive = False

        if self.my_serial.isOpen():
            self.my_serial.close()
        # self.rfile.close()
        # self.sfile.close()
            
 
if __name__ == '__main__':    
    ser = SerThread()
    try:
        if ser.start():
            ser.waiting()
            ser.stop()
        else:
            pass;            
    except Exception as ex:
        print (ex)
 
    if ser.alive:
        ser.stop()
 
    print ('End OK .');
    del ser; 