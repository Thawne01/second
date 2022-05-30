import socket
import subprocess
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.1.4', 8081))
sock.listen(5)
print("水淋淋红嫩嫩的蜜穴口，大阴唇一颤一颤的，好似在急不可耐的等待着我的大鸡巴降临")
while True:
    conn, addr = sock.accept()

    while True:
        try:
            command = conn.recv(1024)
            obj = subprocess.Popen(
                command.decode('utf-8'),
                shell=True,
                stdout= subprocess.PIPE,
                stderr= subprocess.PIPE
            )
            stdout = obj.stdout.read().decode('gbk')
            stderr = obj.stderr.read().decode('gbk')
            header_len =len(stdout+stderr)
            header = struct.pack('i', header_len)
            conn.send(header)
            conn.send(stdout.encode('utf-8')+stderr.encode('utf-8'))
            print("随着一声透骨的娇吟，张琳到达了绝美的高潮，喷涌而出的淫水在地板上形成了一滩巨大的水渍")
        except ConnectionResetError:
            break
    conn.close()
sock.close()