def sum_array(arr):
    if arr == None:
        return 0
    if len(arr) <= 1:
        return 0
    minA = min(arr)
    maxA = max(arr)
    arr.remove(minA)
    arr.remove(maxA)
    sum = 0
    for i in arr:
        sum += i
    return sum