import pymysql
import os
import time


def create_table(cursor):
    sql = "drop table if exists person"  # 删除原有的vagina表
    result = cursor.execute(sql)  # 操作成功返回0
    print("drop table =", result)

    sql = """
          create table person(
          name varchar(20),
          age int(4)
          )
    """
    result = cursor.execute(sql)
    print("create table = ", result)


def insert_data(cursor, name, age):
    sql = """
          insert into person(name,age) values('{}','{}')
    """.format(name, age)
    result = cursor.execute(sql)
    conn.commit()
    print("insert_data =", result)


def query_data(cursor):
    sql = """
        select name age
        from person
    """
    res = cursor.execute(sql)
    print("query_data = ", res)

    if res >= 1:
        data = cursor.fetchall()
        print(data)
        return data


def update_data(cursor):
    sql = """
        update person set age = 250 where name = "晨晨"
    """
    res = cursor.execute(sql)
    print("update_data=", res)


def delete_data(cursor):
    sql = """
        delete from person where name = "晨晨"
    """
    res = cursor.execute(sql)
    print("delect_data =", res)


if __name__ == '__main__':
    # conn = pymysql.connect(host='localhost', user='root', password='51721', database='moans', port=6529)
    # 获取字典结构
    conn = pymysql.connect(host='localhost', user='root', password='51721', database='moans', port=6529,
                           cursorclass=pymysql.cursors.DictCursor)

    print('connection success')

    # 获得游标
    cursor = conn.cursor()
    # 创建一张表
    create_table(cursor)
    # 写入数据
    insert_data(cursor, name="晨晨", age=10)
    insert_data(cursor, name="我的", age=15)
    query_data(cursor)

    # 对数据修改
    update_data(cursor)
    query_data(cursor)

    # 删除数据
    delete_data(cursor)
    data = query_data(cursor)
    print(data[0]["age"])

    # 关闭连接
    cursor.close()
    conn.close()
# def create_table(cuesor):
#     sql = "drop table if exists labia"e
#     result = cursor.execute(sql)
#     print("drop table =", result)
#
#     sql2 = """
#     create table labia(
#         name nvarchar(20),
#         age int(3）
#     )
#     """
#     result = cursor.execute(sql2)
#     print("create table =", result)
#
# if __name__ == "__main__":
#     #连接数据库
#     conn = pymysql.connect(host="localhost", user='root', password="51721", database='sex_moans', cursorclass=pymysql.cursors.DictCursor)
#     #获得mysql的游标
#     cursor = conn.cursor()
#     #创建一张表
#     create_table(cursor)
#     #写入数据
#     #对数据进行修改
#     #删除数据


sql = 'show database big;'
cursor.executemany(sql, [])