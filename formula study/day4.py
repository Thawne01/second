#可变长度的形式参数
# def f(x,y,*z):
#     print(x)
#     print(y)
#     print(*z)
# #*是保存成元组，**是保存成字典
# #a = f(1,2,45,86,55,2068)
# a= f(*(1,2,'a','s'))
# print(a)
#f(1,2,v=3,h=8)
#参数打散
#命名关键字参数：分隔*和**，使参数对应穿进去，具有映射关系



#拆包
# s,d,f = [5,8,6]
# print(s,d,f)
# s,d,*f = [5,8,6,5,7,]
# print(s,d,*f)


#max(max(4,5),max(456,35))


print(all('', 1))
#all()全为真才返回真，any()全为假才为假
zip()