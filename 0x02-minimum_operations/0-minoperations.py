#!/usr/bin/python3
"""
Calculate the min operations for copy and paste letters
"""


def minOperations(n):
    x = 0
    y = 2
    while n > 1:
        while n % y == 0:
            x += y
            n /= y
        y += 1
    return x
