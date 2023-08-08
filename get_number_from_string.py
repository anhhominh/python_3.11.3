def get_number_from_string(string):
    ans = ""
    for str in string:
        if ord(str) >= 48 and ord(str) <= 57:
            ans = ans + str
    return int(ans)