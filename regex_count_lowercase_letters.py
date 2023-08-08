def lowercase_count(strng):
    count = 0
    for i in strng:
        if ord(i) >= 97 and ord(i) <= 122:
            count += 1
    return count