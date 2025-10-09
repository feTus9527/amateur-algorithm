class Solution:
    """
    See: https://leetcode.cn/problems/find-closest-person/description/
    """

    def findClosest(self, x: int, y: int, z: int) -> int:
        x_to_z = abs(x - z)
        y_to_z = abs(y - z)
        return 0 if x_to_z == y_to_z else 1 if x_to_z < y_to_z else 2
