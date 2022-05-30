import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.0.100', 8081))

while True:
    msg = input('>>>').strip()
    client.send(msg.encode('utf-8'))

    data = client.recv(1024)
    print("收到服务器数据", data)
client.close()