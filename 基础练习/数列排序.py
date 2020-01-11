'''
Description
　　给定一个长度为n的数列，将这个数列按从小到大的顺序排列。1<=n<=200

Input
    输入描述:
    　　第一行为一个整数n。
    　　第二行包含n个整数，为待排序的数，每个整数的绝对值小于10000。
        输入样例:
        5
        8 3 6 4 9

Output
    输出描述:
    　　输出一行，按从小到大的顺序输出排序后的数列。
    输出样例:
        3 4 6 8 9
'''
length = int(input())
# 这里的map函数是对后面的列表进行操作，将里面的字符转换为字符串，
# 但是由于map没有sort属性，所以要将他转换为list格式
array = list(map(int, input().split())) 
array.sort()
for i in range(len(array)):
    print(array[i], end=' ')


# map函数是python内置的高阶函数，对传入的list的每一个元素进行映射,
# 返回一个新的映射之后的list