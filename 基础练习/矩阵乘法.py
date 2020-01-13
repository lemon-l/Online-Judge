'''
Description
　　给定一个N阶矩阵A，输出A的M次幂（M是非负整数）
　　例如：
　　A =
　　1 2
　　3 4
　　A的2次幂
　　7 10
　　15 22

Input
    输入描述:
    　　第一行是一个正整数N、M（1<=N<=30, 0<=M<=5），表示矩阵A的阶数和要求的幂数
    　　接下来N行，每行N个绝对值不超过10的非负整数，描述矩阵A的值
    输入样例:
    2 2
    1 2
    3 4

Output
    输出描述:
    　　输出共N行，每行N个整数，表示A的M次幂所对应的矩阵。相邻的数之间用一个空格隔开
    输出样例:
    7 10
    15 22
'''

'''
我服了，为什么会显示runtime error
'''
N, M = map(int, input().split())
# 定义一个多阶列表
list1 = [[] for i in range(N)]
# 将键盘输入的数组转入多阶列表中
for i in range(N):
    arr = input().split()
    for j in range(N):
        list1[i].append(int(arr[j]))

# 定义multiply函数执行阶乘的计算
def multiply(N, result, list1):
    list2 = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            for m in range(N):
                list2[i][j] += list1[i][m]*result[m][j]
    return list2

# 调用计算阶乘的函数
if(M == 0): # 必须考虑单位矩阵
    result = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        result[i][i] = 1
else: # 如果幂不为0,则计算他的M次幂
    result = list1
    for i in range(M - 1):
        result = multiply(N, result, list1)

# 打印出result列表里面的数组
for i in range(len(result[0])):
    for j in range(len(result[1])):
        print(result[i][j], end=' ')
    print()

# 下面是在网上借鉴的代码，提交成功了，但是我觉得那个形状没有什么必要。
'''
def multi_rect(rect_1, shape_1, rect_2, shape_2):
    """矩阵乘法
    :param rect_1: 矩阵A
    :param shape_1: 矩阵A的形状
    :param rect_2: 矩阵B
    :param shape_2: 矩阵B的形状
    :return: 两矩阵之积和积的矩阵形状
    """
    if shape_1[1] != shape_2[0]:
        return
    rect_ = [[0 for _ in range(shape_2[1])] for _ in range(shape_1[0])]
    shape_ = (shape_1[0], shape_2[1])
    for i in range(shape_1[0]):
        for k in range(shape_2[1]):
            for j in range(shape_1[1]):
                rect_[i][k] += rect_1[i][j] * rect_2[j][k]  # 矩阵乘法定义

    return rect_, shape_


n, m = map(int, input().split())

rect = [[] for _ in range(n)]

for i in range(n):
    arr = input().split()
    for j in range(n):
        rect[i].append(int(arr[j]))

result, shape = rect, (n, n)

if m == 0:  # 0次幂只有为方阵才有，此时result为n阶单位阵
    result = [[0 for _ in range(n)] for _ in range(n)]  # shape仍然为(n, n)
    for i in range(n):
        result[i][i] = 1
else:  # m不为0，计算它的m次幂
    for _ in range(m - 1):
        result, shape = multi_rect(rect, (n, n), result, shape)

for i in range(shape[0]):
    for j in range(shape[1]):
        print(result[i][j], end=' ')
    print()
'''
    

