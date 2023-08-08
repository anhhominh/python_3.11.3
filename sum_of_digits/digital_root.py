def digital_root(n):
    while n >= 10:
        sum = 0
        while n>0:
            d = n % 10;
            sum = sum + d;
            n = n // 10
        n = sum 
    return n