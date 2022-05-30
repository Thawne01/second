import pymysql




"""
int()默认显示10位
"""


"""
约束：
    bit比特 用来存枚举类型
    unique:字段唯一不重复
    主键：唯一型，不重复
    default
    外键用于多个表
    not null: 非空
    auto_increment: 自增长
    大多数时间在查询

charset = utf8mb4  mb4存表情
--写注释
select database() 查看当前数据库


decimal(5,2)
enum('男'，'女', 'other') default '保密'
*: 查询所有字段
select name as 姓名:起别名
select distinct name from person; 去重查询
python2 里面<>是不等于
18<age<28 识别不了，条件不生效
枚举类型可以用数字代表
条件不能写浮点，写整数
sql不区分大小写
取反：
    not age>18
    
模糊查询：
    like
    % 替换一个或者多个
        where name like "%小%"
    __: 代表有两个位置
        __%至少有两个字
        
    rlike:正则查询
        rlike "^周.*伦$" #  ^以周开始  .*通配符  $以。。。。结束
            "^周(.*)伦$"
        范围查询
            where age in (18,34)
            where age not between 18 and 34 包含边界
        空判断：
            where age is null
        
        排序：多字段排序，一层一层排序
        asc升序
        desc降序
            order by age asc 默认按id排序，默认升序
            
        聚合函数
            count(*) 返回查询结果的数目
            max(age)
            min(height)
            sum()
            avg()
            round(,2)  保留两位小数
        group by age 分组
        select age,count(*) from
        group_concat()
        group by gender having ave(age)>30 新表的筛选 having
        有特殊符号的加``
        分页
            limit 0（位置）,5（数据的数量） 头五个数据
            

"""
"""

select * from st;
select name as 姓名 from st;
select s.name,s.id from st as s;
select distinct gender from st;   distinct消除重复行
select id from st where name='zcc';
select * from st where id>3;


右链接一般不用
group by 只显示出每组的第一条记录,
source

where 针对的是原表，真实存在的表
having 针对生成出来的表

子查询：  不建议
    查询条件包含查询
    消耗时间
    
    
事务：
    事务的原则有原子性：做就做完，要不不做
    出错回滚
    
    start transaction
    commit
    rollback
    
    
运行sql语句之前创建异常
底层是个套接字
"""

"""
create database python_test_1 charset=utf8;


use python_test_1;

create table students(
    id int unsigned primary key auto_increment not null,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男','女','中性','保密') default '保密',
    cls_id int unsigned default 0,
    is_delete bit default 0
);

create table classes (
    id int unsigned auto_increment primary key not null,
    name varchar(30) not null
);


select * from students;
select name from students;
select id, name, gender from students;
select students.id,students.name,students.gender from students;
select s.id,s.name,s.gender from students as s;
select distinct gender from students;
select * from students where id=1;
select * from students where id > 3;
select * from students where id <= 4;
select * from students where name != '黄蓉';
select * from students where is_delete=0;
select * from students where id > 3 and gender=0;
select * from students where id < 4 or is_delete=0;
select * from students where name like '黄%';
select * from students where name like '黄_';
select * from students where name like '黄%' or name like '%靖';
select * from students where id in(1,3,8);
select * from students where id between 3 and 8;
select * from students where (id between 3 and 8) and gender=1;
select * from students where height is null;
select * from students where height is not null;
select * from students where height is not null and gender=1;
select * from students where gender=1 and is_delete=0 order by id desc;
select * from students where is_delete=0 order by name;
select * from students  order by age desc,height desc;
select count(*) from students;
select max(id) from students where gender=2;
select min(id) from students where is_delete=0;
select sum(age) from students where gender=1;
select avg(id) from students where is_delete=0 and gender=2;
select gender from students group by gender;
select gender,group_concat(name) from students group by gender;
select gender,group_concat(id) from students group by gender;
select gender,group_concat(age) from students group by gender;
select gender,avg(age) from students group by gender;
select gender,count(*) from students group by gender;
select gender,count(*) from students group by gender having count(*)>2;
select gender,count(*) from students group by gender with rollup;
select gender,group_concat(age) from students group by gender with rollup;
select * from students where gender=1 limit 0,3;

"""