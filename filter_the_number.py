def filter_string(string):
    ans = ""
    for i in string:
        if ord(i) >= 48 and ord(i) <= 57:
            ans = ans + i
    return int(ans)