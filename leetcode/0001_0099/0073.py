from typing import List


class Solution:
    """
    See: https://leetcode.cn/problems/set-matrix-zeroes/description/
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = [0] * len(matrix), [0] * len(matrix[0])
        for i, r in enumerate(matrix):
            for j, c in enumerate(r):
                if c == 0:
                    m[i] = 1
                    n[j] = 1

        for i, r in enumerate(matrix):
            for j, c in enumerate(r):
                if m[i] == 1 or n[j] == 1:
                    matrix[i][j] = 0
