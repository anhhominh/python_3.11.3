def square_digits(num):
    if num < 10:
        return num**2
    else:
        nums = []
        while num>0:
            d = num % 10
            nums.append(d)
            num = num // 10
        number = []
        for i in nums:
            number.append(i**2)
        number.reverse()
        list_of_strings = [str(item) for item in number]
        return int(''.join(list_of_strings))