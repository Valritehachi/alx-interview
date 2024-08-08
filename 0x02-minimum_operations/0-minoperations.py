#!/usr/bin/python3

"""
    a function that determines the number of minimum operations given to characters
"""


def minOperations(n):
    """
        A function that calculates the fewest number of operations
        needed to give a certain result.
    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
