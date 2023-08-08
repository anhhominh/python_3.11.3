def find_needle(haystack):
    for i in haystack:
        if( i == 'needle'):
            return 'found the needle at position ' + str(haystack.index(i))