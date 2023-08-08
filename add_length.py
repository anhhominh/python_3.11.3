def add_length(str_):
    ans = []
    s = str_.split(' ')
    for i in s:
        ans.append("{}".format(i) + " {}".format(len(i)))
    return ans