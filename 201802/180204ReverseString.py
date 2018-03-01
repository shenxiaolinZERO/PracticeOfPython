

### Python 实现字符串反转

# class Solution:
def reverseString():
    s=input("请输入要反转的内容：")
    return s[::-1]


s="abcde"
solu=reverseString()
print("反转结果为：",solu)

# 请输入要反转的内容：abcde
# 反转结果为： edcba
