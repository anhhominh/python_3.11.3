def pipe_fix(nums):
    ans = []
    minN = min(nums)
    maxN = max(nums)
    for i in range(minN, maxN + 1):
        ans.append(i)
    return ans