class Solution:
    """
    See: https://leetcode.cn/problems/repeated-substring-pattern/description/
    """

    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)
