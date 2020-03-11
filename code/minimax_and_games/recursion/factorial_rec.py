"""
Compute the factorial with a recursion
"""


def factorial_rec(n):
    if n == 1:
        return 1
    else:
        return factorial_rec(n - 1) * n


print(factorial_rec(10))
