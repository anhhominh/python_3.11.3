def func(x):
    ans = x.split(" ")
    return ans[1]


def sort_reindeer(reindeer_names):
    return sorted(reindeer_names, key=func)