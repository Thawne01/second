"""
GIL,global interpreter lock ,全局解释器锁
本质是一把互斥锁，效果等同于执行权限     互斥锁把多个任务共享数据修改由并发改为串行 代码运行拿到cpu的权限，然后把代码丢给解释器，最后在进程里面的线程运行
每个进程有一把GIL锁，所以多线程不可以并行，发挥不了多核的优势
但是遇到IO就释放GIL锁，可以并发
2.为何要有GIL
垃圾回收机制不是线程安全的
3.有了GIL，如何处理并发
"""

from threading import Thread
import time


def task(name):
    print('%s is running' % name)
    time.sleep(2)


if __name__ == '__main__':
    t1 = Thread(target=task, args=('线程1',))
    t2 = Thread(target=task, args=('线程2',))
    t3 = Thread(target=task, args=('线程3',))
    # 造线程非常快，不用开辟空间，所以子线程会在主线程之前运行
    t1.start()
    t2.start()
    t3.start()
    print('主线程')
