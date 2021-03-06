"""
Project Euler Problem 12
========================

The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 =
28. The first ten terms would be:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

   1: 1
   3: 1,3
   6: 1,2,3,6
  10: 1,2,5,10
  15: 1,3,5,15
  21: 1,3,7,21
  28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five
divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""


def solution():

    def prime():
        n = 1000
        prime = [True for i in range(n + 1)]
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * 2, n + 1, p):
                    prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if prime[p]]

    prime_list = prime()

    def get_num_of_divisors(num):
        factors = []
        for p in prime_list:
            count = 0
            while num % p == 0:
                num //= p
                count += 1
            if count:
                factors.append(count)
            if num == 1:
                break

        num_of_div = 1
        for factor in factors:
            num_of_div *= (factor + 1)

        return num_of_div

    num = 0
    for i in range(1, 100000):
        num += i
        if get_num_of_divisors(num) > 500:
            return num


print solution()
