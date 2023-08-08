def find_multiples(integer, limit):
    ans = []
    for i in range(integer, limit + 1, integer):
        ans.append(i)
    return ans