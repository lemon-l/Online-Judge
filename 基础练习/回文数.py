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
    
