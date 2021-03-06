'''
Description
　　给定一个以秒为单位的时间t，要求用“<H>:<M>:<S>”的格式来表示这个时间。<H>表示时间，<M>表示分钟，而<S>表示秒，它们都是整数且没有前导的“0”。例如，若t=0，则应输出是“0:0:0”；若t=3661，则输出“1:1:1”。

Input
    输入描述:
    　　输入只有一行，是一个整数t（0<=t<=86399）。
    输入样例:
    0

Output
    输出描述:
    　　输出只有一行，是以“<H>:<M>:<S>”的格式所表示的时间，不包括引号。
    输出样例:
    0:0:0
'''
n = int(input())

H = n // 3600
M = (n % 3600) // 60
S = (n % 3600) % 60
print('{0}:{1}:{2}'.format(H, M, S))