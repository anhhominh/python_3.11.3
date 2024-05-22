from collections import Counter

def ordered_count(inp):
    c = Counter(inp)
    return sorted(list(c.items()), key=lambda x: inp.index(x[0]))