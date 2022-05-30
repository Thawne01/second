"""
三种形式
1.timestamp 从1970年到现在的秒数，用于计算时间差
2.localtime 计算机本地的时间
3.UTC 世界标准时间
"""
import time

print(time.time())  # 获取timestamp
print(time.localtime())  # 获取当地时间，返回 结构化时间
# 获取世界标准时间，返回 结构化时间  ,比中国晚8小时
print(time.gmtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))  # 结构化时间转为字符串时间
print(time.strptime("2022-3-7 16:09:22", "%Y-%m-%d %H:%M:%S"))  # 字符串时间转化为结构化时间
print(time.localtime(10))  # 将10秒转化成时间戳，以结构化方式返回
print(time.localtime(time.time()))  # 当前的时间戳
print(time.mktime(time.localtime()))  # 结构化转时间戳
