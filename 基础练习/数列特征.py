'''
Description
    给出n个数，找出这n个数的最大值，最小值，和。
    
Input
    输入描述:
    第一行为整数n，表示数的个数。
    第二行有n个数，为给定的n个数，每个数的绝对值都小于10000。
    输入样例:
    5
    1 3 -2 4 5

Output
    输出描述:
    输出三行，每行一个整数。第一行表示这些数中的最大值，第二行表示这些数中的最小值，第三行表示这些数的和。
    输出样例:
            5
            -2
            11
'''
n = int(input())
array = list(map(int, input().split()))
print(max(array))
print(min(array))
print(sum(array))