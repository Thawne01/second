"""
函数嵌套的一种特殊形式，在调用一个函数的过程中又调用该函数本身，称为递归
我用我自己
def locat(k):
    print('fron locat', k)
    locat(k+1)
locat(0)

递归调用的两个阶段：
   1.回溯：重复调用的过程，每一回规模减少，最终接近一个结果，有明确的结束条件
   2.递推：从结果一层层往回推算

   逻辑型的调用
pass 不是没有用的，而是让pass所在的代码块不输出？不执行？
"""

l = [1,[2,3,[4,[5,[6,[7,[8,[9]]]]]]]]

"""如果考虑遍历拿到每一个数字"""
for n in l:
    print(n)

for i in range(len(l)):
    i = 0
    if i <= len(l):
        la = []
        temp = l[i]
        la.append(temp)
        print(la[0])
        i += 1
    if i == len(l):
        break

# def locat(k):
#     print('fron locat', k)
#     locat(k+1)
# locat(0)


def handle(l):
    for n in l:
        if type(n) is not list:
            print('a number:', n)
        else:
            handle(n)
handle(l)



