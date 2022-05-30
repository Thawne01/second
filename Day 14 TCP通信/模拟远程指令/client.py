import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("192.168.1.4", 8080))

while True:
    command = input(">>>").strip()
    if len(command) == 0:
        continue
    client.send(command.encode('utf-8'))

    data = client.recv(1024)
    print(data.decode('gbk'))


client.close()
