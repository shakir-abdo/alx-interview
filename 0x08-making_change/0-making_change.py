#!/usr/bin/python3
"""Change making module"""


def makeChange(coins, total):
    """determine the fewest number of coins needed
    to meet a given amount total."""
    if total <= 0:
        return 0
    coins_count = 0
    coin_index = 0
    rem = total
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_index >= n:
            return -1
        if rem - sorted_coins[coin_index] >= 0:
            rem -= sorted_coins[coin_index]
            coins_count += 1
        else:
            coin_index += 1
    return coins_count
