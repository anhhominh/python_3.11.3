def rental_car_cost(d):
    if d < 3:
        return d * 40
    elif d >= 3 and d < 7:
        return d * 40 - 20
    elif d >= 7:
        return d * 40 - 50