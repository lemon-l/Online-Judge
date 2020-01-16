'''
Description
　　设有有2 n（n<=6）个球队进行单循环比赛，计划在2 n – 1天内完成，每个队每天进行一场比赛。设计一个比赛的安排，使在2 n – 1天内每个队都与不同的对手比赛。

Input
    输入描述:
    　　输入文件matchplan.in共一行，输入n的数值。 
    输入样例: 
    2

Output
    输出描述: 
    　　输出文件matchplan.out共（2 n – 1）行，第i行输出第i天的比赛安排。
    　　格式为：<i> A-B，C-D，……。其中i是天数，A，B分别为比赛双方的编号，每行共2 n-1个比赛场次。
    输出样例: 
    <1>1-2,3-4
    <2>1-3,2-4
    <3>1-4,2-3
'''
'''
做题思路：
    1. 队伍序号小的先安排比赛，每天2^(n - 1)个队伍比赛
    2. 每个队伍向后挑选最近队伍的比赛，标记今天是否必过赛，是否这两个队伍比过赛
'''
a = int(input())
b = 2**a

list2 = [0 for x in range(10000)]

for i in range(1, b):
    count = 0
    list1 = [0 for x in range(10000)]
    print('<{0}>'.format(i), end='')
    for j in range(1, b + 1):
        if(list1[j] == 0):
            for k in range(j + 1, b + 1):
                if(list2[j * 100 + k] == 0 and list1[k] == 0):
                    list2[j * 100 + k] = 1
                    list1[j] = list1[k] = 1
                    count += 1
                    if(count != 2**(a - 1)):
                        print('{0}-{1},'.format(j, k), end='')
                    else:
                        print('{0}-{1}'.format(j, k), end='')
                    break
    print()





