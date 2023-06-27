def reverse(st):
    num = st.split(' ')
    s = []
    for i in num:
        if i != ' ' and i != '':
            s.append(i)
    
    ans = list(reversed(s))
    
    print(ans)
    return ' '.join(ans)