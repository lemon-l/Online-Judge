'''
Description
　　水仙花数

Input
    输入描述:
    　　判断给定的三位数是否 水仙花 数。所谓 水仙花 数是指其值等于它本身 每位数字立方和的数。例 153 就是一个 水仙花 数。 153=13+53+33
    输入样例:
    123

Output
    输出描述:
    　　一个整数。
    输出样例:
    NO
'''
n = input()

if(int(n) == int(n[0])**3 + int(n[1])**3 + int(n[2])**3):
    print('YES')
else:
    print('NO')
