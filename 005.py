"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solution():
    ans = 2
    for i in range(2, 21):
        ans *= (i / gcd(ans, i))
    return ans


print(solution())
