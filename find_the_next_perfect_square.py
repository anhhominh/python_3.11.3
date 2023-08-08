import math # 1 constant

def find_next_square(sq):

    if (math.sqrt(sq)).is_integer() :
    # if (sq/2).is_integer():
         return int(math.sqrt(sq) + 1) **  2
    else:
        return -1