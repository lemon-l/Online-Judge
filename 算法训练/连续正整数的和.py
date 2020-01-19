'''
Description
　　78这个数可以表示为连续正整数的和，1+2+3，18+19+20+21，25+26+27。
　　输入一个正整数 n(<=10000)
　　输出 m 行(n有m种表示法)，每行是两个正整数a，b，表示a+(a+1)+...+b=n。
　　对于多种表示法，a小的方案先输出。

Input
    输入描述:

    输入样例:
    78

Output
    输出描述:
    输出样例:
    1 12
    18 21
    25 27
'''
n = int(input())
for i in range(1, n // 2 + 1):
    t = n
    for j in range(i, n // 2 + 1):
        t -= j
        if(t == 0):
            print('{0} {1}'.format(i, j))
            break