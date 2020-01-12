'''
Description
　　输入一个正整数n，输出n!的值。
　　其中n!=1*2*3*…*n。

Input
    输入描述:
    　　n!可能很大，而计算机能表示的整数范围有限，需要使用高精度计算的方法。使用一个数组A来表示一个大整数a，A[0]表示a的个位，A[1]表示a的十位，依次类推。
    　　将a乘以一个整数k变为将数组A的每一个元素都乘以k，请注意处理相应的进位。
    　　首先将a设为1，然后乘2，乘3，当乘到n时，即得到了n!的值。
    输入样例:
    10

Output
    输出描述:
    　　输入包含一个正整数n，n<=1000。
    输出样例:
    3628800
'''
n = int(input())
a = s = 1

while a <= n:
    s *= a
    a += 1
print(s)

'''
# 更具题目提示，可以采用数组处理的方法
# 用数组来表示一个大整数a，其中list[0]表示a的个位，list[1]表示a的十位，以此类推
# 这样表示是为了防止a的值过大
'''

n = int(input())
a = [0 for i in range(10000)]
a[0] = length = 1
for i in range(2, n + 1):
    # carry表示仅为
    carry = 0
    for j in range(length):
        temp = a[j] * i + carry
        carry = int(temp / 10)
        a[j] = temp % 10
    while carry > 0:
        a[length] += carry % 10
        length += 1
        carry = int(carry / 10)

while length > 0:
    length -= 1
    print(a[length], end='')




