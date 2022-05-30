with open('novel2.txt', mode='r', encoding='utf-8') as f, open('novel.txt', mode='w', encoding='utf-8') as fd:
    send_msg = f.readlines()
    send_msg = send_msg[0]  # 拿到列表中的字符串
    # print(send_msg.replace('\u3000', ''))  搞定
    send_msg = send_msg.replace('\u3000', '')
    fd.writelines(send_msg)
    fd.flush()
