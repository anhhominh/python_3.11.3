def generate_shape(n):
    ans = []
    s = ''
    for i in range(0,n):
        s = s + '+'
    for i in range(0,n):
        ans.append(s)
    return '\n'.join(ans)