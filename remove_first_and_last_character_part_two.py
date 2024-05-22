def array(string):
    s = string.split(',')
    if len(s) >= 3:
        return " ".join(s[1:len(s)-1])
    return None