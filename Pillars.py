def pillars(num_pill, dist, width):
    if num_pill < 2:
        return 0
    return num_pill * ((dist * 100) + width) - (width * 2) - (dist * 100);