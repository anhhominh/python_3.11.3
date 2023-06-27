def fake_bin(x):
    mylist= list(x)
    ans = ''
    for i in mylist:
        if int(i) < 5 :
            ans = ans + '0'
        else:
            ans = ans + '1'
    return ans