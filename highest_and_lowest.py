def high_and_low(numbers):
    str = numbers.split( )
    num = []
    for i in str:
        num.append(int(i))
    num.sort()
    return f"{num[len(num)-1]} {num[0]}"