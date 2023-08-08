def abbrevName(name):
    first, last = name.upper().split(' ')
    f = first[0]
    l = last[0]
    return f + '.' + l