def words_to_marks(s):
    sum = 0
    for i in s:
        sum = sum + ord(i) - 96
    return sum