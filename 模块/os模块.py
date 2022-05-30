"""
与操作系统交互，围绕文件和目录操作
"""
import os

# 获取当前工作目录
cud = os.getcwd()
# 生成一个目录
os.mkdir('./呼哈')

# 删除目录，若不为空则无法删除
os.rmdir('./呼哈')

# 生成多层递归目录
os.makedirs('./呼哈/哈哈/呼呼')
# 如果haha下面有文件会触发保护机制，只删到haha


# 将当前文件或文件夹放入列表
os.listdir('../函数基础')


print(os.path.join('a','b','c','D:\\','f','d.txt'))
print(os.path.split())
"""
os.path.isfile
os.path.isdir
os.path.join
os.path.exists
"""
