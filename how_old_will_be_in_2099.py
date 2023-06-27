def calculate_age(year_of_birth, current_year):
    if current_year == year_of_birth:
        return "You were born this very year!"
    if current_year > year_of_birth:
        if current_year - year_of_birth > 1:
            return "You are " + str(current_year - year_of_birth) +" years old."
        else:
            return "You are " + str(current_year - year_of_birth) +" year old."
    if current_year < year_of_birth:
        if year_of_birth - current_year > 1:
            return "You will be born in " + str(year_of_birth - current_year) +" years."
        else:
            return "You will be born in " + str(year_of_birth - current_year) +" year."