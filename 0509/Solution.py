class Solution:
    """
    See: https://leetcode.cn/problems/fibonacci-number/description/
    """

    def fib(self, n: int) -> int:
        result = 0
        _prev = 1
        for _ in range(n):
            _tmp = result
            result += _prev
            _prev = _tmp
        return result
