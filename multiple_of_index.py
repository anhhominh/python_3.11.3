def multiple_of_index(arr):
    ans = []
    if arr[0] == 0:
        ans.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] % i == 0:
            ans.append(arr[i])
    return ans