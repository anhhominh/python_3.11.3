def _all(seq, fun): 
    for item in seq: 
        if not fun(item): 
            return False
    return True