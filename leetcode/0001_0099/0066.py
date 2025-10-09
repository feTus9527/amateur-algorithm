from typing import List


class Solution:
    """
    See: https://leetcode.cn/problems/plus-one/description/
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        _carry = 0
        result = []
        digits[-1] += 1
        for digit in reversed(digits):
            digit += _carry
            if digit > 9:
                digit -= 10
                _carry = 1
            else:
                _carry = 0
            result.append(digit)
        if _carry == 1:
            result.append(1)
        return list(reversed(result))
