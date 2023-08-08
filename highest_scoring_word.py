def high(x):
    arr = x.split(' ')
    numArr = []
    for val in arr:
        intNum = 0
        letters = list(val)
        for word in letters:
            intNum += ord(word) - 96
        numArr.append(intNum)
    return arr[numArr.index(max(numArr))]