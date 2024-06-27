#!/usr/bin/python3
"""
function that validates whether a
String of ints represents a valid UTF-8 encoding.
"""
from itertools import takewhile


def int_to_bits(nums):
    """
    Convert ints to bits
    """
    for num in nums:
        mask = 1 << 8
        bits = []
        while mask:
            mask >>= 1
            bits.append(bool(num & mask))
        yield bits


def validUTF8(data):
    """
    Takes a list of ints and returns true if the list is
    a valid UTF-8 encoding, else returns false
    Args:
        data : List of ints representing possible UTF-8 encoding
    Return:
        bool: True if the list is a valid UTF-8 encoding,
        else False
    """
    bits = int_to_bits(data)
    for byte in bits:
        if byte[0] == 0:
            continue

        ones = sum(takewhile(bool, byte))
        if ones <= 1:
            return False
        if ones >= 4:
            return False

        for _ in range(ones - 1):
            try:
                byte = next(bits)
            except StopIteration:
                return False
            if byte[0:2] != [1, 0]:
                return False
    return True
