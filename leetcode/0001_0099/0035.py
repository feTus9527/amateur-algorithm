from typing import List


class Solution:
    """
    See: https://leetcode.cn/problems/search-insert-position/description/
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = -1, len(nums)
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m
            else:
                r = m
        return r

    def searchInsert_alternative(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)
