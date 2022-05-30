# 搞线程啦
# 守护进程/线程  守护的是主进程/线程
import os
import time
from threading import Thread, active_count, current_thread
from multiprocessing import Process

"""
在内存中的程序叫进程
进程不负责运行代码
进程创建线程，线程执行程序

线程运行是无序的
线程 共享全局变量
"""

n = 100


def task():
    global n
    print("%s is running" % os.getpid())
    print('%s is done' % current_thread().name)
    n = 5
    time.sleep(3)


if __name__ == '__main__':
    t = Thread(target=task)  # 创建一个对象
    # 开启一个线程非常快，不用开辟新的空间
    t.start()  # 创建一个新的线程
    t.join()  # 等子线程运行完
    print(active_count())
    print("主线程%s" % os.getpid())
    print("主线程叫%s" % current_thread().name)
    print(n)
