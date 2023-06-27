def str_count(strng, letter):
    dem = 0
    for i in strng:
        if i == letter:
            dem += 1
    return dem