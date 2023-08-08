import collections

def find_it(seq):
    if len( seq ) == 0:
        return None
    b = collections.Counter(seq)
    for c in b:
        if b[c] % 2 ==1:
            return c