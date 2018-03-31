# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

# Matplotlib教程

# Matplotlib安装
#  NumPy库方便数值运算，但枯燥的数据并不利于人们的直观理解。
#  数据需要可视化。
#  Matplotlib：一个数据可视化函数库
#  使用前需要安装
#    利用Python自带的pip工具自动安装
#    访问python官网提供的扩展包下载页面安装 https://pypi.python.org/pypi

# pyplot子库
#  Matplotlib的子库pyplot提供了2D图表制作的基本函数, 实现如：
#  创建图形， 在图形上创建画图区域， 在画图区域上画线，在线上标注等功能。 域上画线，在线上标注等功能。
#  推荐学习手册下载链接地址如下：
# http://www labri fr/perso/nrougier/teaching/matplotlib/

# 初级绘图-例1散点图绘制
# plot()函数基础
#  示例程序如下
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5,6],'ro')
plt.ylabel('Decription of y value')
plt.show()
#  显示结果如下:...

# 初级绘图-例2
#  利用Numpy库的linspace函数生成了一个numpy数组X，包含了从-π到+π等间隔的256个值。
#  S和C则分别是这256个值对应的其正弦x和其平方的余弦xian值组成的numpy数组。 的余弦xian值组成的numpy数组。
#  利用plot函数打印相应图形
#    legend函数用来描述表示每条曲线的标签
#    Title函数用来设置 图标题。
import numpy as np
from matplotlib.pyplot import *
X=np.linspace(-np.pi,np.pi,256,endpoint=True)
C,S=np.cos(X*X),np.sin(X)
plot(X,C,"ro",label="$sin(x)$")
plot(X,S,label="$cos(x^2)$")
xlabel("xlabel")
ylabel("ylabel")
legend()
title("This is Title")
show()
#  显示结果如下:...

#
# 初级绘图-多子图绘制
#  Pyplot子库也可以被用来生成多个子图
#    使用subplot()绘制含有多个子图的图表，语法如下:
#    subplot(nRows, mCols, plotNum)
#  图表的整个绘图区域被等分为n行和m列 然后按照从左到右、从上到下的顺序对每个区域进行编号 ，左上区域的编号为1。
#  plotNum参数指定所创建的子图编号。
#  如果新创建的子图和之前创建的子图区域有重叠的部分，则之前的子图将被覆盖。
from matplotlib.pyplot import *
subplot(221)
subplot(222)
subplot(121)
subplot(224)
show()
#  显示结果如下:...

#
# 初级绘图-双子图绘制实例
import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t) *np.cos(2*np.pi*t)
t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)

plt.subplot(211)
plt.plot(t1,f(t1),"bo",t2,f(t2),"k")
plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2),"r--")
plt.show()
#  显示结果如下:...


# 初级绘图-直方图绘制
#  直方图是数据的一种重要展现形式，它也叫柱状图,是将一个变量的不同等级的相对频数用矩形块标绘的图表。
#  matplotlib提供的直方图绘制函数为hist()
#  其中参数50表示直方图中直条即bin的个数，normed参数是一个布尔值，为真时，表示需要将直方图归一化，
#    纵轴以概率的形式表示。text函数用来在指定位置添加文本标识 用来在指定位置添加文本标识

import numpy as np
import matplotlib.pyplot as plt

mu,sigma=100,15
x=mu+sigma*np.random.randn(10000)
plt.hist(x,50,normed=1,facecolor="g")
plt.xlabel("Smarts")
plt.ylabel("Probability")
plt.title("Histogram of IQ")
plt.text(60,0.025,r"$\mu=100,\ \sigma=15$")
plt.axis([40,160,0,0.03])
plt.show()
#  显示结果如下:...

# 初级绘图
#  matplotlib还有很多功能强大的其他子库，比如可以利用image这个子库，对图像进行操作 g
#  示例如下， 其中image子库的imread函数将png 图片各个像素点的RGB值存入到numpy的数组中 图片各个像素点的RGB值存入到numpy的数组中

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img=mpimg.imread(".\\pythonlogo.png")
plt.imshow(img)
plt.show()
#  显示结果如下:...
