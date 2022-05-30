#字典   通过对键操作而对值操作  'key' 果然是 KEY
dics = {'姓名': '翠花', '年龄': '18', '性别': '女'}
dics.update({'地址':'北京'})#以字典的形式添加
#dics,setdefault('地址','北京')前一个位置存放键，后一个位置存放值
#print(dics)
print(dics.get("年龄"))#通过键访问值,修改值,删除键值对

dics['性别'] = '男'
del dics['年龄']
print(dics)




#列表操作
li = ["安琪拉", "妲己", "韩信", "典韦", "吕布"]
plus = ["小乔", "貂蝉"]
li.extend(plus)
print(li)
print("妲己的下标是：", li.index("妲己"))
a = li.index("韩信")
del li[a-1]
print(li)

b = len(li)
li[b-1] = "白起"
print("删减后的list:", li)
print("下标为偶数的元素：", li[0::2])



#字符串的两种定义方法，后者更常用
#characteristic = str("CET6 this time is terribly hard!")
characteristic = "CET6 this time is terribly hard!"
print(characteristic)
#print(characteristic * 2)可以数乘

thinking = "But i'll never give up."
print(characteristic+thinking)     #字符串的“+”拼接
a = "*"
print(a.join(thinking))   #.join()  方法是用a字符串间隔thinking里面的每一个元素,不改变原有字符串，证实字符串是不可变的

#"is" 本身有判断的意思，所以  .isdigit(),.isalpha(),.isupper()   islower()
#.capitalize() 首字母大写    upper()  全部大写     lower()  全部小写

print(characteristic.split("i"))#用characteristic里原有的‘i’分割字符串，return in list form

print(characteristic.startswith("C"))#判断字符串的开头或结尾是否与我们想的一致
print(thinking.endswith((".")))

'''
单个数字，字符串，浮点数，都是不可变的。容器类型的数据包括序列（有序，元组和列表），字典和集合，其中元组是不可变的，列表是可变的，列表通过下标访问元素，
修改数据。字典通过“KEY”对值进行修改或删除
'''
#集合的反序
li.reverse()
print(li)

kd = [0.5,0.6,0.2,0.8,1.4]
kd.sort(reverse=True)  #默认是升序,sort有分类的意思,当然仅对数字列表生效
print(kd)

print(dics.popitem())
print(dics.pop('性别'))

#集合无序,.add()添加






