def same_case(a, b):
    return a.isupper() == b.isupper() if a.isalpha() and b.isalpha() else -1