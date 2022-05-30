"""
互斥锁的目的是让进程间的数据互通，访问同一个文件。但是多个进程同时访问一个文件必然会引起错乱，所以需要加锁。之所以是“互斥”，是因为当有一个进程访问文件后会产生
排斥其它进程访问该文件的效果，从而确保有序。必需释放锁才能获取下一个锁
用文件共享数据：1.速度慢2.要有互斥锁
串行和并发是一种运行状态
什么是“耦合”？
"""
from multiprocessing import Process, Lock
import json
import time
import random

#字典定义错·了，很搞心态,,俩小时了

#定义读取数据的函数
def sec(name):
    with open('db.json', 'rt', encoding='utf-8')as f:
        data_dict = json.load(f)
        time.sleep(1)  #查票需要一定时间
        #dic_va = int(data_dict['count'])
        print("%s查到通往寒山寺的车票还有%s张"%(name, data_dict['count']))

#定义购票，也就是写数据的函数，应该串行
def get(name):
    with open('db.json', 'rt', encoding='utf-8')as f:
        data_dic = json.load(f)  #load是加载出来
        #dic_va = int(data_dic['count'])
    if data_dic['count'] >0:
        data_dic['count'] -= 1   #有票的话就买票
       # data_dic = str(dic_va)
        time.sleep(random.randint(1, 4))
        #重新写入数据
        with open('db.json', 'wt', encoding='utf-8')as f:
            json.dump(data_dic, f)
            print("%s抢到票了"%name)
    else:
        print('%s看到没有票，失望地会回家了'%name)

#写互斥锁。获取锁，释放锁
def task(name, mutex):
    #读取数据要并发
    sec(name)

#     #写数据要串行
    mutex.acquire()#获取互斥锁
    get(name)
    mutex.release()#释放锁

if __name__ == '__main__':
    mutex = Lock()  # 创建自定义锁对象
    for i in range(10):
        p = Process(target=task, args=('假面骑士%s'%i, mutex))
        #为了确保数据安全，任何人都可以读取数据，但写入数据的时候只能一个一个来
        #              读数据是并发，写入数据是串行
        #join 只能整个任务变串行，用join方法读取数据的时候不能实现并发，所以有互斥锁
        p.start()
        