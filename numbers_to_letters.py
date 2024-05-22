def switcher(arr):
    ans = ''
    for i in arr:
        if i == '27':
            ans = ans + '!'
        elif i == '28':
            ans = ans + '?'
        elif i == '29':
            ans = ans + ' '
        else:
            ans = ans + chr(123 - int(i))
    return ans