
# a = int(input("输入年份:"))
# if a%4==0 and a%100!=0 or a%400==0:
#     print("这是闰年")
# else :
#     print("这不是闰年，sb")


def f(x):
    if x >= 20:
        y = x-3
    elif 0 < x < 20:
        y = x+3
    elif x <= 0:
        y = (-x)**2
    return y
a = int(input("输入自变量的值："))
b = f(a)
print("结果是：", b)




