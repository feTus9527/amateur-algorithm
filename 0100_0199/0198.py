from typing import List


class Solution:
    """
    See: https://leetcode.cn/problems/house-robber/description/
    """

    def rob(self, nums: List[int]) -> int:
        _n = len(nums)
        if _n <= 2:
            return max(nums)
        _dp = [0] * (_n + 1)
        _dp[_n - 1] = nums[_n - 1]
        for i in range(_n - 2, -1, -1):
            _dp[i] = max(_dp[i + 1], _dp[i + 2] + nums[i])
        return _dp[0]
