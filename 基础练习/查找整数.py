'''
Description
    给出一个包含n个整数的数列，问整数a在数列中的第一次出现是第几个。

Input
    输入描述:
    第一行包含一个整数n。
    第二行包含n个非负整数，为给定的数列，数列中的每个数都不大于10000。
    第三行包含一个整数a，为待查找的数。
    输入样例:
    6
    1 9 4 8 3 9
    9

Output
    输出描述:
    如果a在数列中出现了，输出它第一次出现的位置(位置从1开始编号)，否则输出-1。
    输出样例:
    2
'''
n = int(input())
arr = input().split()
a = input()
i = 0
while i < n:
    if a == arr[i]:
        print(i+1)
        break
    i += 1
if i >= n:
    print(-1)
