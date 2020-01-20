'''
Description
　　编写一个程序，输入三个正整数min、max和factor，然后对于min到max之间的每一个整数（包括min和max），如果它能被factor整除，就把它打印出来。
　　输入格式：输入只有一行，包括三个整数min、max和factor。
　　输出格式：输出只有一行，包括若干个整数。
　　输入输出样例

Input
    输入描述:
    输入样例:
    1 10 3

Output
    输出描述:
    输出样例:
    3 6 9
'''
Min, Max, Factor = map(int, input().split())
for i in range(Min, Max + 1):
    if(i % Factor == 0):
        print(i, end=' ')