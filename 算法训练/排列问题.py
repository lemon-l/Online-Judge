'''
Description
　　求一个0～N-1的排列（即每个数只能出现一次），给出限制条件（一张N*N的表，第i行第j列的1或0，表示为j-1这个数不能出现在i-1这个数后面，并保证第i行第i列为0），将这个排列看成一个自然数，求从小到大排序第K个排列。

Input
    输入描述:
    　　N<=10，K<=500000
    输入样例:

Output
    输出描述:
    　　第一行为N和K,接下来的N行，每行N个数，0表示不能，1表示能
    输出样例: 
'''
N, K = map(int, input().split())
list1 = [(0 for x in range(N)) for y in range(N)]
