from multiprocessing import Process, current_process
import os
import time
""" tasklist |findstr r 可以查找所有的进程
    tasklist |findstr python
"""

#1.开启进程可以不传参
def kill():
    print("子进程%s正在运行"%current_process().pid)
    time.sleep(1.5)
    print("子进程%s就要结束了"%current_process().pid)
    return  None

if __name__ == '__main__':
    print("其实主进程一直在运行哦", current_process().pid)
    process1 = Process(target=kill)
    process2 = Process(target=kill)
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    print("主进程的最后一个操作，意味着主进程结束了", current_process().pid)
    print("---------------------------------------")

#2.os模块也可以拿到进程的pid
"""os.getpid()可以拿到当下进程的pid,   os,getppid()可以拿到当下进程的父进程的pid
"""
# def kill():
#     print("当下进程%s正在运行，它的父进程是%s"%(os.getpid(), os.getppid()))
#     time.sleep(10)
#     print("当下进程%s就要结束了，它的父进程是%s"%(os.getpid(), os.getppid()))
#
#
if __name__ == '__main__':
    print("其实主进程一直在运行", os.getpid())
    process1 = Process(target=kill)
    process2 = Process(target=kill)
    process2.start()
    process1.start()
    print("这是主进程%s最后一个操作,它的父进程是%s"%(os.getpid(), os.getppid()))
    print("-------------------------------------------------------")
#3.terminate()杀死进程，is_alive()判断进程是否存活
# def kill():
#     print("子进程{0}正在运行，它的父进程是{1}".format(os.getpid(), os.getppid()))
#     time.sleep(15)
#     print("子进程{0}就要运行完了，它的父进程是{1}".format(os.getpid(), os.getppid()))

if __name__ == '__main__':
    print("主进程{0}正在运行，他是由{1}创造出来的".format(os.getpid(), os.getppid()))
    jiba = Process(target=kill)
    #开启一个子进程
    jiba.start()
    print(jiba.name)#拿到进程的name
    #主动杀死进程,  需要一定时间
    jiba.terminate()
    time.sleep(0.1)
    #判断进程是否存活
    print(jiba.is_alive())
    print("主进程%s就要结束了"%os.getpid())
