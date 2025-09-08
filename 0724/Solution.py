from typing import List


class Solution:
    """
    See: https://leetcode.cn/problems/find-pivot-index/description/
    """

    def pivotIndex(self, nums: List[int]) -> int:
        _sum, _left = sum(nums), 0
        for i, num in enumerate(nums):
            _right = _sum - num
            if _left == _right:
                return i
            _left += num
            _sum -= num
        return -1
