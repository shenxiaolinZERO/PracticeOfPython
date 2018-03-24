# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

# session_item_dic={ 0:[[1,2,3],[4,5,6]] }
# dic = {}
# for i, j in session_item_dic.items():
#     item_list = j
#     # item_list.extend(j[1])
#     dic[i] = item_list
# print(dic)
#

from pandas import Series,DataFrame

# series=Series(["Kangkang","Michale","Jane","Maria"])
# print(series)
#
# print(series.values)
# print(series.index)

# data={"name":["Kangkang","Michale","Jane","Maria"],"age":["18","19","20","21"]}
# dataFrame=DataFrame(data,columns=["name","age","score"])
# print(dataFrame)
filepath1=r"I:\Papers\consumer\codeandpaper\TmallCode\new_code_new_implicit\new_code\data\dataset1\train\session_item.txt"
filepath2=r"I:\Papers\consumer\codeandpaper\TmallCode\new_code_new_implicit\new_code\data\dataset1\train\items.txt"

# r"I:\Papers\consumer\codeandpaper\TmallCode\\new_code_new_implicit\\new_code\data\dataset1\implicit\train_implicit\session_item.txt"
# r"I:\Papers\consumer\codeandpaper\TmallCode\\new_code_new_implicit\\new_code\data\dataset1\implicit\train_implicit\items.txt"


infile1=open(filepath1,"r")
infile2=open(filepath2,"r")

lines=infile1.readlines()
session_len=len(lines)
item_sum=0.0
for session in lines:
    session_item=session.split(";")
    explicit_item=session_item[1]
    explicit_item_len=len(explicit_item)
    item_sum+=explicit_item_len
average1=item_sum/session_len
# print("一共有 %d 个session。"%session_len)
# print("一共有 %d 个explicit item。(session_item文件中的第二列总数)"%item_sum)
# print("每个session平均有 %d 个explicit item。"%average1)

print("一共有 %d 个session。"%session_len)
print("一共有 %d 个buy item。(session_item文件中的第二列总数)"%item_sum)
print("每个session平均有 %d 个buy item。"%average1)

print("\\\\\\\\\\")
item_line=infile2.readline()
item_split=item_line.split()
explicit_item=len(item_line)
average2=explicit_item/session_len
# print("item文件总共有 %d 个explicit_item"%explicit_item)
# print("每个session平均有 %d 个explicit item。"%average2)
