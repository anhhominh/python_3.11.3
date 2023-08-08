from math import gcd

def solution(a):
    return gcd(*a) * len(a)