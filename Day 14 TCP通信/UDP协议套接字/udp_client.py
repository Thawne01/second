import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input(">>>").strip()
    client.sendto(msg.encode('utf-8'), ('192.168.1.4', 8082))
    data, ser_addr = client.recvfrom(1024)
    time.sleep(1.5)
    print(data.decode('utf-8'))
    print(ser_addr)
