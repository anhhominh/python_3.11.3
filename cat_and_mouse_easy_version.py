def cat_mouse(x):
    count = 0
    for i in x:
        if i == '.':
            count = count + 1
    if count > 3:
        return "Escaped!"
    return "Caught!"