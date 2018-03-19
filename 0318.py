# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

session_item_dic={ 0:[[1,2,3],[4,5,6]] }
dic = {}
for i, j in session_item_dic.items():
    item_list = j
    # item_list.extend(j[1])
    dic[i] = item_list
print(dic)

