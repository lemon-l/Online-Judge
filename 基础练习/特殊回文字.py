'''
Description
　　123321是一个非常特殊的数，它从左边读和从右边读是一样的。
　　输入一个正整数n， 编程求所有这样的五位和六位十进制数，满足各位数字之和等于n 。

Input
    输入描述:
    　　输入一行，包含一个正整数n。
    输入样例:
    52

Output
    输出描述:
    　　按从小到大的顺序输出满足条件的整数，每个整数占一行。
        输出样例:
        899998
        989989
        998899
'''
def is_pal(i_):
    i_s = str(i_)
    if i_s == i_s[::-1]:
        return True
    else:
        return False


def sum_i(i_):
    s = 0
    i_s = str(i)
    for j in range(len(i_s)):
        s += int(i_s[j])
    return s

n = int(input())
i = 10000
while i < 1000000:
    if is_pal(i):
        if sum_i(i) == n:
            print(i)
    i += 1


