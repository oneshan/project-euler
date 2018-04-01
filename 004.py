"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def isProduct(num):
    for i in range(100, 1000):
        if num % i == 0 and 99 < (num / i) < 1000:
            return True
    return False


def solution():
    # Time elapsed: user: 75.1 ms, sys: 26.3 ms, total: 101 ms
    for num in range(998001, 100000, -1):
        if str(num) == str(num)[::-1]:
            if isProduct(num):
                return num


def solution_2():
    # Time elapsed: user: 280 ms, sys: 15.5 ms, total: 296 ms
    ans = 1
    for n1 in range(999, 99, -1):
        for n2 in range(999, 99, -1):
            num = n1 * n2
            if str(num) == str(num)[::-1]:
                ans = max(ans, num)
                break
    return ans


print(solution_2())
