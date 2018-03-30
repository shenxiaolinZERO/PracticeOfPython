# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

# NumPy库介绍

# NumPy的安装
#  NumPy系统是Python的一种开源的数值计算扩展
#  可用来存储和处理大型矩阵 可用来存储和处 大 矩阵
#  使用前需要安装
#  可以利用Python自带的pip工具自动安装 可以利用 y 自带的p p工具自动安装
#  或者选择访问下面的网站，下载与Python版本匹配的 exe安装文件
# http://sourceforge.net/projects/numpy/files/NumPy/
#  安装完成后，打开Python3.4，运行命令import numpy，若不出现错误则说明安装成功。

# NumPy的组成与功能
#  Numpy （Numeric Python）可以被理解为一个用python实现的科学计算包，包括：
#  强大的N维数组对象Array；  强大的N维数组对象Array；
#  成熟的函数库；
#  实用的线性代数、傅里叶变换和随机数生成函数。
#  提供了许多高级的数值编程工具，如：矩阵数据类、矢量处理，以及精密的运算库。

# 基础知识
#  NumPy的主要对象是同种元素的多维数组
#  维度(dimensions)叫做轴(axes)
#  轴的个数叫做秩(rank)。
#  例如，在3D空间一个点的坐标 [1, 2, 3] 是一个秩为1的数组，因为它只有一个轴。轴长度为3.
#  例如，在[[ 1., 0., 0.
#  NumPy的数组类被称作ndarray，通常被称作数组。
#    注意numpy.array和标准Python库类array array并不相同,后者只处理一维数组和提供少量功能。
#    ndarray对象属性主要见下表： 例如其中.shape表示数组的维度， .size表示数组元素的总个数。
#
#---属性-------解释
#ndarray.shape:数组的维度，这是一个指示数组在每个维度上大小的整数元组。
#ndarray.size:数组元素的总个数，等于shape属性中元组元素的乘积。
#ndarray.dtype:一个用来描述数组中元素类型的对象，可以通过使用标准Python类型创造dtype。
#ndarray.itemsize:数组中每个元素字节的大小。
#ndarry.data:包含实际数组元素的缓冲区，通常我们通过索引引用数组元素，不使用这个属性。
#

#例子：
from numpy import  *
a=arange(15).reshape(3,5)
print(a)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
print(a.shape)  #(3, 5)
print(a.ndim) #2
print(a.dtype.name) #'int32'
print(a.itemsize) #4
print(a.size) #15
print(type(a)) #<class 'numpy.ndarray'>
b=array([6,7,8])
print(b) #[6 7 8]
print(type(b)) #<class 'numpy.ndarray'>

# 创建数组（方法一）
#  创建数组的方法有多种，比如可以使用array函数利用常规的Python列表和元组创造数组。所创建的数组类型由原序列中的元素类型决定。示例如下：


# 创建数组（方法二）
#  NumPy提供了一些使用占位符创建数组的函数。
#  例如： 函数zeros创建一个全是0的数组，函数ones创建一个全1的数组，函数empty创建一个内容随机并且依赖与内存状态的数组。默认创建的数组类型(dtype)都是float64 示例如下：

# 创建数组（方法三）
#  此外NumPy提供一个arange的函数返回数组，示例如下：


# 打印数组
#  打印数组时，NumPy以类似嵌套列表的形式显示。
#   示例如下：其中一维数组被打印成行，二维数组成矩阵，三维数组成矩阵列表。

# 基本运算
#  数组的算术运算是按元素进行。
#    NumPy中的乘法运算符*指示按元素计算
#  矩阵乘法可以使用dot函数或创建矩阵对象实现。示例如下：

#  非数组的运算可以利用ndarrary类方法实现。
#  通用函数(ufunc) -- NumPy提供常见的数学函数。如sin cos和exp 如sin, cos和exp。
#  在NumPy里这些函数作用按数组的元素运算，产生一个数组作为输出。示例如下：

# 索引、切片与迭代
#  数组还可以被索引、切片和迭代，示例如下：

# 矩阵运算
#  NumPy对于多维数组的运算，缺省情况下并不使用矩阵运算，对数组进行矩阵运算，可调用相应的函数。
#  numpy库也提供了matrix类，使用matrix类创建的是矩阵对象，它们的加减乘除运算缺省采用矩阵方式计算，用法和matlab十分类似。示例如下：


#  矩阵中更高级的一些运算可以在NumPy的线性代数子库linalg中找到。例如inv函数计算逆矩阵，solve函数可以求解多元一次方程组程组。
#
# 函数和方法的总览
#  NumPy库提供作用丰富的函数和方法，下面是一个分类排列汇目录总揽，大家可以通过手册即用即学。