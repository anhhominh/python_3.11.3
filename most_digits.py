def find_longest(arr):
    max = ""
    for i in arr:
        num = str(i)
        if len(num) > len(max):
            max = num
    return int(max)