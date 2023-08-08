def sum_two_smallest_numbers(numbers):
    numbers.sort()
    if len(numbers) >= 1:
        return numbers[0] + numbers[1]