def switcheroo(s):
    ans = ""
    for i in s:
        if i == 'a':
            ans = ans + 'b'
            continue
        elif i == 'b':
            ans = ans + 'a'
            continue
        else:
            ans = ans + i
    return ans