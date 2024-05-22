def two_highest(arg1):
    print(arg1)
    arg1 = list(set(arg1))
    arg1.sort()
    print(arg1)
    ans = []
    if len(arg1) >= 2:
        ans.append(arg1[len(arg1) - 1])
        ans.append(arg1[len(arg1) - 2])
    elif len(arg1) >= 1:
        ans.append(arg1[len(arg1) - 1])
    return ans