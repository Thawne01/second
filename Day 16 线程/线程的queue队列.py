"""
线程是数据共享的，但是锁使得效率变低，队列可以提升效率
"""
import queue
from threading import Thread, active_count
import time


# q = queue.Queue(3)#限制队列里线程的个数,超过这个数会报错,  放进去的时候会阻塞，输出的时候报错
# q.put(1)
# q.put(2)
# q.put(3)
# print('-------------------')
# q.put(4)
#
#
# print(q.get())
# print(q.get())
# print(q.get())
# print('--------------------')
# print(q.get())

def producer(name, food, q):
    for i in range(10):
        res = '%s%s' % (food, i)
        time.sleep(3)  # 生产时间
        q.put(res)
        print('厨师%s生成了%s' % (name, res))


def consumer(name, q):
    while True:
        # 订单没了，但是还在等，需要条件判断终结线程
        res = q.get()
        if res is None:
            if active_count() == 2:
                print(time.time() - start)
            break
        time.sleep(3)
        print('吃货%s吃了%s' % (name, res))


if __name__ == '__main__':
    start = time.time()
    q = queue.Queue(3)
    # 生产者线程
    p1 = Thread(target=producer, args=('大海', '包子', q))
    p2 = Thread(target=producer, args=('肉唇', '精液', q))
    p3 = Thread(target=producer, args=('黑森林', '扇贝', q))
    # 消费者
    c1 = Thread(target=consumer, args=('小萝莉', q))
    c2 = Thread(target=consumer, args=('欲女', q))

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()
    # 等生产者生产完成
    p1.join()
    p2.join()
    p3.join()
    # 给消费者None 判断终结线程
    q.put(None)
    q.put(None)
    print('主线程')
