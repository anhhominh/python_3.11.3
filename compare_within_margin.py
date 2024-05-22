def close_compare(a, b, margin = None):
    if margin == None:
        margin = 0
    if abs(a-b) <= margin:
        return 0
    if a == b:
        return 0
    if a < b:
        return -1
    return 1