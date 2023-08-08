def get_even_numbers(arr):
    ans = []
    for i in arr:
        if i % 2 == 0:
            ans.append(i)
    return ans