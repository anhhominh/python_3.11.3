def merge_arrays(arr1, arr2):
    ans = arr1 + arr2
    ans_set = set(ans)
    ans_1 = list(ans_set)
    ans_1.sort()
    return ans_1