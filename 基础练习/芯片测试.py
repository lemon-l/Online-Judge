'''
Description
　　有n（2≤n≤20）块芯片，有好有坏，已知好芯片比坏芯片多。
　　每个芯片都能用来测试其他芯片。用好芯片测试其他芯片时，能正确给出被测试芯片是好还是坏。而用坏芯片测试其他芯片时，会随机给出好或是坏的测试结果（即此结果与被测试芯片实际的好坏无关）。
　　给出所有芯片的测试结果，问哪些芯片是好芯片。

Input
    输入描述:
    　　输入数据第一行为一个整数n，表示芯片个数。
    　　第二行到第n+1行为n*n的一张表，每行n个数据。表中的每个数据为0或1，在这n行中的第i行第j列（1≤i, j≤n）的数据表示用第i块芯片测试第j块芯片时得到的测试结果，1表示好，0表示坏，i=j时一律为1（并不表示该芯片对本身的测试结果。芯片不能对本身进行测试）。
    输入样例:
    3
    1 0 1
    0 1 0
    1 0 1

Output
    输出描述:
    　　按从小到大的顺序输出所有好芯片的编号
    输出样例:
    1 3
'''
'''
    重点是好芯片比坏芯片多
    如果忽略这个问题就很难解决，本人开始你就不幸忽略了。。。
    既然好芯片比坏芯片多，那么我们只需记录每一列0的个数就行了，若个数超过n/2，则此芯片为坏芯片
    一个chip列表来记录芯片的好坏
'''
n = int(input())
arr = [[] for i in range(n)]
judge = [True for i in range(n)]

# 先将数组写入列表里面
for i in range(n):
    list1 = input().split()
    for j in range(n):
        arr[i].append(int(list1[j]))

for i in range(n):
    count = 0
    for j in range(n):
        if(arr[j][i] == 0):
            count += 1
    if(count > n / 2):
        judge[i] = False

for i in range(n):
    if(judge[i]):
        print(i + 1, end=' ')