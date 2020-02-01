'''
Description
　　Tom教授正在给研究生讲授一门关于基因的课程，有一件事情让他颇为头疼：一条染色体上有成千上万个碱基对，它们从0开始编号，到几百万，几千万，甚至上亿。
　　比如说，在对学生讲解第1234567009号位置上的碱基时，光看着数字是很难准确的念出来的。
　　所以，他迫切地需要一个系统，然后当他输入12 3456 7009时，会给出相应的念法：
　　十二亿三千四百五十六万七千零九
　　用汉语拼音表示为
　　shi er yi san qian si bai wu shi liu wan qi qian ling jiu
　　这样他只需要照着念就可以了。
　　你的任务是帮他设计这样一个系统：给定一个阿拉伯数字串，你帮他按照中文读写的规范转为汉语拼音字串，相邻的两个音节用一个空格符格开。
　　注意必须严格按照规范，比如说“10010”读作“yi wan ling yi shi”而不是“yi wan ling shi”，“100000”读作“shi wan”而不是“yi shi wan”，“2000”读作“er qian”而不是“liang qian”。

Input
    输入描述:
    　　有一个数字串，数值大小不超过2,000,000,000。
    输入样例:
    1234567009

Output
    输出描述:
    　　是一个由小写英文字母，逗号和空格组成的字符串，表示该数的英文读法。
    输出样例:
    shi er yi san qian si bai wu shi liu wan qi qian ling jiu
'''

'''
    此题是参考别人的答案。
'''
n = input()

pin_yin = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si', '5': 'wu',
           '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu'}
pin_yin_2 = {0: '', 1: '', 2: 'shi', 3: 'bai', 4: 'qian', 5: 'wan', 6: 'shi',
             7: 'bai', 8: 'qian', 9: 'yi', 10: 'shi'}
n = n + ' '

l = len(n) - 1

for i in range(l):
    j = int(n[i])
    if j != 0:  # 不为0时的读法
        if (l - i == 2 or l - i == 6 or l - i == 10) and j == 1:
            # 在十位，十万位，十亿位置且位于开头的1不读
            # 例子：
            # 1111111111 会读出 yi shi yi yi yi qian yi bai yi shi yi wan yi qian yi bai yi shi yi
            # 111111 会读出 yi shi yi wan yi qian yi bai yi shi yi
            # 11 会读出 yi shi yi
            # 加上此约束后，则不会读出开头的 yi
            if i != 0:  # 第一个1不输出1， 若不添加此条件，12会读出 yi shi er
                print(pin_yin['1'], end=' ')
            print(pin_yin_2[2], end=' ')
            continue
        print(pin_yin[n[i]], end=' ')
        print(pin_yin_2[l - i], end=' ')
    else:  # 处理0的读法问题
        if l - i == 5 or l - i == 9:  # 如果此0是在万位或亿位，则读出万或亿
            print(pin_yin_2[l - i], end=' ')
        if n[i + 1] == '0' or i == l - 1:  # 如果后一位仍然为0，或者，当前是最后以为，则不读此0
            continue
        print(pin_yin['0'], end=' ')  # 否则才读出这个零
    