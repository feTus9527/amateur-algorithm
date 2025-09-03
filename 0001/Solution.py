from typing import List


class Solution:
    """
    See: https://leetcode.cn/problems/two-sum/description/
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            if map.get(target - num, -1) != -1:
                return [i, map[target - num]]
            map[num] = i
        return [-1, -1]
