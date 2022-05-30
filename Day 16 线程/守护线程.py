import os
import threading
from multiprocessing import Process
from threading import Thread
import time


def foo():
    print(123)
    time.sleep(5)
    print('end123')


def bar():
    print(456)
    time.sleep(3)
    print('end456')


if __name__ == '__main__':
    # 开子进程,创建进程开销大
    # t1 = Process(target=foo)
    # t2 = Process(target=bar)
    # t1.daemon = True
    # t1.start()
    # t2.start()
    # print('主进程', os.getpid())

    t1 = Thread(target=foo)
    t2 = Thread(target=bar)
    t1.daemon = True
    t1.start()
    t2.start()
    print('主线程', os.getpid())
    print(threading.enumerate())  # 统计线程数
    # 456线程还没有终结， 守护线程>主线程>普通线程
