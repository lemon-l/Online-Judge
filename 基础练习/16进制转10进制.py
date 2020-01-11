'''
Description
　　从键盘输入一个不超过8位的正的十六进制数字符串，将它转换为正的十进制数后输出。
　　注：十六进制数中的10~15分别用大写的英文字母A、B、C、D、E、F表示。

Input
    输入描述:
    输入样例:
    FFFF

Output
    输出描述:
    输出样例:
    65535
'''
hexa = input()
print(int(hexa, 16))

