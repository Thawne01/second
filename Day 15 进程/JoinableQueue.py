"""
其实joinableQueue也是一种队列，只不过有task_done 功能更完善, 就是'join able',可以用join的Queue
"""
import time
from multiprocessing import Process, JoinableQueue

def producer(name, food, q):
    for i in range(10):
        res = '%s%s'%(food , i)
        time.sleep(3) #生产数据需要时间
        q.put(res)
        print('厨师%s做好了饭菜%s'%(name, res))

def consumer(name,q):
    while True:
        #等待队列里面有数据
        res = q.get()
        time.sleep(3)
        print('肉唇%s吃了%s'%(name, res))
        #每次完成队列取一次，放入q.join(),取干净了那么q.join()运行完
        q.task_done()
if __name__ == '__main__':
     st_time = time.time()
     q = JoinableQueue()
     #生产者
     p1 = Process(target=producer, args=('大鸡巴哥哥', '肉穴', q))
     p2 = Process(target=producer, args=('中鸡巴哥哥', '乳沟', q))
     p3 = Process(target=producer, args=('小鸡巴哥哥', '后庭', q))
     #消费者
     c1 = Process(target=consumer, args=('方洁', q))
     c2 = Process(target=consumer, args=('徐丹', q))
     #把消费者变成守护进程
     c1.daemon = True
     c2.daemon = True
     p1.start()
     p2.start()
     p3.start()
     c1.start()
     c2.start()

     #等待生产者生产数据
     p1.join()
     p2.join()
     p3.join()
     #task_done 给q.join()发信号

     q.join()
     #消费者吃完最后两个之后程序就运行完了，用守护进程的方式杀死消费者
     print('主进程', time.time()-st_time)

