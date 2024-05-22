def remove(s, n):
    while n > 0:
        s = s.replace('!','',1)
        n = n -1
    return s