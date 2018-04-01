"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def solution():
    for c in range(997, 2, -1):
        a, b = 1, 999 - c
        target = c ** 2
        while a < b:
            if a ** 2 + b ** 2 == target:
                return a * b * c
            a += 1
            b -= 1


print(solution())
