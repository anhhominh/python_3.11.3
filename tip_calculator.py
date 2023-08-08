import math

def calculate_tip(amount, rating):
    if rating.lower() == "terrible":
        return 0
    elif rating.lower() == "poor":
        return math.ceil(amount/100 * 5)
    elif rating.lower() == "good":
        return math.ceil(amount/100 * 10)
    elif rating.lower() == "great":
        return math.ceil(amount/100 * 15)
    elif rating.lower() == "excellent":
        return math.ceil(amount/100 * 20)
    else:
        return 'Rating not recognised'