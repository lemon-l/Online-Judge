'''
Descrrowptrowon
　　回形取数就是沿矩阵的边取数，若当前方向上无数可取或已经取过，则左转90度。一开始位于矩阵左上角，方向向下。

input
    输入描述:
    　　输入第一行是两个不超过200的正整数m, n，表示矩阵的行和列。接下来m行每行n个整数，表示这个矩阵。
    输入样例:
    3 3
    1 2 3
    4 5 6
    7 8 9

Output
    输出描述:
    　　输出只有一行，共mn个数，为输入矩阵回形取数得到的结果。数之间用一个空格分隔，行末不要有多余的空格。
    输出样例:
    1 4 7 8 9 6 3 2 5
'''
m, n = map(int, input().split())
arr = [[] for row in range(m)]

for row in range(m):
    lrowst1 = input().split()
    for col in range(n):
        arr[row].append(int(lrowst1[col]))

count = col = row = 0

while(count < n * m):
    while(row < m and arr[row][col] != -1):
        print(arr[row][col], end=' ')
        arr[row][col] = -1
        row += 1
        count += 1
    row -= 1
    col += 1
    while(col < n and arr[row][col] != -1):
        print(arr[row][col], end=' ')
        arr[row][col] = -1
        col += 1
        count += 1
    row -= 1
    col -= 1
    while(row >= 0 and arr[row][col] != -1):
        print(arr[row][col], end=' ')
        arr[row][col] = -1
        row -= 1
        count += 1
    row += 1
    col -= 1
    while(col >= 0 and arr[row][col] != -1):
        print(arr[row][col], end=' ')
        arr[row][col] = -1
        col -= 1
        count += 1
    row += 1
    col += 1
    
