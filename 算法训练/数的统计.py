'''
Description
　　在一个有限的正整数序列中，有些数会多次重复出现在这个序列中。
　　如序列：3，1，2，1，5，1，2。其中1就出现3次，2出现2次，3出现1 次，5出现1次。
　　你的任务是对于给定的正整数序列，从小到大依次输出序列中出现的数及出现的次数。

Input
    输入描述:
    　　第一行正整数n，表示给定序列中正整数的个数。
    　　第二行是n 个用空格隔开的正整数x，代表给定的序列。
    输入样例:
    12
    8 2 8 2 2 11 1 1 8 1 13 13

Output
    输出描述:
    　　若干行，每行两个用一个空格隔开的数，第一个是数列中出现的数，第二个是该数在序列中出现的次数。
    输出样例:
    1 3
    2 3
    8 3
    11 1
    13 2
'''
n = int(input())
list1 = list(map(int, input().split()))
# 统计每一个数字出现的次数， 数字作为key，出现的次数作为值
result = {}
for i in list1:
    if i in result.keys():
        result[i] += 1
    else:
        result[i] = 1
result1 = sorted(result.items(), key=lambda item: item[0])
# 排序后result1为一个列表，里面是元组
for i in result1:
    print('{0} {1}'.format(i[0], i[1]))