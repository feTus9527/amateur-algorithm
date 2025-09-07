class Solution:
    """
    See: https://leetcode.cn/problems/length-of-last-word/description/
    """

    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        _s = s[::-1].strip()
        for i in _s:
            if i == " ":
                break
            else:
                result += 1
        return result
