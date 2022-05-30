"""
 闭：该函数是一个内部函数
 包：该内部的函数名字在外部被引用
 函数的定义嵌套函数的定义
"""
def outer():
    print('externer function is running')
    def inner():
        print('inner function is running')
    return inner#返回inner的内存地址   加括号是运行inner()
#执行outer(),inner被定义
inner = outer()
print(inner)
inner()
#不规范操作，没说不可以
outer()()


"""
参数为函数传值
"""
def fu(x, y):
    print(x, y)
fu(4, 6)
"""
闭包  为函数体传值  每次传入相同的参数
"""
def out(x,y):
    def ji():
        print(x* y)
    return ji
kasisd = out(4, 5)
kasisd()
