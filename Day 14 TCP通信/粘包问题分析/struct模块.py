import struct

num = struct.pack('i', 12154)
print(num)
print(len(num))
print(type(num))

print("-----------")

origine = struct.unpack('i', num)
print(origine[0])
print(len(origine))
print(type(origine))