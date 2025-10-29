"""
See: https://oj.haizeix.com/problem/239
"""

"""
Given a serial number i of a house in rank x:
1. it locates in the number Math.ceil(i / 4) quarter of the city;
2. 
"""


from math import sqrt
from typing import Tuple

GRID_LENGTH = 10


def fn(rank: int, serial_number: int) -> Tuple[int, int]:
    if rank == 1:
        if serial_number == 1:
            return 0, 0
        if serial_number == 2:
            return 0, 1
        if serial_number == 3:
            return 1, 1
        if serial_number == 4:
            return 1, 0
    l = 1 << (rank - 1)
    block = l**2
    if serial_number <= block:
        """
        District 1
        (x, y) -> (y, x)
        """
        x, y = fn(rank - 1, serial_number)
        x, y = y, x
    elif serial_number <= 2 * block:
        """
        District 2
        (x, y) -> (x, y + l)
        """
        x, y = fn(rank - 1, serial_number - block)
        x, y = x, y + l
    elif serial_number <= 3 * block:
        """
        District 3
        (x, y) -> (x + l, y + l)
        """
        x, y = fn(rank - 1, serial_number - 2 * block)
        x, y = x + l, y + l
    else:
        """
        District 3
        (x, y) -> (2 * l - y - 1, l - x - 1)
        """
        x, y = fn(rank - 1, serial_number - 3 * block)
        x, y = 2 * l - y - 1, l - x - 1
    return x, y


T = int(input())

for i in range(T):
    [N, S, D] = [int(item) for item in input().split(" ")]
    sx, sy = fn(N, S)
    dx, dy = fn(N, D)
    print(round(GRID_LENGTH * sqrt((sx - dx) ** 2 + (sy - dy) ** 2)))
