#!/usr/bin/python3
"""Defines function that determine if  box containing  list
   of lists can be opened using key stored in the lists
"""


def canUnlockAll(boxes):
    """Determines if boxe can be unlocked"""
    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False
