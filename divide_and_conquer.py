def div_con(x):
    sum1 = 0
    sum2 = 0
    for i in x:
        if type(i) == type(0):
            sum1 = sum1 + i
        else:
            sum2 = sum2 + int(i)
    print(sum1)
    print(sum2)
    return sum1 - sum2