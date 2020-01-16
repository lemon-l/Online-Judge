'''
Description
　　Hanks 博士是BT (Bio-Tech，生物技术) 领域的知名专家，他的儿子名叫Hankson。现 在，刚刚放学回家的Hankson 正在思考一个有趣的问题。 今天在课堂上，老师讲解了如何求两个正整数c1 和c2 的最大公约数和最小公倍数。现 在Hankson 认为自己已经熟练地掌握了这些知识，他开始思考一个“求公约数”和“求公 倍数”之类问题的“逆问题”，这个问题是这样的：已知正整数a0,a1,b0,b1，设某未知正整 数x 满足： 1． x 和a0 的最大公约数是a1； 2． x 和b0 的最小公倍数是b1。 Hankson 的“逆问题”就是求出满足条件的正整数x。但稍加思索之后，他发现这样的 x 并不唯一，甚至可能不存在。因此他转而开始考虑如何求解满足条件的x 的个数。请你帮 助他编程求解这个问题。

Input
    输入描述:
    　　输入第一行为一个正整数n，表示有n 组输入数据。

    　　接下来的n 行每 行一组输入数据，为四个正整数a0，a1，b0，b1，每两个整数之间用一个空格隔开。输入 数据保证a0 能被a1 整除，b1 能被b0 整除。
    输入样例:
    2
    41 1 96 288
    95 1 37 1776

Output
    输出描述:
    　　输出共n 行。每组输入数据的输出结果占一行，为一个整数。
    　　对于每组数据：若不存在这样的 x，请输出0； 若存在这样的 x，请输出满足条件的x 的个数；
    输出样例:
    6
    2
'''
n = int(input())
gys, gbs = 0, 0
count = 0

# 定义函数求最大公因数
def max_gys(m, a0):
    for i in range(1, min(m, a0)):
        if(m % i == 0 and a0 % i == 0):
            gys = i
        return gys
# 定义函数求最小公倍数
def min_gbs(m, b0):
    gbs = max_gys(m, b0) * (m // max_gys(m, b0)) * (b0 // max_gys(m, b0))
    return gbs

for i in range(n):
    a0, a1, b0, b1 = map(int, input().split())
    for x in range(1, 100000):
        if(max_gys(x, a0) == a1 and min_gbs(x, b0) == b1):
            count += 1
    print(count)


