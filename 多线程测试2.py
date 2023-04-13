import threading
import time


def func(n_1, n_2):
    print('load', n_1)
    for i in range(n_1, n_2):
        global sum 
        sum += 1 / (i**2) * 6


t_start = time.time()
n_1 = 1
n_2 = 1000000000
seg = 10000000
sum = 0
thread_list = []
for i in range(n_1, n_2, seg):
    thread_ = threading.Thread(target=func(i, i+seg))
    # thread_.setDaemon(True)
    thread_.start()
    thread_list.append(thread_)
print(sum**0.5)
print(f'耗时{time.time() - t_start:.2f}秒')


t1 = time.time()
count = 0
for i in range(n_1, n_2):
    count += 1 / (i**2) * 6
print(sum**0.5)
print(count)
print(f'耗时{time.time() - t1:.2f}秒')
