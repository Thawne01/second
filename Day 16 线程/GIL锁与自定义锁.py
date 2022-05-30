"""
如果说锁是权限，那么同时使用GIL锁和自定义锁就相当于假面骑士铠武需要两个锁种才能开启变身，此时线程才会运行
"""
from threading import Thread, Lock
import time

mutex = Lock()
n = 99


def task():
    # 1.第一个线程抢到了GIL锁
    # 4.第二个线程抢到了线程1释放的GIL锁，但由于缺乏自定义锁如仍不能运行
    global n
    # 2.第一个线程抢到了自定义锁
    # 5.第二个线程卡在了自定义锁这里
    # 7.第二个线程抢到了自定义锁
    mutex.acquire()
    temo = n
    # 3.遇到IO，第一个线程释放GIL锁，但仍然有自定义锁
    time.sleep(0.1)
    n = temo - 1
    # 6.线程1运行完自定义锁里的代码，释放自定义锁
    mutex.release()
    print(n, )


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
