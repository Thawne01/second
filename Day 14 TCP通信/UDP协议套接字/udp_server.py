import  socket
import time
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('192.168.10.4', 2068))
print("已绑定")
while True:
    data, cli_ad = server.recvfrom(1024)
    print(data)
    print(cli_ad)
    time.sleep(1.5)
    server.sendto(data.upper(), cli_ad)
    print("任务结束")
