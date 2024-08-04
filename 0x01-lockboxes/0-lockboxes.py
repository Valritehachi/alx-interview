#!/usr/bin/python3
"""a script that uses one list to unlock list of lists"""


def canUnlockAll(boxes):
    """
    a function that uses one list to unlock other list
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
