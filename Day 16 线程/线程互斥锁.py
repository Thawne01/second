"""
线程互斥锁，和进程互斥锁含义差不多嘛，“互斥”意味着排斥，有了一个就不许其它的进来，从而保证串行而不是并发，
内存共享，引起混乱，加锁变有序  线程
访问文件共享 引起混乱 加锁有序访问文件 进程
"""

from threading import Thread, Lock
import time

mutex = Lock()  # 定义锁
n = 99


def task():
    global n
    mutex.acquire()  # 加锁
    temp = n
    """到此为止后面的99个线程都进来了，并且temp = 100，虽然共享内存，但是不安全"""
    time.sleep(0.1)
    n = temp - 1
    mutex.release()  # 完成计算释放锁


if __name__ == '__main__':
    t_1 = []
    start = time.time()
    for i in range(100):
        t = Thread(target=task)
        t_1.append(t)
        t.start()
    for t in t_1:
        t.join()
        print(n, time.time() - start)
