def persistence(n):
    count = 0
    while n >= 10:
        tmp = 1
        while n>0:
            d = n % 10
            tmp = tmp * d
            n = n // 10
        count += 1
        n = tmp
    return count