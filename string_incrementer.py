def increment_string(strng):
    head = tail = ''

    for char in strng:
        if char.isdigit():
            tail += char
        else:
            head += tail + char
            tail = ''

    number = int(tail or '0')
    if len(str(number)) < len(tail):
        return head + str(number + 1).zfill(len(tail))
    return head + str(number + 1)