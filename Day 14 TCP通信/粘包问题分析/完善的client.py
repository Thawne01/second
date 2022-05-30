import socket
import struct

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.4', 8081))
while True:
    command = input(">>>:").strip()
    if len(command)==0: continue
    client.send(command.encode('utf-8'))
    temp = client.recv(4)
    total_data = struct.unpack('i', temp)[0]
    data = b''
    ori_size = 0
    while ori_size <= total_data:
        tem_dt = client.recv(1024)
        ori_size += len(tem_dt)
        data += tem_dt

    print("收到数据：", data.decode('utf-8'))

client.close()