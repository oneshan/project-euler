"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def solution():
    visited = {}
    step, stack = 1, [1]
    while stack:
        next_stack = []
        for num in stack:

            next_num = (num - 1) // 3
            if next_num not in visited and next_num * 3 + 1 == num:
                visited[next_num] = step
                next_stack.append(next_num)

            next_num = num * 2
            if next_num not in visited and next_num < 1000000:
                visited[next_num] = step
                next_stack.append(next_num)

        step += 1
        stack = next_stack

    ans = (num, step)
    for i in range(2, 1000000):
        if i in visited:
            continue
        num, step = i, 0
        while num not in visited:
            step += 1
            if num & 1:
                num = num * 3 + 1
            else:
                num = num // 2
        visited[i] = step + visited[num]
        if visited[i] > ans[-1]:
            ans = (i, visited[i])

    return ans[0]


print(solution())
