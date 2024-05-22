def is_sorted_and_how(arr):
    check_1 = False
    check_2 = False
    # yes, ascending
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                check_1 = True
                break
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] < arr[j]:
                check_2 = True
                break
    if check_1 == False and check_2 == True:
        return 'yes, ascending'
    elif check_1 == True and check_2 == False:
        return 'yes, descending'
    else:
        return 'no'