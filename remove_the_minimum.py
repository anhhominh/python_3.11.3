def remove_smallest(numbers):
    if numbers is None or len(numbers) == 0:
        return []
    copy = numbers.copy()
    copy.remove(min(numbers))
    return copy