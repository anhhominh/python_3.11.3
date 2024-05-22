def spacify(string):
    ans = []
    if len(string) <= 1:
        return string
    for i in string:
        ans.append(i)
    return ' '.join(ans)