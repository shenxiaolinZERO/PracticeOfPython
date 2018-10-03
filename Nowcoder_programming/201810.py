# !/usr/bin/env python
# encoding: utf-8
__author__ = 'ScarlettZero'

# 2018-October

# [1] 数组逆置
# 20181001 Monday
def ArrayReverse():
    inArray = input()
    outArray = inArray[::-1]
    print(outArray)
# ArrayReverse()

# [2No] 二叉树遍历   要用指针存？？——C/C++？？
# 20181002 Tuesday
# 二叉树的遍历：
# 1）先序（根）遍历：访问根节点——>遍历左子树——>遍历右子树
# 2）中序（根）遍历：遍历左子树——>访问根节点——>遍历右子树
# 3）后序（根）遍历：遍历左子树——>遍历右子树——>访问根节点
# def BinaryTree():

# [2] 素数判定
# 20181002 Tuesday
def IsPrime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def JudgePrime():
    n = int(input())
    if IsPrime(n):
        print("yes")
    else:
        print("no")
# JudgePrime()


