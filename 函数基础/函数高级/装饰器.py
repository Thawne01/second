"""
一个特殊的闭包函数
定义：一个给其它函数添加功能的函数
软件的维护遵从开放封闭原则：
   软件一旦上线后对修改源代码是封闭的，对拓展功能是开放的

装饰器的原则：
  不修改被装饰对象的源代码
  不修改被装饰对象的调用方式
"""
# def muscling():
#     print('muscling')
#     running()
#
# def running():#被装饰函数
#     print("running")
#     # print('muscling')#修改了源代码
# running()
# muscling()#改变调用方式
#
#
# cod = '晨'
# def kas(name):
#
#     print('------------')
#     print(('我是%s'%name))
#     print('=============')
#
# kas(cod)
#
#
# def decorate(func):#等下要传入的kas,被装饰的函数
#     def new_kas(name):
#         print('我是装饰函数前面的coce')
#         func(name)
#         print('我是后面的code')
#     return new_kas
# #传参可以传变量名，值，函数名
# kas = decorate(kas)
# print((kas))
# kas(cod)
#
#
#
from  datetime import datetime
# print(datetime.now())
# n = 9000000



#时间装饰器
def time_de(func):
    def new_func(n):
        start = datetime.now()
        print('开始时间')
        func(n)
        end_t = datetime.now()
        print('结束时间')
        time1 = end_t - start
        print(('花费时间', time1))
    return new_func

@time_de
def for1(n):

    sum1 = 0
    for i in range(1, n+1):
        sum1 += i
    print(sum1)


# for1(n)
# for1 = time_de(for1)
lj = for1(5)



