def series_sum(n):
    total = 0
    dem = 0
    i = 1
    while(dem < n):
        total = total + 1/i
        i += 3
        dem += 1
    return "{:.{}f}".format( total, 2 ) 