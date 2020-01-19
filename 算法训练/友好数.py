'''
Description
　　有两个整数，如果每个整数的约数和（除了它本身以外）等于对方，我们就称这对数是友好的。例如：
　　9的约数和有：1+3=4
　　4的约数和有：1+2=3
　　所以9和4不是友好的。
　　220的约数和有：1 2 4 5 10 11 20 22 44 55 110=284
　　284的约数和有：1 2 4 71 142=220
　　所以220和284是友好的。
　　编写程序，判断两个数是否是友好数。

Input
    输入描述:
    　　一行，两个整数，由空格分隔
    输入样例:
    220 284

Output
    输出描述:
    　　如果是友好数，输出"yes"，否则输出"no"，注意不包含引号。
    输出样例:
    yes
'''
m, n = map(int, input().split())

def judge(t):
    sum1 = 0
    for i in range(1, t // 2 + 1):
        if(t % i == 0):
            sum1 += i
    return sum1

if(judge(m) == n and judge(n) == m):
    print('yes')
else:
    print('no')
