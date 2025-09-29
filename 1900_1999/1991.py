from typing import List


class Solution:
    """
    See: https://leetcode.cn/problems/find-the-middle-index-in-array/description/
    """

    def findMiddleIndex(self, nums: List[int]) -> int:
        _sum = sum(nums)
        _left = 0
        for i, num in enumerate(nums):
            if _left * 2 + num == _sum:
                return i
            _left += num
        return -1
