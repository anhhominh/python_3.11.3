def Xbonacci(signature,n):
    result = signature[:]

    for x in range(n-len(signature)):
        current_fib = 0
        start = len(result) - len(signature)
        for y in result[start:]:
            current_fib += y
        result.append(current_fib)

    return result[:n]