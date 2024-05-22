def sequence_sum(begin_number, end_number, step):
    sum = 0
    for i in range(begin_number, end_number + 1, step):
        print(i)
        sum = sum + i
    return sum