'''
Description
　　153是一个非常特殊的数，它等于它的每位数字的立方和，即153=1*1*1+5*5*5+3*3*3。编程求所有满足这种条件的三位十进制数。

Input
    输入描述:
    　　按从小到大的顺序输出满足条件的三位十进制数，每个数占一行。
    输入样例:

Output
    输出描述:

    输出样例: 
'''
def judge(n):
    s = 0
    for i in range(len(n)):
        s += pow(int(n[i]), 3)
    if(s == int(n)):
        print(n)

for i in range(100, 1000):
    judge(str(i))