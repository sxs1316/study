# --*-- coding:utf-8 --*--
# @FileName      : 003_Python字符串.py
# @DateTime      : 2022/11/24 20:49
# @Author        : SXS
# @Email         : sxs1316@outlook.com
# @description   : Python字符串相关操作和应用
# @Version       : 1.0


# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 字符串可以用+运算符连接在一起，用*运算符重复。
# Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# Python中的字符串不能改变。

s = 'abcdefg'

# 字符串索引
print(s[0], s[-1])

# 字符串截取
print(s[0:2], s[-2:])

# 字符串转义
s1 = 'a\nb'
s2 = r'a\nb'
print(s1)
print(s2)

# 字符串拼接
a = 'a'
b = 'b'
print(a+b)



