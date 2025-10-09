class Solution:
    """
    See: https://leetcode.cn/problems/climbing-stairs/description/
    """

    def climbStairs(self, n: int) -> int:
        result = 1
        _prev = 0
        for _ in range(n):
            _tmp = result
            result += _prev
            _prev = _tmp
        return result
