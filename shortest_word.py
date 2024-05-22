def find_short(s):
    ans = s.split(' ')
    min = len(ans[0])
    for i in ans:
        if len(i) < min:
            min = len(i)
    return min