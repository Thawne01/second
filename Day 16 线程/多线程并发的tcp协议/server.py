import socket
from threading import Thread


def communication(conn):
    while True:
        try:
            data = conn.recv(1024)
            print("收到客户端数据", data)

            conn.send(data.upper())
        except ConnectionResetError:
            break

def server(ip,port,backlog=5):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(backlog)
    while True:
        #链接循环
        conn, client_addr = server.accept()

        #通信循环
        t = Thread(target=communication, args=(conn, ))
        t.start()

if __name__ == '__main__':
    s = Thread(target=server, args=('192.168.0.100', 8081))
    s.start()