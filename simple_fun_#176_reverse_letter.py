def reverse_letter(string):
    str = ""
    for i in string:
        if(ord(i) >= 97 and ord(i) <= 122):
            str = str + i
#     Reverse a String in Python
    return str[::-1]