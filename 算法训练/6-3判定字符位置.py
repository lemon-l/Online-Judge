'''
Description
　　返回给定字符串s中元音字母的首次出现位置。英语元音字母只有‘a’、‘e’、‘i’、‘o’、‘u’五个。
　　若字符串中没有元音字母，则返回0。
　　只考虑小写的情况。

Input
    输入描述:

    输入样例:
    and

Output
    输出描述:

    输出样例:
    1
'''
s = input()
vowel = ['a', 'e', 'i', 'o', 'u']
count = 0
for i in range(len(s)):
    if s[i] in vowel:
        print(i + 1)
        count += 1
        break
if count == 0:
    print('0')
