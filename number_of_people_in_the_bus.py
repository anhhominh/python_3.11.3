def number(bus_stops):
    sum1 = 0
    sum2 = 0
    for i in bus_stops:
        sum1 = sum1 + i[0]
        sum2 = sum2 + i[1]
    return sum1 - sum2