'''
Description
　　给定某整数数组和某一整数b。要求删除数组中可以被b整除的所有元素，同时将该数组各元素按从小到大排序。如果数组元素数值在A到Z的ASCII之间，替换为对应字母。元素个数不超过100，b在1至100之间。

Input
    输入描述:
    　　第一行为数组元素个数和整数b
    　　第二行为数组各个元素 
    输入样例: 

Output
    输出描述: 
    　　按照要求输出
    输出样例: 
'''
num, b = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list1.copy()

for i in list2:
    if(i % b == 0):
        list1.remove(i)
list1.sort()
for i in list1:
    if(i >= ord('A') and i <= ord('Z')):
        i = chr(i)
    print(i, end = ' ')
