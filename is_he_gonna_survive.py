def hero(bullets, dragons):
    if dragons == 0:
        return True
    if bullets/dragons >= 2:
        return True
    else:
        return False