import subprocess

command = input(">>>").strip()

obj = subprocess.Popen(
    command,
    shell=True,  # True的话就从操作系统的命令提示符运行
    stdout=subprocess.PIPE,  # 通过PIPE在两个进程之间开启一个通道
    stderr=subprocess.PIPE,
)

stdout = obj.stdout.read().decode('utf-8')
stderr = obj.stderr.read().decode('utf-8')

print("成功远程指令")
print(stdout + stderr)
