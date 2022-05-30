"""
解决读取文件速度慢的问题，不需要锁
Inter Process Communication
multiprocessing模块支持两种形式：队列，管道。都是使用消息传递，共享内存空间
队列 = 管道+锁
"""
from multiprocessing import Queue
"""
先进先出，Queue(限制队列里的个数)
占用的内存
"""
q = Queue(3)#创建队列
q.put('啊啊大鸡巴哥哥操的人家太爽啦啊啊啊')
q.put('啊啊啊大鸡吧老公都快把人家子宫捅穿了啦！！！')
q.put('绝顶高潮带来的欲仙 欲死的享受和大肉棒不间断的光速抽插带来的致命的酥麻快感，已经让蒋馨茹的 大脑彻底短路。')
print('队列满了')
print("-----------------------")
#队列满了，再也塞不进去，相当于锁了
print(q.get())
print(q.get())
print(q.get())
#队列空了，阻塞等待加入，相当于锁了
print('队列空了')
