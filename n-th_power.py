def index(array, n):
    if len(array) - 1 < n:
        return -1
    else:
        return pow(array[n],n)