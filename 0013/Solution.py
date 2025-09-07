class Solution:
    """
    See: https://leetcode.cn/problems/roman-to-integer/description/
    """

    _MAPPING = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        result = 0
        _length = len(s)

        for i, ch in enumerate(s):
            _val = Solution._MAPPING[ch]
            if i < _length - 1 and _val < Solution._MAPPING[s[i + 1]]:
                result -= _val
            else:
                result += _val
        return result
