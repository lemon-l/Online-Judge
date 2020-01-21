'''
Description
　　读入10个复数，建立对应链表，然后求所有复数的和。

Input
    输入描述:

    输入样例:
    1 2
    1 3
    4 5
    2 3
    3 1
    2 1
    4 2
    2 2
    3 3
    1 1

Output
    输出描述:

    输出样例:
    23+23i
'''
former = [0 for x in range(10)]
latter = [0 for x in range(10)]
for i in range(10):
    former[i], latter[i] = map(int, input().split())
print('{0}+{1}i'.format(sum(former), sum(latter)))