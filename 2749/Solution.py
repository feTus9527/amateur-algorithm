from itertools import count


class Solution:
    """
    See: https://leetcode.cn/problems/minimum-operations-to-make-the-integer-zero/description/
    """

    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for ops in count(1):
            x = num1 - ops * num2
            if x < 0:
                break
            if int.bit_count(x) <= ops <= x:
                return ops
        return -1
