class Solution:
    """
    See: https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
    """

    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
