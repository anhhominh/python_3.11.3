def power_of_two(x):
    current_number = 0
    counter = 0
    while current_number <= x:
        current_number = 2**counter
        counter+=1
        if current_number == x:
            return True
    return False  