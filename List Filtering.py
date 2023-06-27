def filter_list(l):
    ans = []
    for i in l:
        if type(i) == int:
            ans.append(i)
    return ans