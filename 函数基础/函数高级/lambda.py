"""
ctrl + F5重启程序
ctrl+F2停止
F9 绿色的三角形调到下一个断定
F8 蓝色朝下的椒图单步走
Alt+ shift +F7蓝色朝右下角的尖头是进入定义函数的函数
F7进入函数
shift+F8跳出函数
"""
"""
用于临时使用一次的场景，没有重复使用的需求
lambda 空格 参数:函数体
返回值省了return
内存地址赋值给变量无意义，但是可以用
"""
print(lambda x,y:x*y)
print((lambda x, y: x*y)(1, 2))

salaries={
    'xialuo':3000000,
    'xishi':5000,
    'dahai':4656
}
#
#聚合函数max,min
#max(字典,key=函数名),比较valuo值，返回key
def func(name):
    return salaries[name]
print(max(salaries, key=func))
print(max(salaries, key=lambda name:salaries[name]))
print(min(salaries, key=lambda name:salaries[name]))

nums=[11,33,55,97,5456]
res = sorted(nums, reverse=True)
print(res)

#for遍历
for i in salaries.values():
    print(i)
print(sorted(salaries.values()))
print(sorted(salaries, key=lambda name:salaries[name], reverse=False))


