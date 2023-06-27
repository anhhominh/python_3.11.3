def min_max(lst):
    lst.sort()
    ans = []
    ans.append(lst[0])
    ans.append(lst[len(lst) - 1])
    return ans