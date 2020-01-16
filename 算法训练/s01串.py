'''
Description
　　s01串初始为"0"
　　按以下方式变换
　　0变1，1变01

Input
    输入描述:
    　　1个整数(0~19)
    输入样例:
    3

Output
    输出描述:
    　　n次变换后s01串
    输出样例:
    101
'''
# 看到这个题目就是一脸懵逼，完全不知道是什么意思
# 看了其他人的代码，发现是f(n) = f(n - 2) + f(n - 1)的递归
a = int(input())
# 既然是递归，则函数是少不了的
def recursion(n):
    if(n == 0):
        print('0', end='')
    elif(n == 1):
        print('1', end='')
    else:
        recursion(n - 2)
        recursion(n - 1)
recursion(a)
