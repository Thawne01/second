import hashlib


# 文件完整性校验,   不可逆


# 1.创建hash工厂
# fac = hashlib.md5()
fac = hashlib.sha1()
# hashlib.sha224()

# 2.在内存里传值, 内存里只有二进制
fac.update('我和你在一起的时光总是过得特别快'.encode('utf-8'))

# 3.产出hash值
print(fac.hexdigest())
