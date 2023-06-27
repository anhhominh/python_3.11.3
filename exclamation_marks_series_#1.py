def remove(s):
    if s == "":
        return s
    ans = ""
    if s[len(s) - 1] == '!':
        for i in range(0,len(s) - 1):
            ans = ans + s[i]
        return ans
    return s