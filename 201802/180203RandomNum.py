


# 利用 Python 随机产生1000个1~10000之间的整数，找出其中最大的5个三位数并输出。
# 要求： 1）利用列表存储产生的所有数。 2）将最大的5个三位数存储在一个元组中。

from random import randint
l=[randint(1,10000) for i in range(1000)]

l_sorted=sorted([i for i in l if i<1000],reverse=True)
max5=(l_sorted[0],l_sorted[1],l_sorted[2],l_sorted[3],l_sorted[4])
print(max5)

#输出结果：
#(999, 997, 992, 980, 971)

