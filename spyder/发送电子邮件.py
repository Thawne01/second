import smtplib
from email.mime.text import MIMEText

# 实例化一个对象
smt = smtplib.SMTP()

# 读取文件信息
with open('novel.txt', mode='r', encoding='utf-8') as f:
    send_msg = f.readlines()
send_msg = send_msg[0]

message = MIMEText(send_msg, 'plain', 'utf-8')
message['Subject'] = "我给你的第一封邮件"

# 连接smtp服务器
smt.connect('smtp.qq.com', 25)

# 登录邮箱用户名和密码
smt.login('1879053131@qq.com', 'mgnpfvaszgyvjbge')

# 发送邮件
smt.sendmail('1879053131@qq.com', '1879053131@qq.com', message.as_string())