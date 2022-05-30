"""
进程是一个程序运行的过程，包含了运行这个程序所有方面的所有资源
开启一个进程要：先向系统申请内存空间，然后将数据拷贝进cpu，最后由cpu执行
多进程擅长计算密集型，进程之间的空间数据是相互隔离、不共享的，内存是相互隔离的
"""
"""进程锁可以让一个进程先运行完，守护进程用来伴随另一个进程的死亡而死亡，所以这两个进程间有某种联系和需要的话可以考虑进程锁
   试试用“锁种”的概念理解进程锁,其实pycharm运行时当然会开启一个进程，子进程是在此进程的基础上开辟的，所以运行一个文件就会有一个主进程
"""
from multiprocessing import Process, current_process
import time
import random
def tuisuo(s):
    print("进程%d正在运行"%current_process().pid, s)
    time.sleep(random.randint(0, 4))
    print("等待了一会儿这个进程终于运行完了", s)

if __name__  == '__main__':
    process1 = Process(target=tuisuo, args=("柔若无骨",))
    #第二种传参方式
    process2 = Process(target=tuisuo, kwargs={'s': '柔若无'})
    print(process1)
    process1.start()#先.start()的子进程先开始运行
    process2.start()


    print("实际上主进程正在运行，只不过看不见而已")

#开启一个子进程时会先运行主进程，主进程运行到一定程度这时候子进程准备工作完成了，就开始运行子进程，
#主进程是隐形的，并没有表现出来，毕竟是在cpu后台运行嘛
#加了join()方法之后就会保证先运行完子进程再运行主进程
"""并发就是，实际上已经运行完了，只不过是过了一会儿再输出在屏幕上，由此有了“状态的保留”"""

