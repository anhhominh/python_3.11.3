def check_exam(arr1,arr2):
    count = 0
    for i in range(len(arr1)):
        if arr2[i] == arr1[i]:
            count += 4
        elif arr2[i] != arr1[i] and arr2[i]  != "":
            count -= 1
    if count < 0:
        return 0
    return count