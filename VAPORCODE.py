def vaporcode(s):
    ans = []
    for i in s:
        if i != " ":
            ans.append(i.upper())
    return "  ".join(ans)