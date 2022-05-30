from redis import Redis

if __name__ == '__main__':
    cli_add = Redis(host='192.168.184.128', port=6379, db=1)
    # res = cli_add.get('name')
    # print(res.decode('utf-8'))

    # 修改成功返回True
    # res = cli_add.set('name', 'python')
    # print(res)

    res = cli_add.delete('name')
    print(res)


