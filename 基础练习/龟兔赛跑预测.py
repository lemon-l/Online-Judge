
v1, v2, t, s, l = input().split()

# 乌龟跑步用的时间
time2 = l / v2
# 兔子不休息的情况下跑步用的时间
time1 = l / v1

for i in range(time1):
    if(v1 * i - v2 * i >= t):
        time1 += s
        

    
if(time1 > time2):
    print('T')
elif(time1 < time2):
    print('R')
elif(time1 == time2):
    print('D')

