'''
Description
　　求出区间[a,b]中所有整数的质因数分解。

Input
    输入描述:
    　　输入两个整数a，b。
    输入样例:
    3 10

Output
    输出描述:
    　　每行输出一个数的分解，形如k=a1*a2*a3...(a1<=a2<=a3...，k也是从小到大的)(具体可看样例)
    输出样例:
    3=3
    4=2*2
    5=5
    6=2*3
    7=7
    8=2*2*2
    9=3*3
    10=2*5
'''
start, end = map(int, input().split())

# 判断是否为素数
def is_Primes(a):
    for i in range(2, a // 2 + 1):
        if(a % i == 0):
            return False
            break
    return True
'''
如果一个数本身自己就是素数，则可以表示成 n = n;
如果是个偶数，则可以表示成 n = 2 * k
如果是个奇数，则从3开始遍历，寻找他的质因数

如果用传统的.format方法，得重置n次，显然一点都不合理，所以可以巧用循环来实现
'''
for i in range(start, end + 1):
    if(is_Primes(i)):
        print("{0}={1}".format(i, i))
    else:
        print('{0}='.format(i),end='')
        l = []
        while i > 1:
            for j in range(2, i+1):
                if i % j == 0:
                    i //= j
                    l.append(str(j))
                    break
        print("*".join(l))
        

