from typing import List


class Solution:
    """
    See: https://leetcode.cn/problems/house-robber/description/
    """

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        _dp = [0] * len(nums)
        _dp[0] = nums[0]
        _dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            _dp[i] = max(_dp[i - 2] + nums[i], _dp[i - 1])
        return _dp[-1]
