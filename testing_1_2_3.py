def number(lines):
    ans = []
    for i in range(1,len(lines) + 1):
        tmp = str(i)
        ans.append(tmp +": "+lines[i-1])
    return ans