import socket

# 创建套接字对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接至目标服务器
client.connect(("192.168.10.12", 8080))

# 发送问候消息

while True:
    sentence = str(input("输入指令:")).strip()

    if len(sentence) == 0:
        continue
    client.send(sentence.encode(encoding="utf-8"))

    # 接受服务器返回的数据，并解码
    data = client.recv(1024)
    print(">>>", data.decode("utf-8"))

client.close()
