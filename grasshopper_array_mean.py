def find_average(nums):
    if nums == []:
        return 0
    sum = 0
    for i in nums:
        sum = sum + i
    return sum / len(nums)