def is_vow(inp):
    for value, unicode_value in enumerate(inp):
        if unicode_value == 97:
            inp[value] = 'a'
        if unicode_value == 101:
            inp[value] = 'e'
        if unicode_value == 105:
            inp[value] = 'i'
        if unicode_value == 111:
            inp[value] = 'o'
        if unicode_value == 117:
            inp[value] = 'u'
    return inp