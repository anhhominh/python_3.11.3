def sum_digits(number):
    num = list(map(int, str(abs(number))))
    total = 0
    for i in range(0,len(num)):
        total += int(num[i])
    return total