# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

# >1hours

#字典是针对非序列集合而提供的一种数据类型，灵活地查找信息。
#是一种“键值对”。
#例如：姓名和电话号码；用户名和密码，国家名称和首都等。

#字典的概念：通过任意键值查找集合中值信息的过程。
#Python中通过字典实现映射
#字典是键值对的集合：该集合以键为索引，同一个键信息对应一个值。
#一个键值也叫一个字典对象，字典对象是可变的，它是一个容器类型，能存储任意个数的Python对象，也可包括其他容器类型。

passwd={"China":"BigCountry","Korean":"SmallCountry","France":"MediumCountry"}
print("字典例子为：",passwd)

#字典类型与序列类型的区别：
#1.存取和访问方式不同。
#2.键的类型不同：序列类型只能用数字类型的键；字典类型可以用其他对象类型作为键。
#3.排列方式不同：序列类型保持了元素的相对关系；字典中的数据是无序排列的。
#4.映射方式不同：序列类型通过地址映射到值；字典类型通过键直接映射到值。


#####----字典的操作

#操作1：为字典增加一项：dictionary[key]=value
students={"2302018001":"John","2302017002":"Peter"}
students["2302017003"]="Susan" #增加一个新的数据项

#操作2：访问字典中的值：dictionaryName[key]返回键key对应的值value
print("访问字典中的值：",students["2302017003"]) #访问字典中的值： Susan
print("访问字典中的值：",students["2302017002"]) #访问字典中的值： Peter

#操作3：删除字典中的一项：del dictionaryName[key]
del students["2302017003"]
print("删除后的学生字典为：",students) #删除后的学生字典为： {'2302018001': 'John', '2302017002': 'Peter'}

#操作4：字典的遍历
    # for key in students:
    #     print(key+":"+str(students[key]))
    #     #结果为：2302018001:John
    #     #       2302017002:Peter
    #
    # #遍历字典的键key：
    # for key in dictionaryName.keys():
    #     print(key)
    # #遍历字典的值value：
    # for value in dictionaryName.values():
    #     print(value)
    # #遍历字典的项：
    # for item in dictionaryName.items():
    #     print(item)
    # #遍历字典的key-value：
    # for item,value in dictionary.items():
    #     print(item,value)

#操作5：判断一个键是否在字典中：in 或者not in
students2={"2302018001":"John","2302017002":"Peter"}
print("2302018001" in students2) #True
print("2302018011" in students2) #False

##----字典的标准操作符：-,<,>,=,<=,>=,==,!=,and,or,not
d1={"red":41,"blue":3}
d2={"blue":3,"red":41}
print(d1==d2) #True
print(d1!=d2) #False
print("--------------------------------")

#Python 还提供了丰富的字典方法，其中：

#keys():tuple  返回一个包含字典所有key的列表
#values():tuple 返回一个包含字典所有value的列表
#items():tuple  返回一个包含所有键值的列表
#clear():None  删除字典中的所有项目
#get(key):value  返回字典中key对应的值
#pop(key):val  删除并返回字典中key对应的值
#update(字典)  将字典中的键值添加到字典中

students3={"2302018001":"John","2302017002":"Peter"}
print("包含字典所有key的列表：",tuple(students3.keys())) #包含字典所有key的列表： ('2302018001', '2302017002')
print("包含字典所有value的列表：",tuple(students3.values())) #包含字典所有value的列表： ('John', 'Peter')
print("包含字典所有key、value的列表：",tuple(students3.items())) #包含字典所有key、value的列表： (('2302018001', 'John'), ('2302017002', 'Peter'))
print("返字典中key的对应的值：",students3.get("2302018001")) #返字典中key的对应的值： John
print(" 删除并返回字典中key对应的值：",students3.pop("2302018001")) # 删除并返回字典中key对应的值： John
print("删除后的字典为：",students3) #删除后的字典为： {'2302017002': 'Peter'}
print("删除字典中所有项目后：",students3.clear()) #删除字典中所有项目后： None
print(students3) #{}

