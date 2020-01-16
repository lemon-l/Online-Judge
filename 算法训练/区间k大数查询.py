'''
Description
    给定一个序列，每次询问序列中第l个数到第r个数中第K大的数是哪个。


Input
    输入描述:
    第一行包含一个数n，表示序列长度。
    第二行包含n个正整数，表示给定的序列。
    第三个包含一个正整数m，表示询问个数。
    接下来m行，每行三个数l,r,K，表示询问序列从左往右第l个数到第r个数中，从大往小第K大的数是哪个。序列元素从1开始标号。
    输入样例: 
    5
    1 2 3 4 5
    2
    1 5 2
    2 3 2

Output
    输出描述: 
    总共输出m行，每行一个数，表示询问的答案。 
    输出样例: 
    4
    2
'''
n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list3 = []

for i in range(m):
    list2 = []
    l, r, k = map(int, input().split())
    list2 = list1[l - 1: r]
    list2.sort(reverse= True)
    print(list2[k - 1])