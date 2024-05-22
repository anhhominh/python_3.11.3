from functools import reduce

ops = {
    "AND": lambda a, b: a and b,
    "OR": lambda a, b: a or b,
    "XOR": lambda a, b: not b if a else b
}


def logical_calc(array, op):
    return reduce(ops[op], array[1:], array[0])