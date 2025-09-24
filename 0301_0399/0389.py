from functools import reduce
from operator import xor


class Solution:
    """
    See: https://leetcode.cn/problems/find-the-difference/description/
    """

    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(xor, map(ord, s + t)))
