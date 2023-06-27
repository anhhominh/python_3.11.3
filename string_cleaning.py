def string_clean(s):
    for x in s:
        print(x)
        if ord(x) >= 48 and ord(x) <= 57:
            s = s.replace(x, '')
    return s