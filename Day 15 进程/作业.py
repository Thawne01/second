"""
1.守护进程，“守护”者，意味着一旦被守护的人死亡自己也将死亡。在进程里，守护进程伴随着被守护进程的终结而终结，常常用于某种情况下主进程结束了而子进程还没结束，这时候
杀死子进程就节省了资源，而且任务也已经完成了
2.通过文件处理数据，一来因为要访问文件，读取数据，写入数据啥的，比较费时间，二来为了确保有序访问文件加上了锁，这也使得通过文件处理数据烦了不少
"""
import time
from multiprocessing import Process, JoinableQueue



def producer(name,food,q):
    for i in range(10):
        res = '%s%s'%(food, i)
        time.sleep(3)
        q.put(res)
        print('厨师%s生产了好吃的%s'%(name, res))

def consumer(name,q):
    while True:
        res = q.get()
        time.sleep(3)
        print("消费者%s吃了%s"%(name, res))
        q.task_done()
if __name__ == '__main__':
    st_time = time.time()
    q = JoinableQueue()
    #for i in range(10):一不小心循环开了进程
    p1 = Process(target=producer, args=('zcc', '鱼肉香菇', q))
    p2 = Process(target=producer, args=('zzl', '京酱肉丝', q))
    p3 = Process(target=producer, args=('zzn', '糖醋', q))
    c1 = Process(target=consumer, args=('方洁', q))
    c2 = Process(target=consumer, args=('徐丹', q))
    c1.daemon = True
    c2.daemon = True
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()


    p1.join()
    p2.join()
    p3.join()

    q.join()
    print('主进程')