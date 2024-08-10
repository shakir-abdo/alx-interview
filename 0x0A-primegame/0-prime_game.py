#!/usr/bin/python3
""" Prime Game func"""


def isWinner(x, nums):
    """Prime game winner function"""
    if x < 1 or not nums:
        return None

    maria = 0
    ben = 0

    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for x in range(2, int(n**0.5) + 1):
        if primes[x]:
            for y in range(x**2, n + 1, x):
                primes[y] = False

    # count the no of pm less than n i nums
    for n in nums:
        count = sum(primes[2 : n + 1])
        ben += count % 2 == 0
        maria += count % 2 == 1

    if maria == ben:
        return None

    return "Maria" if maria > ben else "Ben"
