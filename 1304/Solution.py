from typing import List


class Solution:
    """
    See: https://leetcode.cn/problems/find-n-unique-integers-sum-up-to-zero/description/
    """

    def sumZero(self, n: int) -> List[int]:
        m = n // 2 + 1
        result = []
        for i in range(1, m):
            result.extend([i, -i])
        return result if n % 2 == 0 else result + [0]
