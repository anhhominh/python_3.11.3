def sum_of_minimums(numbers):
    total = 0
    for x in numbers:
        total = total + min(x)
    return total