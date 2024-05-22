def stringy(size):
    ans = []
    for i in range(0,size):
        if i % 2 == 0:
            ans.append('1')
        else:
            ans.append('0')
    return ''.join(ans)