'''
Description
　　1221是一个非常特殊的数，它从左边读和从右边读是一样的，编程求所有这样的四位十进制数。

Input
    输入描述:
    　　按从小到大的顺序输出满足条件的四位十进制数。
    输入样例:
Output
    输出描述:
    输出样例: 
'''
# 判断是否为回文数
def palindrome(n):
    count = 0
    for i in range(len(n) // 2):
        if(n[i] == n[len(n) - 1 - i]):
            count += 1
        else:
            break
    if(count == 2):
        print(n)
            

for i in range(1000, 10000):
    palindrome(str(i))

''' The other answer '''

# def is_pal(i_):
#     i_s = str(i_)
#     if i_s == i_s[::-1]:
#         return True
#     else:
#         return False


# i = 1000
# while i < 10000:
#     if is_pal(i):
#         print(i)
#     i += 1
    
