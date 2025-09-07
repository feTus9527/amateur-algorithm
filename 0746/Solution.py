from typing import List


class Solution:
    """
    See: https://leetcode.cn/problems/min-cost-climbing-stairs/description/
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        _length = len(cost)
        _f0 = 0
        _f1 = 0
        for i in range(2, _length + 1):
            _f2 = min(_f1 + cost[i - 1], _f0 + cost[i - 2])
            _f0 = _f1
            _f1 = _f2
        return _f1
