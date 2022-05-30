
from peewee import *

# peewee会自动增添id字段


"""insert , update,等后面要加execute()"""

database = MySQLDatabase(host="localhost", user="root", password='51721', port=6529, database='big')


class person(Model):
    name = CharField()
    age = IntegerField()

    class Meta:
        database = database
        table_name = 'person'


def create_table():
    # 判断表是否存在，若已经存在则删除，再创建新的表

    isexist = person.table_exists()
    if isexist:
        res = person.drop_table()
        print("drop_table =", res)
    res = person.create_table()
    print("create_table = 0,", res)


def insert_data(person):
    res = person.insert(person.__data__).execute()  # 返回表里自增的id值
    print("insert data = ", res)


def query_data():
    personList = person.select().execute()
    if len(personList) == 0:
        print("表中数据为空")
        return

    for ele in personList:
        print("name = ", ele.name, "age = ", ele.age)


def update_data(person):
    person.update(age=555).where(person.name == "curry").execute()
    # person.age = 555
    # res = person.update(person.__data__).where(person.name == "curry").execute()
    # print("update_data = ", res)


def delete_data(person):
    res = person.delete().where(person.name == "curry").execute()
    print("delete_data = ", res)


if __name__ == "__main__":
    database.connect()

    create_table()
    persona = person(name="curry", age=30)
    personb = person(name="stephon", age=66)
    insert_data(persona)
    insert_data(personb)
    query_data()

    update_data(persona)
    query_data()

    delete_data(person)
    query_data()
