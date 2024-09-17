#!/usr/bin/python3
"""This function determines the smallest number of coins needed
   to get to a given total
"""


def makeChange(coins, total):
    """This function makes changes to coins and 
    calculates that change.
    """
    if total <= 0:
        return 0
    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
