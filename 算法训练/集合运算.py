'''
Description
　　给出两个整数集合A、B，求出他们的交集、并集以及B在A中的余集。

Input
    输入描述:
    　　第一行为一个整数n，表示集合A中的元素个数。
    　　第二行有n个互不相同的用空格隔开的整数，表示集合A中的元素。
    　　第三行为一个整数m，表示集合B中的元素个数。
    　　第四行有m个互不相同的用空格隔开的整数，表示集合B中的元素。
    　　集合中的所有元素均为int范围内的整数，n、m<=1000。 
    输入样例: 
    5
    1 2 3 4 5
    5
    2 4 6 8 10

Output
    输出描述: 
    　　第一行按从小到大的顺序输出A、B交集中的所有元素。
    　　第二行按从小到大的顺序输出A、B并集中的所有元素。
    　　第三行按从小到大的顺序输出B在A中的余集中的所有元素。
    输出样例: 
    2 4
    1 2 3 4 5 6 8 10
    1 3 5
'''
m = int(input())
A = list(map(int, input().split()))
n = int(input())
B = list(map(int, input().split()))
# 求交集
ret1 = sorted([i for i in B if i in A])
for i in ret1:
    print(i, end=' ')
print()
# 求并集
ret2 = sorted(list(set(A).union(set(B))))
for i in ret2:
    print(i, end= ' ')
print()
# 求差集A - B
ret3 = sorted([i for i in A if i not in B])
for i in ret3:
    print(i, end=' ')
