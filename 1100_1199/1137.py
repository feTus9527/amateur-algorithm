class Solution:
    """
    See: https://leetcode.cn/problems/n-th-tribonacci-number/description/
    """

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        result = 1
        _prev1, _prev2 = 0, 1
        for _ in range(n - 2):
            _tmp = result
            result += _prev1 + _prev2
            _prev1 = _prev2
            _prev2 = _tmp
        return result
