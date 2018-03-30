# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

###

#图形显示分为：
#   图素法：矢量图：以图形对象为基本元素组成的图形，如矩阵、圆形。
#   像素法：标量图：以像素点为基本单位形成图形。

#Python图形工具包有：tkinter （简称tk接口）、Graphics、turtle

#图形用户界面：
#Graphical User Interface, GUI
#Tkinter---Python 标准GUI
#Graphics---基于Tkinter扩展图形库
#Turtle---python内置的图形库

#举例：单图形编程
#第一步：导入图形模块
import graphics
#第二步：创建图形窗口
win=graphics.GraphWin()
#第三步：关闭窗口
win.close()

#以上三步可以简化为：
from graphics  import  *
win=GraphWin()

#......
#......