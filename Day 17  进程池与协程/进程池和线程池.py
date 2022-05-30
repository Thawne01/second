"""
受制于计算机硬件，子进程和子线程不可能一直开，而且也浪费资源，所以进程池和线程池可以限制新开的线程或进程的数量，减少内存的浪费
提交任务的两种方式：
同步调用：完完整整地等代码运行完拿到结果再走下一个，任务状态是串行
异步调用：提交完一个任务后，遇IO换线程，执行下一个线程，任务状态是并发
"""
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import os
import random

def task(name):
    print("%s %sis running "%(name, os.getpid()))
    time.sleep(random.randint(1, 4))
    return 123

if __name__ == '__main':
    print('cpu', os.cpu_count())
    p = ProcessPoolExecutor(4)
    #只开四个进程的id
    # p.submit(task, '进程的pid')
    # p.submit(task, '进程的pid')
    # p.submit(task, '进程的pid')
    # p.submit(task, '进程的pid')
    # #再次开新的进程不需要开辟空间
    # p.submit(task, '进程的pid')
    # p.submit(task, '进程的pid')
    # for i in range(20):
    #     fut =  p.submit(task, ('进程的pid'))#有返回值
    #     print(fut)
    #     #同步调用
    #     print(fut.result())
    # print('主进程')


    result = []#存放结果
    for i in range(20):
        fut = p.submit(task,('进程的pid'))
        result.append(fut)
    p.shutdown()#关闭进程池入口，并原地等待所有任务运行完
    for t in result:
        print(t.result())


