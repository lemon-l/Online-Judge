'''
Description
　　定义一个学生结构体类型student，包括4个字段，姓名、性别、年龄和成绩。然后在主函数中定义一个结构体数组（长度不超过1000），并输入每个元素的值，程序使用冒泡排序法将学生按照成绩从小到大的顺序排序，然后输出排序的结果。
　　输入格式：第一行是一个整数N（N<1000），表示元素个数；接下来N行每行描述一个元素，姓名、性别都是长度不超过20的字符串，年龄和成绩都是整型。
　　输出格式：按成绩从小到大输出所有元素，若多个学生成绩相同则成绩相同的同学之间保留原来的输入顺序。
    输入：
    　　3
    　　Alice female 18 98
    　　Bob male 19 90
    　　Miller male 17 92

    输出：
    　　Bob male 19 90
    　　Miller male 17 92
    　　Alice female 18 98
'''
'''
没有错呀，为啥显示wrong answer
'''
n = int(input())
list1 = [['' for i in range(4)] for j in range(n)]
for i in range(n):
    list1[i] = input().split()

def by_score(t):
    return int(t[3])
L = sorted(list1, key = by_score)
for i in L:
    for j in i:
        print(j, end= ' ')
    print()

