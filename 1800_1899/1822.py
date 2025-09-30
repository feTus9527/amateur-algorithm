from typing import List


class Solution:
    """
    See: https://leetcode.cn/problems/sign-of-the-product-of-an-array/description/
    """

    def arraySign(self, nums: List[int]) -> int:
        result = 1
        for num in nums:
            result *= num
        return 1 if result > 0 else (-1 if result < 0 else 0)
