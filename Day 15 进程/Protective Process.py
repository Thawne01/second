from multiprocessing import Process, current_process
import os
import time
"""
   守护进程是一个子进程，伴随主进程的结束而结束
"""
def authotize(king):
    print("子进程{0}正在运行，它的父进程是{1}".format(os.getpid(), os.getppid()))
    time.sleep(3)
    print("子进程{0}就要运行完了，它的父进程是{1}".format(os.getpid(), os.getppid()))

# #定义主程序的入口
if __name__ == '__main__':
    print("主进程正在运行哦！", os.getpid())
    task1 = Process(target=authotize, args=("云升",))
    #将子进程task1声明为守护进程,先声明在开启子进程
    task1.daemon = True
    task1.start()
    time.sleep(2.9)#主进程还有0.1秒结束，子进程被迫结束         如果是4秒，那么子进程可以运行完
    print("主进程就要结束了,守护进程也要结束了")
