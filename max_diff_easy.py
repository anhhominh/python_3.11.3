def max_diff(lst):
    if len(lst) > 1:
        return max(lst) - min(lst)
    return 0