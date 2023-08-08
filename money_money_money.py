def calculate_years(principal, interest, tax, desired):
    year=0;
    while principal<desired:
        year += 1
        principal=principal+((principal*interest)-(principal*interest*tax))
    return year