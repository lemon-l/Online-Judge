def judge(n):
    s = 0
    for i in range(len(n)):
        s += pow(int(n[i]), 3)
    if(s == int(n)):
        print(n)

for i in range(100, 1000):
    judge(str(i))