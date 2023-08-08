def derive(coefficient, exponent): 
    if exponent == 2:
        return f"{coefficient * exponent}x^2"
    return f"{coefficient * exponent}x^{exponent-1}"