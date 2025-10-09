class Solution:
    """
    See: https://leetcode.cn/problems/valid-anagram/description/
    """

    def isAnagram(self, s: str, t: str) -> bool:
        _cnt = [0] * 26
        for ch in s:
            _cnt[ord(ch) - ord("a")] += 1
        for ch in t:
            _cnt[ord(ch) - ord("a")] -= 1
        for i in _cnt:
            if i != 0:
                return False
        return True
