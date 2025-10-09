from typing import List


class Solution:
    """
    See: https://leetcode.cn/problems/longest-common-prefix/description/
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        _min = min([len(s) for s in strs])
        for i in range(_min):
            if len(set([s[i] for s in strs])) == 1:
                result += strs[0][i]
            else:
                break
        return result
