def shortcut( s ):
    str = ['a','e','i','o','u']
    for x in str:
        s = s.replace(x,'')
    return s