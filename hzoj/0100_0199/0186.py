"""
See: https://oj.haizeix.com/problem/186
"""

import re
from typing import List

n = int(input("Please input a positive integer.\n"))
each_n = input("Please input n positive integers, each splits with a space.\n")

arr = [int(i) for i in re.split(r"\s+", each_n)]


def fn(arr: List[int], n: int) -> int:
    i, result = 0, 0
    while i < n:
        result += 1
        i += arr[i]
    return result


print(fn(arr, n))
