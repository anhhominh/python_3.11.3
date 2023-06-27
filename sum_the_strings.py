# Sum The Strings
def sum_str(a, b):
    if a == '':
        a = '0'
    if b == '':
        b = '0'
    sum = int(a) + int(b)
    return str(sum)