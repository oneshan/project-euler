"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""


def solution():
    n = 110000
    prime = [True for i in range(n + 1)]
    p = 2
    while p ** 2 <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    count = 10001
    for p in range(2, n + 1):
        if prime[p]:
            count -= 1
        if count == 0:
            return p


print(solution())
