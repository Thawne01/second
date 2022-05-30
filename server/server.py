import socket

#创建套接字对象
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#绑定服务端的IP和端口
sock.bind(('192.168.1.4', 8080))
print("已绑定端口，等待进行下一步")


#监听端口等待客户端连接。      可以连接6个，一个在连接，5个在等待连接
sock.listen(5)
print("正在监听该端口")


#接受客户端的连接请求
#服务端要不断的与客户端建立连接，断开连接(不是服务器关机），即稳定运行
while True:
    conn, client_addr = sock.accept()
    print(conn)
    print("IP和端口：", client_addr)



    #接收客户端的问候

    while True:
        try:
            data = conn.recv(1024)
            print("收到客户端消息：", data.decode('utf-8'))

            #对客户端数据反馈
            conn.send("呵……呵……操死你这个丝袜骚货……嘶……这丝袜穴夹得真紧啊……我操……我操……操坏这个丝袜骚逼".encode('utf-8'))
        except ConnectionResetError:
            break

    #关闭与客户端的连接
    conn.close()



#关闭服务器
sock.close()

