'''
Description
　　有一份提货单，其数据项目有：商品名（MC）、单价（DJ）、数量（SL）。定义一个结构体prut，其成员是上面的三项数据。在主函数中定义一个prut类型的结构体数组，输入每个元素的值，计算并输出提货单的总金额。
　　输入格式：第一行是数据项个数N(N<100)，接下来每一行是一个数据项。商品名是长度不超过100的字符串，单价为double类型，数量为整型。
　　输出格式：double类型的总金额。
    输入：
    　　4
    　　book 12.5 3
    　　pen 2.5 10
    　　computer 3200 1
    　　flower 47 5

输出：
　　3497.500000

Input
    输入描述:
    输入样例:

Output
    输出描述:
    输出样例: 
'''
n = int(input())
sum1 = 0
for i in range(n):
    MC, DJ, SL = list(input().split())
    sum1 += float(DJ) * float(SL)
print('{0:.6f}'.format(sum1))