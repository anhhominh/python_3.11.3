def small_enough(array, limit):
    array.sort()
    if array[len(array) - 1] <= limit:
        return True
    return False