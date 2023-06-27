def replace_exclamation(s):
    str = 'aeiouAEIOU' 
    for i in str:
        for j in s:
            if i == j:
                s = s.replace(j,'!')
    return s