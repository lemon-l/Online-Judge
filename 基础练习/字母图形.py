'''
Description
    利用字母可以组成一些美丽的图形，下面给出了一个例子：
    ABCDEFG
    BABCDEF
    CBABCDE
    DCBABCD
    EDCBABC
    这是一个5行7列的图形，请找出这个图形的规律，并输出一个n行m列的图形。

Input
    输入描述:
    输入一行，包含两个整数n和m，分别表示你要输出的图形的行数的列数。
    输入样例:
    5 7

Output
    输出描述:
    输出n行，每个m个字符，为你的图形。
    输出样例:
    ABCDEFG
    BABCDEF
    CBABCDE
    DCBABCD
    EDCBABC
'''
line, column = map(int, input().split())
# 定义一个空的二维数组
list1 = [[0 for j in range(column)] for i in range(line)]

for i in range(line):
    for j in range(column):
        if(j >= i): # 数组中字母规律
            list1[i][j] = chr(ord('A') + j - i)
        else:
            list1[i][j] = chr(ord('A') + i - j)

for m in range(line):
    for n in range(column):
        print(list1[m][n], end='')
    print()
