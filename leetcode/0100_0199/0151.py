from typing import List


class Solution:
    """
    See: https://leetcode.cn/problems/reverse-words-in-a-string/description/
    """

    def reverseWords(self, s: str) -> str:
        result, temp = "", ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == " ":
                if temp != "":
                    result += f" {temp}"
                    temp = ""
            else:
                temp = s[i] + temp
            i -= 1

        if temp != "":
            result += f" {temp}"

        return result[1:]
