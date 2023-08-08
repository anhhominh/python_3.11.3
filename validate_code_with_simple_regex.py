def validate_code(code):
    code = str(code)
    valid_start = "123"
    index = 0
    for number in code:
        if index == 0 and number in valid_start:
            return True
        index = index + 1
    else:
        return False