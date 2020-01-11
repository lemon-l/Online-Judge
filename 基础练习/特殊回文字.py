def is_pal(i_):
    i_s = str(i_)
    if i_s == i_s[::-1]:
        return True
    else:
        return False


def sum_i(i_):
    s = 0
    i_s = str(i)
    for j in range(len(i_s)):
        s += int(i_s[j])
    return s

n = int(input())
i = 10000
while i < 1000000:
    if is_pal(i):
        if sum_i(i) == n:
            print(i)
    i += 1


