# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#一、创建对象
#1. 通过传递一个list对象来创建一个Series，pandas会默认创建整型索引：
s=pd.Series([1,3,4,np.nan,6,8])
print(s)
# 0    1.0
# 1    3.0
# 2    4.0
# 3    NaN
# 4    6.0
# 5    8.0
# dtype: float64

#2.通过传递一个numpy array，时间索引以及列标签来创建一个DataFrame：
dates=pd.date_range('20180301',periods=6)
print(dates)
# DatetimeIndex(['2018-03-01', '2018-03-02', '2018-03-03', '2018-03-04',
#                '2018-03-05', '2018-03-06'],
#               dtype='datetime64[ns]', freq='D')
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
# numpy.random.randn(d0, d1, …, dn)是从标准正态分布中返回一个或多个样本值。(可含负数）
# numpy.random.rand(d0, d1, …, dn)的随机样本位于[0, 1)中。
#P=numpy.random.rand(N,K) #随机生成一个 N行 K列的矩阵
print(df)
#                    A         B         C         D
# 2018-03-01 -0.451506 -0.884044 -0.916664 -0.763684
# 2018-03-02 -0.463568  0.340688 -0.077484 -0.237660
# 2018-03-03 -1.533427  0.301283  0.268640 -0.011027
# 2018-03-04  1.036050  0.402203  0.485365  2.086525
# 2018-03-05  0.221578 -0.821756 -0.265241  0.277563
# 2018-03-06  1.774195 -0.288553  1.527936  0.119153

