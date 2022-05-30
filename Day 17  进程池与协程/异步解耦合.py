from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import os


def get(i):
    print('%s下载进程%s' % (os.getpid(), i))
    time.sleep(3)
    parse(i)


def parse(i):
    print('%s解析进程结果%s' % (os.getpid(), i))
    time.sleep(0.1)


if __name__ == '__main__':
    p = ProcessPoolExecutor(9)
    start_time = time.time()
    for i in range(9):
        fut = p.submit(get, i)
    p.shutdown(wait=True)
    print("主进程", time.time() - start_time)  # 3.51517653465271
    print('主进程', os.getpid())

"""这样其实get里面调用了parse函数，是耦合在一起的，数据不安全，要尽量达到高聚合低耦合
其实是一个进程保管了下载任务和解析任务，当它下载完后并没有去解析结果，而是在等待其它进程下载完再解析，资源被浪费了，花费的时间变长"""


def post(i):
    print('%s正在下载任务%s' % (os.getpid(), i))
    time.sleep(3)
    # parser(i)
    return i


def parser(i):
    i = i.result()
    print("%s正在解析结果%s" % (os.getpid(), i))
    time.sleep(0.1)


if __name__ == '__main__':
    ps = ProcessPoolExecutor(9)
    st_time = time.time()
    for i in range(9):
        ftr = ps.submit(post, i)
        ftr.add_done_callback(parse)  # 让进程下载完后自动触发parse任务
        """parse会在get完成后自动触发，接受一个future对象(来自于current.futures)，      就是从get任务返回的i(
        i已经变成了一个future对象)，那么parse任务就不缺参数可以运行了 """
    ps.shutdown(wait=True)  # 关闭进程池
    print('主进程', time.time() - st_time)  # 4.348678350448608
    print('主进程在这儿呢', os.getpid())

"""究极完全体0"""
from threading import Thread, current_thread


def fetch(i):
    print('%s下载线程%s' % (os.getpid(), i))
    time.sleep(3)
    return i


def decod(i):
    i = i.result()
    print('%s正在解析结果%s' % (current_thread().name, i))
    time.sleep(0.1)


if __name__ == '__main__':
    pr = ThreadPoolExecutor(9)
    ini_time = time.time()
    for i in range(9):
        fue = pr.submit(fetch, i)
        """添加一个任务回收，future.result()"""
        fue.add_done_callback(decod)
    pr.shutdown(wait=True)
    print('主线程', time.time() - ini_time)
    print('主线程', current_thread().name)
