def cube_checker(volume, side):
    if volume < 0 or side < 0 or volume == 0:
        return False
    ans = pow(side,3)
    return volume == ans