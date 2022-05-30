import json
import time,random
from multiprocessing import Process,Lock
# 查票可以并发 没有改数据
def search(name):
    with open('db.json','rt',encoding='utf-8')as f:
        dic = json.load(f)
    # 模拟查票时间
    time.sleep(1)
    print('%s查看到余票为%s'%(name,dic['count']))
# 购票应该串行 改了数据
def get(name):
    with open('db.json','rt',encoding='utf-8')as f:
        dic = json.load(f)
        # 先看下有没有票
    if dic['count']>0:
        # 有票模拟填信息，付款，提交数据给服务端
        dic['count']-=1
        # 其他的进程全部都进来了
        time.sleep(random.randint(1,3))
        # 重新写入
        with open('db.json', 'wt', encoding='utf-8')as f:
            json.dump(dic,f)
            print('%s购票成功'%name)
    else:
        print('%s查看到没有票了'%name)
# # 并发
# def task(name):
#     # 串行
#     search(name)
#
#     get(name)
def task(name,mutex):
    # 并发
    search(name)
    # 串行
    # 获取锁
    mutex.acquire()
    get(name)
    # 释放锁
    mutex.release()

# if __name__ == '__main__':
#     for i in range(10):
#         p = Process(target=task,args=('路人%s'%i,))
#         # 数据安全，是指读的时候无所谓，写的（改的）时候必须安全
#         #         # 写的时候是串行，读的时候并发
#         #  join只能将进程的任务整体变成串行
#         #         # 互斥锁可以局部串行
#         p.start()
#         p.join()

# 加锁
if __name__ == '__main__':
    mutex = Lock()
    for i in range(10):
        p = Process(target=task,args=('路人%s'%i,mutex))
        # 数据安全，是指读的时候无所谓，写的（改的）时候必须安全
        #         # 写的时候是串行，读的时候并发
        #  join只能将进程的任务整体变成串行
        #         # 互斥锁可以局部串行
        p.start()