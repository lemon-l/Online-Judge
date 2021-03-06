'''
Description
　　首先给出简单加法算式的定义：
　　如果有一个算式(i)+(i+1)+(i+2),(i>=0)，在计算的过程中，没有任何一个数位出现了进位，则称其为简单的加法算式。
　　例如：i=3时，3+4+5=12，有一个进位，因此3+4+5不是一个简单的加法算式；又如i=112时，112+113+114=339，没有在任意数位上产生进位，故112+113+114是一个简单的加法算式。

　　问题：给定一个正整数n，问当i大于等于0且小于n时,有多少个算式(i)+(i+1)+(i+2)是简单加法算式。其中n<10000。

Input
    输入描述:
    　　一个整数，表示n 
    输入样例: 

Output
    输出描述: 
    　　一个整数,表示简单加法算式的个数
    输出样例: 
'''
n = int(input())
'''
要想满足条件则:
    最高位取值为1,2,3
    个位的取值为0,1,2
    其余为可取值0,1,2,3
'''
qian, bai, shi, ge, count = 0, 0, 0, 0, 0
for i in range(n):
    qian = i / 1000
    bai = i % 1000 / 100
    shi = i % 100 / 10
    ge = i % 10
    if(ge <= 2 and shi <= 3 and bai <= 3 and qian <= 3):
        count += 1
print(count)