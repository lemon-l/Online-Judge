'''
Description
　　秋天到了，n只猴子采摘了一大堆苹果放到山洞里，约定第二天平分。这些猴子很崇拜猴王孙悟空，所以都想给他留一些苹果。
    第一只猴子悄悄来到山洞，把苹果平均分成n份，把剩下的m个苹果吃了,然后藏起来一份，最后把剩下的苹果重新合在一起。
    这些猴子依次悄悄来到山洞，都做同样的操作，恰好每次都剩下了m个苹果。第二天，这些猴子来到山洞，把剩下的苹果分成n分，
    巧了，还是剩下了m个。问，原来这些猴子至少采了多少个苹果。

Input
    输入描述:
    　　两个整数，n m
    输入样例:
    5 1

Output
    输出描述:
    　　一个整数，表示原来苹果的数目
    输出样例:
    15621
''' 
'''
解题思路：
    一共分了n + 1, 然后每次都要私藏m个苹果，所以算出苹果树后，减掉私藏的即可
'''
n, m = map(int, input().split())
# 设总苹果数为t
t = 1
sum1 = n + 1

while(sum1):
    sum1 -= 1
    t *= n
print(t - ((n - 1) * m))

    

    

