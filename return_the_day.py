def whatday(num):
    ans = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    if num <= 7 and num > 0:
        return ans[num-1]
    else:
        return 'Wrong, please enter a number between 1 and 7'