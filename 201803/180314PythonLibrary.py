# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

#Python库纵览
# Python语言的开放性
# 开源、开放是Python语言最重要的特点
#  Python解释器开源
#  Python库开源
#  开放的程序生态环境
#  学习(优秀资源)+实践(解决问题)+贡献(推动发展)

# Python库
# PyPI – Python Package Index
# https://pypi.python.org/
#  Python官网提供的Python库索引
#  截止2015年10月，PyPI提供68486个库的检索和下载

# Python编程
# 库(cool)编程
#  Python编程依赖各种已发布库及其中函数或对象
#  基于库的思想有助于程序设计的模块化
#  借助已有代码，快速实现原型系统，关注你的功能

# Python库通用安装方法
# Python库安装概述
#  (1) Python库的自定义安装
# 找到库所在网站，根据指示下载安装
#  (2) Python库的工具安装，使用pip工具
# 通过pip安装库函数，需要计算机连接互联网
#  (3) Python库的文件安装
# 通过.whl文件直接安装

# 库的自定义安装
# 安装numpy库
# 库所在网站：http://www.numpy.org/
# 下载地址：http://sourceforge.net/projects/numpy
# 下载：numpy-1.10.1-win32-superpack-python3.4.exe
# 执行安装


# 库的工具安装：pip
# 以Windows为例，打开cmd，输入pip –h
# 注意，不要在IDLE中输入pip

# pip使用
# pip支持以下一些子命令：...

# pip的install命令
#  命令格式：
# pip install [安装库名称]
#  示例：安装 py2exe库
# pip将py2exe库从网络下载并安装到系统中
#  更新库的命令格式：
# pip install –U [安装库名称]
#  示例：对已安装的 py2exe库进行版本更新
# pip将在网络上检查py2exe库的最新版本，如果更新则
# 下载安装。


# pip的uninstall命令
#  卸载库的命令格式：
# pip uninstall [安装库名称]
#  示例：卸载已安装的 py2exe库
# pip将卸载本机中的py2exe库

# pip的list命令
#  显示已安装库的命令：
# pip list
#  显示有更新的库命令：
# pip list --outdated
#  wheel库提供对wheel格式文件的安装
# Python安装文件一般用wheel格式，.whl

# pip的show命令
#  显示一个已安装库的具体信息
# pip show [安装库名称]
#  示例：显示安装 py2exe库具体信息

# pip的search命令
#  在PyPI中搜索库名或摘要中的关键字
# pip search [关键字]
#  示例：搜索 py2exe关键字对应信息

# 库的文件安装
#  Python库文件的格式：
# Python安装文件一般用wheel格式，.whl
#  下载地址：
# http://www.lfd.uci.edu/~gohlke/pythonlibs
#  示例：安装pywin32库
# 下载 pywin32-219-cp34-none-win_amd64.whl
#  安装命令：


# 安装方式的选择
#  优先级1：pip工具安装
# 但部分库会不成功（请不要纠结）
#  优先级2：库的自定义安装
#  优先级3：库的文件安装