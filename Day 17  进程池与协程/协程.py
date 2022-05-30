from gevent import monkey
from gevent import spawn, joinall
import time


from greenlet import greenlet  # 实现协程的包之一

"""任务一调用任务二.switch, 任务二调用任务一.switch
通过switch实现交替切换任务"""
# 所有的io行为进行打包
monkey.patch_all()
# 导入gevent负责管理的任务


"""协程是单线程实现并发，又称微线程
在单线程多任务时遇到IO就切换线程，可以降低单线程IO的时间，提高单线程的效率
协程可以把单线程的效率最大化"""

"""
2022.4.18
1.类里边的列表是可迭代对象，写了  __iter__ 后才是可迭代对象
for 循环来迭代是个死循环，调用迭代器next()函数
创建类的时候不传参更方便
isinstance(要判断的东西，要判断的类型)  : 可以判断一个东西的类型
next  遇到StopIteration /异常自动停止
a,b = b, b+a 先执行右边？ 经查证，确实是，准确的说是先把等号右边算完然后赋值  
无聊。本来左边的式子也不要计算，只做赋值用，跟我原本的理解没什么区别
可以用类去写迭代器和生成器，还没试过
没想到yield与协程还有爬虫有关
if 前面写了死循环,发生异常时执行return     return后面的信息.value 可以输出return后面的信息
send可以把东西传到生成器的yield，a所产生的结果通过send实现了修改，传输，不是赋值
send之后再next取值会在生成器中接着yield走
yield 可以不返回值
交替执行速度够快就是并发，闪电侠的影残留

进程，线程，生成器,greenlets,gevent
gevent.get_current()可以拿到当前函数的地址
gevent会自动判断当前任务是否为耗时任务，如IO,sleep等，不耗时就先执行完，耗时就切换任务
使用gevent中的sleep  :gevent.sleep
打补丁可以使gevent识别其它包的耗时任务



"""


async  def play(name):
    print('%s play 1' % name)
    time.sleep(5)
    print(('%s play 2' % name))


def eat(name):
    print('%s eat 1' % name)
    time.sleep(3)
    print('%s eat 2' % name)


g1 = spawn(play, '拳皇')
g2 = spawn(play, 'KADUOKE')
# #等待任务运行完
# g1.join()
# g2.join()
joinall([g1, g2])

print("主线程is over")
