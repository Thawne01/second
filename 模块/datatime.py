from datetime import datetime
#print(datetime.now())#以字符串形式返回当下时间
t = datetime.now()
"""
t.year  month  day  hour minute second microsecond
"""
tm = t.minute
print(tm)

# 手动指定时间
# print(datetime.datetime(2022,3,7,16,23,56))
t2 = datetime(2021, 5, 8, 2)
print("时间差", t2)


# 替换某个时间单位的值
nt = t.replace(year=2000)
print(nt)

