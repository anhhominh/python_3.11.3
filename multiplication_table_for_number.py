def multi_table(number):
    ans = []
    for i in range(1,11):
        tmp = i* number
        ans.append(f"{i} * {number} = {tmp}")
    return '\n'.join(ans)