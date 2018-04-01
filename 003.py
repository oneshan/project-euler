"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def solution():
    num = 600851475143
    factor = 1
    while factor < num:
        factor += 2
        while num % factor == 0:
            num /= factor
    return factor

print(solution())
