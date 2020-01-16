'''
Description
　　求出5个字符串中最长的字符串。每个字符串长度在100以内，且全为小写字母。

Input
    输入描述:

    输入样例: 
    one two three four five

Output
    输出描述: 
        输出样例: 
        three
'''
st = input().split()
list1 = []
max1 = 0
bx = 0

for i in range(len(st)):
    if(len(st[i]) > max1):
        max1 = len(st[i]) 
        bx = i

print(st[bx])