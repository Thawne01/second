import pymysql


def create_table(cur):
    sql = """drop table if exists students;"""
    res = cur.execute(sql)
    print('1', res)
    sql = """
        create table students(
            id int primary key not null,
            name varchar(20) not null,
            age int not null,
            sex enum('男', '女', '其他'),
            hobbies set('远离那些困扰', '穿过沙漠遇见你','冥冥之中谁在编排你')
        );
    """
    res = cur.execute(sql)

    print(res)


def append_data(cur):
    sql = """
        insert into students values
        (1,"路文飞", 30, '女', '远离那些困扰'),
        (2,"感谢你特别邀请", 28,'男','冥冥之中谁在编排你'),
        (3,"来见证你的爱情", 32, '女','穿过沙漠遇见你'),
        (4,"茶饭不思", 17,'男','远离那些困扰');
    """
    res = cur.execute(sql)

    print(res)


def fetch_data(cur):
    sql = """
        select * from students where sex='男'
    """
    res = cur.execute(sql)

    print('获取数据', res)

    if res >= 1:
        data = cur.fetchall()
        print(data)


def delete_data(a):
    sql = """
        delete s.* from students as s where id=3
    """
    res = a.execute(sql)

    print('删除数据', res)


def modifydata(cur):
    sql = """
        update students set sex='男' where sex='女'
    """
    res = cur.execute(sql)

    print('修改数据', res)


def main(cur):
    create_table(cur)

    append_data(cur)
    fetch_data(cur)
    delete_data(cur)

    modifydata(cur)


if __name__ == '__main__':
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='51721',
        database='cc',
        port=6529,
        cursorclass=pymysql.cursors.DictCursor
    )
    cur = conn.cursor()
    main(cur)
    conn.commit()
    cur.close()
    conn.close()
