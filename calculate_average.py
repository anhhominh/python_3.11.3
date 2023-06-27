def find_average(numbers):
    if len(numbers) == 0: 
        return 0
    average = 0
    for i in numbers:
        average = average + i
    return average/len(numbers)