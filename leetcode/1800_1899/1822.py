from typing import List


class Solution:
    """
    See: https://leetcode.cn/problems/sign-of-the-product-of-an-array/description/
    """

    def arraySign(self, nums: List[int]) -> int:
        result = 1
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                result = -result
        return result
