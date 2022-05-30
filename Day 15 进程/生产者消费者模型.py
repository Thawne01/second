"""
产生数据 与 处理数据
互不干涉，产生数据的一直产生数据，处理数据的一直处理数据，达到解耦合，提高工作效率
"""
import  time
import random
from multiprocessing import Process, Queue
def producer(name,food,q):
    for i in range(10):
        res = '%s%s'%(food, i)
        time.sleep(random.randint(1, 4))   #生产数据要时间‘
        q.put(res)
        print('厨师%s做好了%s'%(name, res))

def consumer(name, q):
    while True:
        res = q.get()
        #如果队列里面空了就退出
        if res is None:
            break
        time.sleep(random.randint(1, 4))
        print('骚女%s吃了%s'%(name, res))

if __name__ == '__main__':
    q =   Queue()
    #生产者
    p1 = Process(target=producer, args=('小嘴', '阴茎 ', q))
    p2 = Process(target=producer, args=('头部', '套弄 ', q))
    p3 = Process(target=producer, args=('舌尖', '马眼 ', q))
    #消费者
    c1 = Process(target=consumer, args=('蜜穴', q))
    c2 = Process(target=consumer, args=('粉臀', q))

    #开启进程
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()
    """要等厨师先做饭，然后才能吃，所以让生产者进程先执行完"""
    p1.join()
    p2.join()
    p3.join()
    #生产者生产完成,还生成一个多余的None 给消费者
    q.put(None)
    q.put(None)
    print('主进程')


