'''
Description
杨辉三角形又称Pascal三角形，它的第i+1行是(a+b)i的展开式的系数。
它的一个重要性质是：三角形中的每个数字等于它两肩上的数字相加。
下面给出了杨辉三角形的前4行：
   1
  1 1
 1 2 1
1 3 3 1
给出n，输出它的前n行。

Input
    输入描述:
    输入包含一个数n。
    输入样例:
    4

Output
    输出描述:
    输出杨辉三角形的前n行。每一行从这一行的第一个数开始依次输出，中间使用一个空格分隔。请不要在前面输出多余的空格。
    输出样例:
    1
    1 1
    1 2 1
    1 3 3 1
'''
def createL(l): # 生成杨辉三角的一行
    L = [1]
    for x in range(1, len(l)):
        L.append(l[x] + l[x-1])
    L.append(1)
    return L
 
 
def printL(L): # 打印
    s = ""
    for x in L:
        s += str(x) + " "
    print(s)
 
 
L = [1]
row = int(input("输入行数："))
for x in range(row):
    printL(L)
    L = createL(L)