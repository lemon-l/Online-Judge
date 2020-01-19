'''
Description
　　涛涛立志要做新好青年，他最近在学做菜。由于技术还很生疏，他只会用鸡蛋，西红柿，鸡丁，辣酱这四种原料来做菜，我们给这四种原料标上字母A,B,C,D。
　　涛涛现在会做的菜有五种：
　　1、 西红柿炒鸡蛋 原料：AABDD
　　2、 酸辣鸡丁 原料：ABCD
　　3、 宫保鸡丁 原料：CCD
　　4、 水煮西红柿 原料：BBB
　　5、 怪味蛋 原料：AD
　　这天早上，开开去早市给涛涛买了一些原料回来。由于事先没有什么计划，涛涛决定，对于现存的原料，每次尽量做菜单上靠前（即编号小）的菜。
　　现在请你写一个程序，判断一下开开和涛涛中午能吃到哪些菜。

Input
    输入描述:
    　　共4个整数a,b,c,d。分别表示开开买的A,B,C,D这4种原料的数量。每种原料不会超过30份。
    输入样例:
    3
    1
    2
    4

Output
    输出描述:
    　　输出5行。其中第i行表示涛涛做的第i种菜的数目。
    输出样例:
    1
    0
    1
    0
    1
'''
'''
实在忍不了le,这道题有毒，明明只有两个人为什么要重复做一道菜，多吃几道他不香吗？
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
count1, count2, count3, count4, count5 = 0, 0, 0, 0, 0

while(a >= 2 and b >= 1 and d >= 2):
    a -= 2
    b -= 1
    d -= 2
    count1 += 1

while(a >= 1 and b >= 1 and c >= 1 and d >= 1):
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    count2 += 1
while(c >= 2 and d >= 1):
    c -= 2
    d -= 1
    count3 += 1
while(b >= 3):
    b -= 3
    count4 += 1
while(a >= 1 and d >= 1):
    a -= 1
    d -= 1
    count5 += 1
print('{0}\n{1}\n{2}\n{3}\n{4}'.format(count1, count2, count3, count4, count5))

